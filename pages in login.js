import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { login, signup } from "../api";

const Login = () => {
  const navigate = useNavigate();

  const [isSignup, setIsSignup] = useState(false);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // -------------------------
  // SUBMIT HANDLER
  // -------------------------
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setLoading(true);

    try {
      let res;
      if (isSignup) {
        res = await signup({ email, password });
      } else {
        res = await login({ email, password });
      }

      // Save JWT
      localStorage.setItem("token", res.data.access_token);

      // Redirect to main chat
      navigate("/");
    } catch (err) {
      setError(
        err.response?.data?.detail ||
          "Authentication failed. Try again."
      );
    } finally {
      setLoading(false);
    }
  };

  // -------------------------
  // UI
  // -------------------------
  return (
    <div className="auth-page">
      <div className="auth-box">
        <h2>{isSignup ? "Create Account" : "Login"}</h2>

        {error && (
          <div style={{ color: "#ff4d4d", marginBottom: 10 }}>
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email address"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit" disabled={loading}>
            {loading
              ? "Please wait..."
              : isSignup
              ? "Sign Up"
              : "Login"}
          </button>
        </form>

        <div
          className="auth-switch"
          onClick={() => setIsSignup(!isSignup)}
        >
          {isSignup
            ? "Already have an account? Login"
            : "New here? Create an account"}
        </div>
      </div>
    </div>
  );
};

export default Login;