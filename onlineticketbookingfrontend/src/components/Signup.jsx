import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import "../styles/Signup.css";

export default function Signup() {
  const [formData, setFormData] = useState({
    username: "",   // ✅ backend expects "username", not fullName
    email: "",
    password: "",
    confirmPassword: "", // for frontend validation only
  });

  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");
    setSuccess("");

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match");
      return;
    }

    try {
      const payload = {
        username: formData.username,
        email: formData.email,
        password: formData.password,
      };

      await axios.post("http://127.0.0.1:8000/users/signup", payload);
      setSuccess("OTP sent to your email!");
      navigate("/verify-otp", { state: { email: formData.email } });
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to send OTP");
    }
  };

  return (
    <div className="signup-container">
      <div className="signup-box">
        <h2 className="signup-title">Create Account</h2>
        {error && <p className="error-message">{error}</p>}
        {success && <p className="success-message">{success}</p>}

        <form onSubmit={handleSubmit} className="signup-form">
          <div>
            <input
              type="text"
              name="username"   // ✅ matches backend
              placeholder="Username"
              value={formData.username}
              onChange={handleChange}
              className="signup-input"
              required
            />
          </div>
          <div>
            <input
              type="email"
              name="email"
              placeholder="Email"
              value={formData.email}
              onChange={handleChange}
              className="signup-input"
              required
            />
          </div>
          <div>
            <input
              type="password"
              name="password"
              placeholder="Password"
              value={formData.password}
              onChange={handleChange}
              className="signup-input"
              required
            />
          </div>
          <div>
            <input
              type="password"
              name="confirmPassword"
              placeholder="Confirm Password"
              value={formData.confirmPassword}
              onChange={handleChange}
              className="signup-input"
              required
            />
          </div>
          <button type="submit" className="signup-button">
            Send OTP
          </button>
        </form>

        <p className="signup-footer">
          Already have an account?{" "}
          <Link to="/" className="signin-link">
            Sign In
          </Link>
        </p>
      </div>
    </div>
  );
}
