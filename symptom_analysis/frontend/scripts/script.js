async function predictDisease() {
    const symptoms = document.getElementById("symptoms").value.trim();
    const predictBtn = document.getElementById("predict-btn");
    const loading = document.getElementById("loading");
    const resultDiv = document.getElementById("result");

    if (!symptoms) {
        alert("Please enter symptoms!");
        return;
    }

    try {
        // Show loading animation and disable button
        loading.classList.remove("hidden");
        resultDiv.classList.add("hidden");
        predictBtn.disabled = true;
        predictBtn.innerText = "Predicting...";

        const response = await fetch("/disease/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ symptoms })
        });

        const data = await response.json();

        if (!response.ok) throw new Error(data.error || "Failed to predict disease");

        // Hide loading and show results
        loading.classList.add("hidden");
        resultDiv.classList.remove("hidden");

        // Display result values
        document.getElementById("disease").innerText = data.disease || "Not available";
        document.getElementById("description").innerText = data.description || "No description available";
        document.getElementById("medications").innerText = data.medications?.join(", ") || "No medications available";
        document.getElementById("precautions").innerText = data.precautions?.join(", ") || "No precautions available";
        document.getElementById("diet").innerText = data.diet || "No diet recommendations";
        document.getElementById("workout").innerText = data.workout || "No workout suggestions";
    } catch (error) {
        console.error("Error:", error);
        alert(error.message || "Something went wrong. Please try again.");
    } finally {
        // Reset button
        predictBtn.disabled = false;
        predictBtn.innerText = "🔍 Predict";
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const registerForm = document.querySelector("#register-form");
    if (registerForm) {
        registerForm.addEventListener("submit", (e) => {
            const password = document.querySelector("#password").value;
            const confirmPassword = document.querySelector("#confirm-password").value;
            if (password !== confirmPassword) {
                e.preventDefault();
                alert("Passwords do not match!");
            }
        });
    }
});
