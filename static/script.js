const taskSelect = document.getElementById("task");
const levelBox = document.getElementById("levelBox");
const output = document.getElementById("output");

taskSelect.addEventListener("change", function () {
    if (taskSelect.value === "learn") {
        levelBox.classList.remove("hidden");
    } else {
        levelBox.classList.add("hidden");
    }
});

async function sendRequest() {
    const task = document.getElementById("task").value;
    const input = document.getElementById("userInput").value.trim();
    const level = document.getElementById("level").value;

    if (!input) {
        output.textContent = "Please enter some text first.";
        return;
    }

    output.textContent = "Generating response...";

    try {
        let response;

        if (task === "qa") {
            response = await fetch("/qa", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ question: input })
            });
        }

        if (task === "explain") {
            response = await fetch("/explain", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ topic: input })
            });
        }

        if (task === "quiz") {
            response = await fetch("/quiz", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: input })
            });
        }

        if (task === "summarize") {
            response = await fetch("/summarize", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ text: input })
            });
        }

        if (task === "learn") {
            response = await fetch(`/learn/recommendations?topic=${encodeURIComponent(input)}&level=${encodeURIComponent(level)}`);
        }

        const data = await response.json();
        output.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        output.textContent = "Something went wrong. Please check the server and try again.";
    }
}
