const API_URL = 'http://localhost:5000/api';
const socket = io('http://localhost:5000');

socket.on('log', data => {
    logMessage(`[WebSocket] ${data.message}`);
});

async function populateVendorDropdown() {
    const vendors = ['Samsung', 'Xiaomi', 'Huawei', 'Oppo'];
    const select = document.getElementById('vendor-select');
    vendors.forEach(vendor => {
        const option = document.createElement('option');
        option.value = vendor.toLowerCase();
        option.textContent = vendor;
        select.appendChild(option);
    });
}

async function scanDevices() {
    try {
        const devices = await WebUSB.getDevices();
        if (devices.length === 0) {
            logMessage('Nie wykryto urządzeń. Upewnij się, że debugowanie USB jest włączone.');
            return;
        }
        displayDevices(devices);
    } catch (error) {
        logMessage(`Błąd skanowania urządzeń: ${error}`);
    }
}

function displayDevices(devices) {
    const deviceList = document.getElementById('device-list');
    deviceList.innerHTML = '<h3>Wykryte Urządzenia</h3>';
    devices.forEach(device => {
        const div = document.createElement('div');
        div.innerHTML = `<input type="radio" name="device" value="${device.id}"> ${device.vendor} ${device.model}`;
        deviceList.appendChild(div);
    });
}

async function runBypass() {
    const vendor = document.getElementById('vendor-select').value;
    const deviceId = document.querySelector('input[name="device"]:checked')?.value;
    
    if (!vendor || !deviceId) {
        logMessage('Wybierz producenta i urządzenie');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/bypass/${vendor}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ device_id: deviceId }),
        });
        const data = await response.json();
        if (data.status === 'success') {
            displaySteps(data.result);
            displayProgressChart(data.result);
        } else {
            logMessage(`Błąd: ${data.message}`);
        }
    } catch (error) {
        logMessage(`Błąd podczas bypassu: ${error}`);
    }
}

async function runAccessibilityExploit() {
    const vendor = document.getElementById('vendor-select').value;
    const deviceId = document.querySelector('input[name="device"]:checked')?.value;
    
    if (!vendor || !deviceId) {
        logMessage('Wybierz producenta i urządzenie');
        return;
    }
    
    try {
        const response = await fetch(`${API_URL}/accessibility/${vendor}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ device_id: deviceId }),
        });
        const data = await response.json();
        if (data.status === 'success') {
            logMessage(`Exploit Accessibility: ${data.output}`);
        } else {
            logMessage(`Błąd: ${data.message}`);
        }
    } catch (error) {
        logMessage(`Błąd w exploicie Accessibility: ${error}`);
    }
}

async function flashTWRP() {
    const deviceId = document.querySelector('input[name="device"]:checked')?.value;
    const twrpImagePath = prompt('Podaj ścieżkę do obrazu TWRP:');
    if (!deviceId || !twrpImagePath) {
        logMessage('Wybierz urządzenie i podaj ścieżkę do obrazu TWRP');
        return;
    }
    try {
        const response = await fetch(`${API_URL}/flash_twrp`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ device_id: deviceId, twrp_image_path: twrpImagePath }),
        });
        const data = await response.json();
        logMessage(data.status === 'success' ? `TWRP zaflashowane: ${data.output}` : `Błąd: ${data.message}`);
    } catch (error) {
        logMessage(`Błąd podczas flashowania TWRP: ${error}`);
    }
}

function displaySteps(steps) {
    const logOutput = document.getElementById('log-output');
    logOutput.innerHTML = '<h3>Kroki Bypassu</h3>';
    steps.forEach(step => {
        const p = document.createElement('p');
        p.textContent = `[${step.status.toUpperCase()}] ${step.step}: ${step.output || step.error}`;
        logOutput.appendChild(p);
    });
}

function displayProgressChart(steps) {
    const ctx = document.getElementById('progress-chart').getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: steps.map(s => s.step),
            datasets: [{
                label: 'Postęp',
                data: steps.map(s => s.status === 'success' ? 100 : 0),
                backgroundColor: steps.map(s => s.status === 'success' ? '#4caf50' : '#f44336'),
                borderColor: steps.map(s => s.status === 'success' ? '#388e3c' : '#d32f2f'),
                borderWidth: 1
            }]
        },
        options: {
            scales: { y: { beginAtZero: true, max: 100 } }
        }
    });
}

function logMessage(message) {
    const logOutput = document.getElementById('log-output');
    const p = document.createElement('p');
    p.textContent = message;
    logOutput.appendChild(p);
}

document.getElementById('scan-devices').addEventListener('click', scanDevices);
document.getElementById('run-bypass').addEventListener('click', runBypass);
document.getElementById('demo-mode').addEventListener('click', () => {
    const vendor = document.getElementById('vendor-select').value;
    runDemoMode(vendor);
});
document.getElementById('flash-twrp').addEventListener('click', flashTWRP);
document.getElementById('accessibility-exploit').addEventListener('click', runAccessibilityExploit);
document.addEventListener('DOMContentLoaded', populateVendorDropdown);
