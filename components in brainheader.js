import React from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { logout } from "../api";

const BrainHeader = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    if (window.confirm("Logout from BlackBrain?")) {
      logout();
      navigate("/login");
    }
  };

  return (
    <header className="brain-header">
      {/* APP NAME */}
      <h1>BlackBrain</h1>

      {/* NAVIGATION */}
      <nav>
        <NavLink
          to="/"
          end
          className={({ isActive }) => (isActive ? "active" : "")}
        >
          Chat
        </NavLink>

        <NavLink
          to="/plans"
          className={({ isActive }) => (isActive ? "active" : "")}
        >
          Plans
        </NavLink>

        <NavLink
          to="/history"
          className={({ isActive }) => (isActive ? "active" : "")}
        >
          History
        </NavLink>

        <NavLink
          to="/profile"
          className={({ isActive }) => (isActive ? "active" : "")}
        >
          Profile
        </NavLink>

        <span
          onClick={handleLogout}
          style={{
            marginLeft: 14,
            fontSize: 14,
            color: "#ff4d4d",
            cursor: "pointer"
          }}
        >
          Logout
        </span>
      </nav>
    </header>
  );
};

export default BrainHeader;