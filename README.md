# AI FAQ Chatbot

An AI-powered chatbot that answers user questions using LLMs.  
Built with FastAPI, Groq Llama 3, Redis session memory, and a Streamlit chat interface.

## Features

- FastAPI backend API
- LLM responses using Groq (Llama 3)
- Session-based conversation memory using Redis
- Interactive chat UI built with Streamlit
- Streaming responses (ChatGPT-like typing effect)

## Tech Stack

- FastAPI
- Groq API
- Llama 3
- Redis
- Streamlit
- Python

## Project Architecture

User → Streamlit UI → FastAPI Backend → Groq Llama3 → Redis Memory

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/ai-faq-chatbot.git
cd ai-faq-chatbot
