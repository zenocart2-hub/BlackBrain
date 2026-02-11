import React from "react";

/*
  ChatBubble Component
  --------------------
  Props:
  - sender: "user" | "brain"
  - text: string
*/

const ChatBubble = ({ sender, text }) => {
  const isUser = sender === "user";

  return (
    <div
      className={`chat-bubble ${
        isUser ? "chat-user" : "chat-brain"
      }`}
    >
      <pre
        style={{
          whiteSpace: "pre-wrap",
          wordBreak: "break-word",
          margin: 0
        }}
      >
        {text}
      </pre>
    </div>
  );
};

export default ChatBubble;