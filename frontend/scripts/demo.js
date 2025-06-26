async function runDemoMode(vendor) {
    try {
        const response = await fetch(`${API_URL}/demo/${vendor}`);
        const data = await response.json();
        if (data.status === 'success') {
            displaySteps(data.steps);
            displayProgressChart(data.steps);
        } else {
            logMessage(`Błąd w trybie demo: ${data.message}`);
        }
    } catch (error) {
        logMessage(`Błąd w trybie demo: ${error}`);
    }
}
