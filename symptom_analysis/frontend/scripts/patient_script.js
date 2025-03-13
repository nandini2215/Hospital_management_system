document.getElementById("consultation-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const responseMessage = document.getElementById("response-message");
    responseMessage.innerText = "Sending request...";
    responseMessage.style.color = "#007bff";

    try {
        const response = await fetch("/request_consultation", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                mobile: document.getElementById("mobile").value.trim(),
                disease: document.getElementById("disease").value.trim()
            })
        });

        const data = await response.json();
        responseMessage.innerText = data.message;
        responseMessage.style.color = response.ok ? "#28a745" : "#dc3545";
    } catch (error) {
        console.error("Error:", error);
        responseMessage.innerText = "An error occurred. Please try again later.";
        responseMessage.style.color = "#dc3545";
    }
});
