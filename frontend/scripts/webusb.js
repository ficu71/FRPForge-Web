class WebUSB {
    static async getDevices() {
        try {
            const filters = [
                { vendorId: 0x04e8 }, // Samsung
                { vendorId: 0x2717 }, // Xiaomi
                { vendorId: 0x12d1 }, // Huawei
                { vendorId: 0x1bbb }  // Oppo
            ];
            const devices = await navigator.usb.getDevices();
            return devices.map(device => ({
                id: device.serialNumber || `device_${Math.random().toString(36).slice(2)}`,
                vendor: this.getVendorName(device.vendorId),
                model: device.productName || 'Unknown'
            }));
        } catch (error) {
            console.error('Błąd WebUSB:', error);
            return [
                { id: 'device1', vendor: 'Samsung', model: 'Galaxy A50' },
                { id: 'device2', vendor: 'Xiaomi', model: 'Redmi Note 9' },
                { id: 'device3', vendor: 'Huawei', model: 'P30' },
                { id: 'device4', vendor: 'Oppo', model: 'Reno 6' }
            ]; // Fallback dla demo
        }
    }

    static async connect(deviceId) {
        const devices = await this.getDevices();
        const device = devices.find(d => d.id === deviceId);
        if (!device) throw new Error('Urządzenie nie znalezione');
        await device.open();
        await device.selectConfiguration(1);
        await device.claimInterface(0);
        console.log(`Połączono z ${deviceId}`);
        return device;
    }

    static getVendorName(vendorId) {
        const vendors = {
            0x04e8: 'Samsung',
            0x2717: 'Xiaomi',
            0x12d1: 'Huawei',
            0x1bbb: 'Oppo'
        };
        return vendors[vendorId] || 'Nieznany';
    }
}
