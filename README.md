# ⚡ AI Workspace Assistant

A full-stack, production-ready AI Chat Application built with a modern **React (Vite)** frontend and a high-performance **FastAPI (Python)** backend. Designed as a monorepo, the application features an aesthetically polished dark-mode interface with neon accents, smooth scrolling, typing indicators, and robust cross-origin support.

---

## 🌐 Live Demos

* **Frontend App (Vercel):** [https://your-app-name.vercel.app](https://ai-chat-application-frontend-iota.vercel.app/)
* **Backend API (Render):** [https://ai-chat-application-backend-aruf.onrender.com](https://ai-chat-application-backend-aruf.onrender.com)
* **API Documentation:** [https://ai-chat-application-backend-aruf.onrender.com/docs](https://ai-chat-application-backend-aruf.onrender.com/docs) *(Interactive FastAPI Swagger UI)*

---

## ✨ Features

* **🎨 Modern UI/UX:** Dark-mode design with electric blue/purple neon highlights, clean typography, and interactive input states.
* **⚡ High Performance:** Ultra-fast frontend powered by Vite and lightweight asynchronous backend built with FastAPI & Uvicorn.
* **🔄 CORS Configured:** Fully integrated cross-origin resource sharing configured for seamless communication between Vercel and Render.
* **📦 Monorepo Architecture:** Clean, maintainable structure housing both `frontend/` and `backend/` in a single repository.
* **🛡️ Fallback & Error Handling:** Graceful message parsing for API key variables and state updates.

---

## 🛠️ Tech Stack

### Frontend
* **Framework:** React.js (Bootstrapped with [Vite](https://vitejs.dev/))
* **Styling:** Custom CSS3 with CSS variables for dark theme & glassmorphism effects
* **HTTP Client:** Native Javascript `fetch` API

### Backend
* **Framework:** FastAPI (Python 3.11)
* **Server:** Uvicorn ASGI
* **Validation:** Pydantic models
* **Middlewares:** Starlette CORSMiddleware

### Hosting & Infrastructure
* **Frontend Hosting:** [Vercel](https://vercel.com/)
* **Backend Hosting:** [Render](https://render.com/) (Web Service)
* **Version Control:** Git & GitHub

---

## 📂 Directory Structure

```text
AI_Chat_Project/
├── backend/
│   ├── main.py                # FastAPI endpoints & CORS configuration
│   ├── requirements.txt       # Python dependencies (fastapi, uvicorn, pydantic, etc.)
│   └── .gitignore
├── frontend/
│   ├── src/
│   │   ├── App.jsx            # Main React chat component
│   │   ├── App.css            # Dark mode styling & layout
│   │   └── main.jsx
│   ├── package.json           # Node dependencies & scripts
│   └── vite.config.js
├── .gitignore                 # Root gitignore for monorepo tracking
└── README.md                  # Project documentation
