const chatBox = document.getElementById("chat-box");
const chatForm = document.getElementById("chat-form");
const chatInput = document.getElementById("chat-input");

function addMessage(text, sender) {
    const message = document.createElement("div");
    message.classList.add("message", sender);
    message.textContent = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// LLM intro on page load
window.addEventListener("load", () => {
    addMessage("Hello! I'm Ryan Gao. Ask me anything about my experience and background.", "bot");
});

chatForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const userMessage = chatInput.value.trim();
    if (!userMessage) return;

    addMessage(userMessage, "user");
    chatInput.value = "";

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({message: userMessage})
        });

        const data = await response.json();
        if (data.reply) {
            addMessage(data.reply, "bot");
        } else {
            addMessage("Error: No reply received.", "bot");
        }
    } catch (err) {
        addMessage("Error connecting to server.", "bot");
        console.error(err);
    }
});
