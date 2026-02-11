import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";

import Login from "./pages/Login";
import Chat from "./pages/Chat";
import Plans from "./pages/Plans";
import History from "./pages/History";
import Profile from "./pages/Profile";

import BrainHeader from "./components/BrainHeader";

import "./styles.css";

/* ---------------------------------------
   AUTH CHECK
---------------------------------------- */
const isAuthenticated = () => {
  return !!localStorage.getItem("token");
};

/* ---------------------------------------
   PROTECTED ROUTE
---------------------------------------- */
const ProtectedRoute = ({ children }) => {
  if (!isAuthenticated()) {
    return <Navigate to="/login" replace />;
  }
  return children;
};

function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Header only after login */}
        {isAuthenticated() && <BrainHeader />}

        <Routes>
          {/* AUTH */}
          <Route path="/login" element={<Login />} />

          {/* MAIN CHAT */}
          <Route
            path="/"
            element={
              <ProtectedRoute>
                <Chat />
              </ProtectedRoute>
            }
          />

          {/* PLANS */}
          <Route
            path="/plans"
            element={
              <ProtectedRoute>
                <Plans />
              </ProtectedRoute>
            }
          />

          {/* HISTORY */}
          <Route
            path="/history"
            element={
              <ProtectedRoute>
                <History />
              </ProtectedRoute>
            }
          />

          {/* PROFILE */}
          <Route
            path="/profile"
            element={
              <ProtectedRoute>
                <Profile />
              </ProtectedRoute>
            }
          />

          {/* FALLBACK */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;