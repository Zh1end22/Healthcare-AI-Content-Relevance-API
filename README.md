# Healthcare AI Content Relevance Service

This project provides an AI-powered API service that analyzes healthcare-related content—such as articles, blog posts, or research summaries—and returns:

- A relevance score indicating how closely the content relates to healthcare AI
- An alignment score measuring how well the article fits specific client interest areas (e.g. workflow optimization, physician experience)
- A categorized theme label based on predefined strategic focus areas
- A brief rationale explaining why the content may be valuable or insightful from a healthcare AI perspective

The service uses Google's Gemini model (via a managed API) to understand the context of each article and generate actionable metadata.

You simply POST raw article content, and receive a JSON response with scoring, theme classification, and summary insight.

## Who It's For

This tool is designed for:

- Healthcare AI consultants and analysts seeking automated insight extraction from large volumes of industry content
- Health IT and digital health companies wanting to monitor articles that align with their products and market strategy
- Innovation teams in healthcare organizations looking to track content that supports clinical decision-making, patient engagement, or operational efficiency
- Marketing and content teams needing help curating thought-leadership topics that resonate with client pain points and strategic goals

It streamlines how teams discover, prioritize, and respond to relevant content in the fast-moving healthcare AI landscape.

## Features

- Relevance scoring using Gemini API
- Categorization into predefined healthcare AI themes
- Alignment scoring based on client-defined focus areas
- Smart rationale generation for each article
- JSON API with a single POST endpoint
- FastAPI-powered backend with built-in Swagger docs

---

## Tech Stack

| Tool            | Purpose                                         |
|-----------------|-------------------------------------------------|
|  Python       | Backend language                                 |
|  FastAPI      | Web framework (for API)                          |
|  Gemini API   | AI engine (via Google Generative Language API)   |
|  httpx        | Async HTTP client to call Gemini API             |
|  dotenv       | Manage API keys via .env                         |
| Thunder Client | API testing directly inside VS Code             |

---
## API Reference

This service exposes a single endpoint via a FastAPI backend. It uses Google’s Gemini API to analyze healthcare-related article content and returns structured relevance scoring, categorization, and rationale.

-  Framework: FastAPI (Python)
-  AI Engine: Gemini API (via Google Generative Language API)
-  Recommended testing tools: Thunder Client (VS Code), Postman, curl, or FastAPI Swagger UI

---

### POST /analyze

Analyze a healthcare article for its relevance to AI in healthcare and alignment with client-specific interests.

- URL: `/analyze`
- Method: `POST`
- Content-Type: `application/json`
- Authentication: None (for local use)

#### Request Body

    json {"content": "Paste the full text of your article here..."}
## Running Locally (Step-by-Step Guide)

This guide walks you through setting up the Healthcare AI Content Relevance Scoring API on your local machine using FastAPI and Gemini (Google Generative Language API).

---

### Steps to Use the Project

### Clone the repo
git clone https://github.com/Zh1end22/Healthcare-AI-Content-Relevance-API.git
cd healthcare-ai-content-api

### Create virtual environment
python3 -m venv venv
source venv/bin/activate

### Install dependencies
pip install fastapi uvicorn httpx python-dotenv

### Create .env file with your Gemini API key
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env

### Start the FastAPI server
uvicorn main:app --reload
## Screenshot(s)

Thunder Client Test:![App Screenshot](https://i.imgur.com/VY6hzqk.png)


