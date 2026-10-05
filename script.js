async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();

  if (!message) return;

  input.value = "";

  const chatBox = document.getElementById("chat-box");

  chatBox.innerHTML += `<p><b>You:</b> ${message}</p>`;

  try {
    const response = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    chatBox.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;

  } catch (error) {
    console.error(error);
    chatBox.innerHTML += `<p><b>Error:</b> Backend is not connected.</p>`;
  }
}


const input = document.getElementById("user-input");

input.addEventListener("keydown", function(event) {
  if (event.key === "Enter") {
    event.preventDefault();
    sendMessage();
  }
});