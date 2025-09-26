const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");

chatForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = userInput.value.trim();
  if (!message) return;

  // Display user's message
  const userMsgDiv = document.createElement("div");
  userMsgDiv.className = "chat-message user-message";
  userMsgDiv.textContent = message;
  chatBox.appendChild(userMsgDiv);
  chatBox.scrollTop = chatBox.scrollHeight;

  userInput.value = "";

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    const botMsgDiv = document.createElement("div");
    botMsgDiv.className = "chat-message bot-message";
    botMsgDiv.textContent = data.reply || data.error;
    chatBox.appendChild(botMsgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
  } catch (err) {
    console.error("Fetch/JSON error:", err);
  }
});
