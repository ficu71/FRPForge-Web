async function runDemoMode(vendor) {
    try {
        const steps = [
            { step: "Symulacja kroku 1", status: "success", output: "Zakończono" },
            { step: "Symulacja kroku 2", status: "success", output: "Zakończono" }
        ];
        displaySteps(steps);
        displayProgressChart(steps);
        logMessage(`Tryb demo dla ${vendor} uruchomiony lokalnie`);
    } catch (error) {
        logMessage(`Błąd w trybie demo: ${error}`);
    }
}
