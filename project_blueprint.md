# Project Blueprint: AI-for-Artisans

## 1. Project Overview & Vision
**AI-for-Artisans** (internally known as *ArtisanGPS*) is an innovative digital platform designed to empower traditional and rural artisans. The platform aims to bridge the gap between age-old craftsmanship and modern market demands by leveraging artificial intelligence to provide actionable insights, predictive market trends, material cost analysis, and a unified production planner. 

The ultimate goal is to offer artisans a sophisticated, accessible dashboard to manage their business, optimize their stock, and increase their overall lifetime earnings.

---

## 2. Core Features & User Workflows
The platform is built around a central, user-friendly **Dashboard** where artisans can:
- **Home Hub**: View daily priority tasks (e.g., "Start Weaving for Diwali Stock"), dynamic market nudges, operations alerts (e.g., humidity affecting dyes), and quick actionable questions.
- **Trend Feed**: Explore aesthetic and demanded visual design trends with integrated AI metrics for consumer interest.
- **Material Costs (Constraints)**: Monitor real-time local mandi/market prices for raw materials (yarn, dyes) and calculate dynamic profit margins.
- **Production Advisor**: Engage in an interactive session (voice/text) to receive step-by-step guidance on creating trending products efficiently.
- **My Crafts (Inventory)**: Manage existing product lines, check stock quantities, and list new products for sale.
- **Artisan Profile**: A sharable, verified identity page showcasing the artisan's lifetime earnings, order fulfillment rates, dedicated biography, and specialized skillset.

---

## 3. Technology Stack

### Frontend (Client-Side)
- **Framework**: React.js 
- **Tooling**: Vite (for rapid development and optimized builds)
- **Routing**: React Router (`react-router-dom`)
- **Styling**: Pure modern CSS with responsive layouts (flexbox/grid) 
- **Key Libraries**: `framer-motion` (for smooth micro-animations and page transitions)
- **Architecture**: A modular component structure built around a persistent `DashboardLayout` featuring a responsive mobile/desktop sidebar.

### Backend (Server-Side)
- **Framework**: FastAPI (Python)
- **Why FastAPI?**: Chosen specifically for its high performance, native asynchronous capabilities, and seamless integration with the Python Data Science and Machine Learning ecosystem.
- **API Documentation**: Auto-generated interactive Swagger UI & ReDoc.
- **Database (Proposed)**: PostgreSQL (via SQLAlchemy ORM) for relational integrity, or MongoDB (via Motor) for flexible, document-based schemas depending on product catalog complexity.
- **Validation**: Pydantic (for strict type hinting and request/response validation).

### Data & Machine Learning (AI Integration)
The Python backend will host and serve inferences for:
- **Time-Series Forecasting**: Predicting raw material cost fluctuations and seasonal product demand (e.g., Diwali sarees).
- **Computer Vision/Generative AI**: Suggesting new design motifs (e.g., Peacock motifs) or analyzing uploaded artisan products.
- **NLP (Language Processing)**: Powering the "Production Advisor" where artisans can ask questions and receive localized, translated responses (Hindi/English support).

---

## 4. System Architecture & Folder Structure

### Frontend Structure
```text
frontend/
├── public/                 # Static assets, images, icons
├── src/
│   ├── components/         # Reusable UI elements (DashboardLayout, Cards, Buttons)
│   ├── pages/              # Main route views (Home, Profile, Trends, ProductionAdvisor)
│   ├── App.jsx             # React Router configuration
│   ├── index.css           # Global typography, color variables, and utility classes
│   └── main.jsx            # React root mount point
```

### Backend Structure (Proposed)
```text
backend/
├── app/
│   ├── api/             # API Router definitions (endpoints like /auth, /products, /trends)
│   │   ├── dependencies.py # Reusable dependencies (e.g., get_db, current_user)
│   │   └── endpoints/   # Grouped API routes
│   ├── core/            # Application config, environment variables, security (JWT)
│   ├── crud/            # Create, Read, Update, Delete abstractions (DB operations)
│   ├── db/              # Database connection setup and session management
│   ├── models/          # SQLAlchemy Database Models
│   ├── schemas/         # Pydantic models (Data validation)
│   ├── ml/              # Machine Learning pipelines, model loading, caching wrappers
│   ├── services/        # Complex business logic tying CRUD and ML together
│   └── main.py          # FastAPI application entry point
├── requirements.txt     # Python dependencies
└── .env.example         # Example environment variables
```

---

## 5. Deployment Strategy (Proposed)
1. **Frontend**: Deployed as a static application on **Vercel** or **Netlify** for edge caching and fast global delivery.
2. **Backend**: Containerized using **Docker** and deployed on **Render**, **AWS ECS/EKS**, or **Google Cloud Run** to easily scale machine learning inference instances.
3. **Database**: Managed cloud database service (e.g., AWS RDS, Supabase, or MongoDB Atlas).
4. **CI/CD**: GitHub Actions to run automated testing, linting (ESLint, Flake8), and continuous deployment upon merges to the `main` branch.

---

## 6. Next Steps for the Team
- **Backend Scaffold**: Initialize the Python virtual environment, install FastAPI, and set up the `app/` structure.
- **Database Design**: Agree on database schemas for Artisans, Products, Orders, and Material Sources.
- **ML Mocking**: Build mock JSON endpoints for the ML services (Trends, Pricing) so the frontend team can continue development while the data team trains the models.
