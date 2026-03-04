import { Link } from "react-router-dom";
import "./Landing.css";

export default function LandingPage() {
    return (
        <div className="landing-container">
            {/* ══════════════════════════════════════════
                HERO — 100vh, navbar floated on top
            ══════════════════════════════════════════ */}
            <section className="hero-section">
                {/* Background image — full cover */}
                <img
                    src="/images/artisan_hero_clean.png"
                    alt="Indian artisan craftsman in workshop"
                    className="hero-bg-img"
                />

                {/* Subtle left-to-right gradient */}
                <div className="hero-gradient" />

                {/* ── NAVBAR — transparent, floated over hero ── */}
                <header className="hero-header">
                    {/* Logo */}
                    <Link to="/" className="hero-logo">
                        <img src="/images/logo.png" alt="ArtisanGPS" style={{ height: '40px', width: 'auto' }} />
                    </Link>

                    {/* Center Nav */}
                    <nav className="hero-nav">
                        <Link to="#" className="hero-nav-link">Platform</Link>
                        <Link to="#" className="hero-nav-link">Our Impact</Link>
                        <Link to="#" className="hero-nav-link">Partnerships</Link>
                    </nav>

                    {/* CTA */}
                    <Link to="/home" className="hero-cta-btn">
                        Get Started
                    </Link>
                </header>

                {/* ── HERO TEXT — left side, vertically centered ── */}
                <div className="hero-text-container">
                    <p className="hero-eyebrow">
                        Preserving Indian Heritage
                    </p>

                    <h1 className="hero-headline">
                        Empowering Indian<br />
                        Craft with{" "}
                        <span style={{ color: "#F5A623" }}>AI</span>
                        <br />
                        Intelligence
                    </h1>

                    <p className="hero-subtext">
                        Bridge the gap between traditional heritage and global
                        markets. AI-driven insights designed for the Indian rural
                        artisan ecosystem.
                    </p>

                    <div className="hero-buttons">
                        <Link to="/home" className="hero-btn-primary">
                            For Partners →
                        </Link>
                        <Link to="#" className="hero-btn-secondary">
                            Learn More
                        </Link>
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════
                FEATURES SECTION
            ══════════════════════════════════════════ */}
            <section className="features-section">
                <div className="features-header">
                    <h2>Precision Intelligence for Every Loom</h2>
                    <p>Combining auspicious traditions with cutting-edge data to help artisans thrive in a digital first economy.</p>
                </div>

                <div className="features-grid">
                    {/* Market Intelligence */}
                    <div className="feature-card">
                        <div className="feature-icon-wrapper">
                            <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
                                <circle cx="12" cy="8" r="4" fill="#F5A623" />
                                <path d="M4 20c0-3.3 3.6-6 8-6s8 2.7 8 6" stroke="#F5A623" strokeWidth="2" strokeLinecap="round" />
                            </svg>
                        </div>
                        <h3>Market Intelligence</h3>
                        <p>Understand global demand shifts. Our AI translates complex market signals into actionable local advice.</p>
                    </div>

                    {/* Trend Forecasting */}
                    <div className="feature-card">
                        <div className="feature-icon-wrapper">
                            <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
                                <polyline points="3,16 7,11 11,14 16,7 21,10" stroke="#F5A623" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round" fill="none" />
                            </svg>
                        </div>
                        <h3>Trend Forecasting</h3>
                        <p>Predict colors, motifs, and textures for upcoming seasons based on real-time fashion week data.</p>
                    </div>

                    {/* Smart Pricing */}
                    <div className="feature-card">
                        <div className="feature-icon-wrapper">
                            <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
                                <path d="M17 6H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H7M12 3v18" stroke="#F5A623" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
                            </svg>
                        </div>
                        <h3>Smart Pricing</h3>
                        <p>Optimize margins with transparent cost-benefit analysis and dynamic raw material tracking.</p>
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════
                3-STEPS SECTION
            ══════════════════════════════════════════ */}
            <section className="steps-section">
                <div className="steps-container">
                    {/* Left: Steps */}
                    <div className="steps-left">
                        <h2>Simplified Intelligence in Three Steps</h2>

                        <div className="steps-list">
                            {[
                                { n: "1", title: "Connect Your Craft", body: "Register as an artisan, NGO, or partner through our visual-first onboarding interface." },
                                { n: "2", title: "Receive Daily Feed", body: "Get personalized trend videos and market insights tailored to your specific craft type." },
                                { n: "3", title: "Optimize & Grow", body: "Use smart pricing calculators and forecast tools to maximize every product's value." },
                            ].map(({ n, title, body }) => (
                                <div key={n} className="step-item">
                                    <div className="step-number">{n}</div>
                                    <div>
                                        <h4>{title}</h4>
                                        <p>{body}</p>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Right: Loom image + badge overlapping below */}
                    <div className="steps-right">
                        <div className="loom-image-wrapper">
                            <img
                                src="/images/loom_weaving.png"
                                alt="Loom weaving"
                                className="loom-image"
                            />
                        </div>
                        {/* Badge */}
                        <div className="loom-badge">
                            <svg width="20" height="20" viewBox="0 0 24 24" fill="none">
                                <path d="M3 17l5-5 4 4 6-7" stroke="#F5A623" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
                            </svg>
                            <div>
                                <p className="badge-title">Efficiency Gain</p>
                                <p className="badge-value">+34% Revenue</p>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════
                CTA BANNER
            ══════════════════════════════════════════ */}
            <section className="cta-banner-section">
                <div className="cta-banner-box">
                    <h2>Join the Revolution of<br />Digital Craftsmanship</h2>
                    <p>
                        Be part of the platform that is preserving Indian heritage through modern
                        intelligence. We are looking for partners and visionaries.
                    </p>
                    <div className="cta-banner-actions">
                        <Link to="/home" className="cta-btn-primary">Become a Partner</Link>
                        <Link to="#" className="cta-btn-secondary">Contact Us</Link>
                    </div>
                </div>
            </section>

            {/* ══════════════════════════════════════════
                FOOTER
            ══════════════════════════════════════════ */}
            <footer className="footer-section">
                <div className="footer-container">
                    {/* Top row */}
                    <div className="footer-top">
                        {/* Brand */}
                        <div className="footer-brand">
                            <div className="footer-logo">
                                <img src="/images/logo.png" alt="ArtisanGPS" style={{ height: '32px', backgroundColor: 'white', padding: '4px', borderRadius: '4px' }} />
                            </div>
                            <p className="footer-desc">
                                An AI-first market intelligence platform designed to empower rural Indian artisans with global insights.
                            </p>
                        </div>

                        {/* Nav columns */}
                        <div className="footer-links">
                            {[
                                { title: "Platform", links: ["How it Works", "Pricing Data", "Success Stories"] },
                                { title: "Connect", links: ["For NGOs", "For Government", "Retail Partners"] },
                                { title: "Resources", links: ["Blog", "Report", "Terms"] },
                            ].map(({ title, links }) => (
                                <div key={title} className="footer-link-col">
                                    <h5>{title}</h5>
                                    <ul>
                                        {links.map(item => (
                                            <li key={item}>
                                                <Link to="#">{item}</Link>
                                            </li>
                                        ))}
                                    </ul>
                                </div>
                            ))}
                        </div>
                    </div>

                    {/* Partners row */}
                    <div className="footer-partners">
                        <p>Our Ecosystem Partners</p>
                        <div className="partner-bars">
                            {[80, 110, 90, 130].map((w, i) => (
                                <div key={i} className="partner-bar" style={{ width: `${w}px` }} />
                            ))}
                        </div>
                    </div>

                    {/* Copyright */}
                    <div className="footer-copyright">
                        <p>© 2024 ArtisanGPS Market Intelligence. All Rights Reserved.</p>
                    </div>
                </div>
            </footer>
        </div>
    );
}
