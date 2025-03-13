document.addEventListener("DOMContentLoaded", () => {
    const symptomsInput = document.getElementById("symptoms");
    const predictBtn = document.getElementById("predict-btn");
    const loading = document.getElementById("loading");
    const resultDiv = document.getElementById("result");

    predictBtn.addEventListener("click", async () => {
        const symptoms = symptomsInput.value.trim();

        if (!symptoms) {
            showAlert("Please enter your symptoms!");
            return;
        }

        toggleLoading(true);

        try {
            const response = await fetch("/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ symptoms })
            });

            const data = await response.json();

            if (data.error) {
                showAlert(data.error);
            } else {
                displayResults(data);
            }
        } catch (error) {
            console.error("Error:", error);
            showAlert("Something went wrong. Please try again later.");
        } finally {
            toggleLoading(false);
        }
    });

    function toggleLoading(isLoading) {
        if (isLoading) {
            loading.classList.remove("hidden");
            resultDiv.classList.add("hidden");
            predictBtn.disabled = true;
            predictBtn.innerText = "Predicting...";
        } else {
            loading.classList.add("hidden");
            predictBtn.disabled = false;
            predictBtn.innerText = "🔍 Predict";
        }
    }

    function displayResults(data) {
        document.getElementById("disease").innerText = data.disease || "N/A";
        document.getElementById("description").innerText = data.description || "No description available.";
        document.getElementById("medications").innerText = data.medications?.join(", ") || "No medications suggested.";
        document.getElementById("precautions").innerText = data.precautions?.join(", ") || "No precautions provided.";
        document.getElementById("diet").innerText = data.diet || "No dietary recommendations.";
        document.getElementById("workout").innerText = data.workout || "No workout suggestions.";

        resultDiv.classList.remove("hidden");
        setTimeout(() => resultDiv.classList.add("show-result"), 100);
    }

    function showAlert(message) {
        alert(message);
    }
});
