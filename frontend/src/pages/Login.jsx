import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import './Login.css';

const LogoIcon = () => (
  <svg width="28" height="28" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M20 30 C20 30 8 26 8 14 C8 14 14 16 18 24" fill="#22c55e" />
    <path d="M20 30 C20 30 32 26 32 14 C32 14 26 16 22 24" fill="#22c55e" />
    <path d="M20 30 C20 30 14 18 20 8 C26 18 20 30 20 30Z" fill="#16a34a" />
  </svg>
);

export default function Login() {
  const [mobileNumber, setMobileNumber] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // Simulate login and redirect to home
    navigate('/home');
  };

  return (
    <div className="auth-page-container">
      {/* Background Image with Overlay */}
      <div className="auth-background" style={{ backgroundImage: "url('/images/artisan_hero_clean.png')" }}>
        <div className="auth-overlay"></div>
      </div>

      {/* Authentication Modal */}
      <motion.div
        className="auth-modal"
        initial={{ y: 30, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
      >
        <div className="auth-header">
          <div className="auth-logo">
            <LogoIcon />
            <span>ArtisanGPS</span>
          </div>
          <h1 className="auth-title">Namaste! Welcome Back to<br />your marketplace dashboard.</h1>
        </div>

        <form className="auth-form" onSubmit={handleLogin}>
          {/* Mobile Number Field */}
          <div className="form-group">
            <label>Mobile Number</label>
            <div className="phone-input-group">
              <div className="country-code">
                <span className="flag">🇮🇳</span>
                <span>+91</span>
                <span className="chevron">▾</span>
              </div>
              <input
                type="tel"
                placeholder="9876543210"
                value={mobileNumber}
                onChange={(e) => setMobileNumber(e.target.value)}
                required
              />
            </div>
          </div>

          {/* Password Field */}
          <div className="form-group">
            <div className="label-row">
              <label>Password</label>
              <Link to="#" className="forgot-password">Forgot Password?</Link>
            </div>
            <div className="password-input-group">
              <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
              <button type="button" className="toggle-password">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                  <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                  <line x1="1" y1="1" x2="23" y2="23"></line>
                </svg>
              </button>
            </div>
          </div>

          <button type="submit" className="auth-btn-primary">Login to Account</button>
        </form>

        <div className="auth-divider">
          <span>OR</span>
        </div>

        <button type="button" className="auth-btn-secondary">Login with OTP</button>

        <div className="auth-footer-text">
          New to ArtisanGPS? <Link to="/signup" className="auth-link">Create an Account</Link>
        </div>

        <div className="auth-bottom-links">
          <Link to="#">HELP CENTER</Link>
          <Link to="#">PRIVACY POLICY</Link>
          <Link to="#">ENGLISH (INDIA)</Link>
        </div>
      </motion.div>
    </div>
  );
}
