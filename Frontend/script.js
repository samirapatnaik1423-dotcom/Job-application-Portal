const API_URL = "https://x6auz96v35.execute-api.ap-south-2.amazonaws.com/prod/apply";

document.getElementById("applicationForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const message = document.getElementById("message");

    const data = {
        fullName: document.getElementById("fullName").value,
        email: document.getElementById("email").value,
        phoneNumber: document.getElementById("phoneNumber").value,
        qualification: document.getElementById("qualification").value,
        experience: document.getElementById("experience").value,
        skills: document.getElementById("skills").value,
        coverLetter: document.getElementById("coverLetter").value
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (response.ok) {
            message.className = "success";
            message.innerText = "Application submitted successfully!";
            document.getElementById("applicationForm").reset();
        } else {
            message.className = "error";
            message.innerText = result.message || "Submission failed";
        }

    } catch (error) {
        message.className = "error";
        message.innerText = "Error connecting to server";
    }
});