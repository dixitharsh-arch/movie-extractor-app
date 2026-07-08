# 🎬 Movie Information Extractor

A Streamlit app that extracts **structured, machine-readable movie data** — not free-form human text — from a plain-text paragraph description, using an LLM (Groq's `llama-3.3-70b-versatile`) via LangChain.

## Why structured output matters

Unlike a typical chatbot response that returns a paragraph of human-readable text, this app is built to return **strict JSON output** validated against a fixed schema (via Pydantic). That means the output isn't just something a person reads — it's something a **system can consume directly**:

- Feed straight into a database, API, or data pipeline with no manual parsing
- Guaranteed consistent field names and types on every request (e.g. `release_year` is always an `int` or `None`, `genre` is always a `list`, never missing or reworded)
- Safe for downstream automation — companies can plug this into a movie cataloging system, recommendation engine, content management tool, or internal dataset builder without writing custom text-parsing logic
- No "guessing" required to extract a value from prose — every field is a predictable JSON key

## Features

- Paste any paragraph describing a movie
- Extracts structured data using a Pydantic schema:
  - Title
  - Release Year
  - Genre(s)
  - Director
  - Cast
  - Rating
  - Summary
- Uses LangChain's `PydanticOutputParser` to enforce the LLM's output into this exact schema — the model cannot return arbitrary prose, only valid structured JSON
- Displays the result as clean, formatted JSON in the UI — ready to copy, log, or pass to another system

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI
- [LangChain](https://www.langchain.com/) — prompt orchestration
- [Groq](https://groq.com/) — LLM inference (`llama-3.3-70b-versatile`)
- [Pydantic](https://docs.pydantic.dev/) — structured output schema

## Setup (local)

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your-groq-api-key
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment

This app is deployed on [Streamlit Community Cloud](https://share.streamlit.io/). The `GROQ_API_KEY` is set as a secret in the app's settings rather than a local `.env` file.

## License

This project is for personal/educational use.
