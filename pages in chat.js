import React, { useState } from "react";
import { askBrain } from "../api";

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [mode, setMode] = useState("basic");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // -------------------------
  // SEND MESSAGE
  // -------------------------
  const sendMessage = async () => {
    if (!input.trim()) return;

    setError("");

    const userMessage = {
      sender: "user",
      text: input
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await askBrain(input, mode);

      const brainMessage = {
        sender: "brain",
        text: JSON.stringify(res.data.response, null, 2)
      };

      setMessages((prev) => [...prev, brainMessage]);
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          "Something went wrong. Try again."
      );
    } finally {
      setLoading(false);
    }
  };

  // -------------------------
  // ENTER KEY SUPPORT
  // -------------------------
  const handleKeyPress = (e) => {
    if (e.key === "Enter") {
      sendMessage();
    }
  };

  // -------------------------
  // UI
  // -------------------------
  return (
    <div className="chat-page">
      {/* MODE SELECT */}
      <div style={{ marginBottom: 12 }}>
        <select
          value={mode}
          onChange={(e) => setMode(e.target.value)}
          style={{
            width: "100%",
            padding: 10,
            borderRadius: 8,
            background: "#1c1c1c",
            color: "#fff",
            border: "none"
          }}
        >
          <option value="basic">Basic Brain</option>
          <option value="decision">Decision Brain</option>
          <option value="study">Study Brain</option>
          <option value="money">Money Brain</option>
          <option value="problem">Problem Breaker</option>
          <option value="nobullshit">No Bullsh*t Mode</option>
        </select>
      </div>

      {/* CHAT BOX */}
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`chat-bubble ${
              msg.sender === "user"
                ? "chat-user"
                : "chat-brain"
            }`}
          >
            <pre
              style={{
                whiteSpace: "pre-wrap",
                wordBreak: "break-word"
              }}
            >
              {msg.text}
            </pre>
          </div>
        ))}

        {loading && (
          <div className="chat-bubble chat-brain">
            Thinking...
          </div>
        )}
      </div>

      {error && (
        <div style={{ color: "#ff4d4d", marginBottom: 10 }}>
          {error}
        </div>
      )}

      {/* INPUT */}
      <div className="chat-input-box">
        <input
          type="text"
          placeholder="Ask BlackBrain..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
        />
        <button onClick={sendMessage} disabled={loading}>
          Send
        </button>
      </div>
    </div>
  );
};

export default Chat;