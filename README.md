---
title: Ubuntuuu
emoji: 🐨
colorFrom: purple
colorTo: gray
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
---

# Agentic RAG AI Tutor

## Overview

**Agentic RAG AI Tutor** is an adaptive, conversational AI tutor that helps students understand complex topics by relating them to their personal interests and background knowledge. The system builds rapport, gathers the user's name and interests, and uses analogies and examples tailored to each student, making learning more engaging and effective.

## Features

- **Conversational AI Tutor:** Greets users, asks for their name and interests, and remembers them for the session.
- **Personalized Explanations:** Uses the user's hobbies, interests, or favorite subjects to create analogies for complex topics.
- **Rapport Building:** Maintains a friendly, supportive tone and checks in with the user to ensure understanding.
- **Dynamic Prompting:** Suggests topics, adapts to user uncertainty, and keeps the conversation engaging.
- **Powered by Gemini:** Utilizes Google's Gemini LLM for high-quality, research-backed explanations.
- **Modern UI:** Built with Gradio for an interactive chat experience.

## How It Works

1. **Start a Conversation:** The AI tutor greets you and asks for your name and interests.
2. **Ask Questions:** When you ask about a topic, the tutor explains it using analogies from your interests.
3. **Ongoing Engagement:** The tutor checks in, suggests topics, and adapts to your learning needs.

## Getting Started

### Prerequisites

- Python 3.9+
- Google Gemini API key

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/agentic_rag_ai.git
    cd agentic_rag_ai
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**
    - Create a `.env` file in the project root:
        ```
        GEMINI_API_KEY=your_google_gemini_api_key
        ```

### Running the App

```bash
python main.py
```

The Gradio interface will launch in your browser. You can also share the link with others.

## Project Structure

```
agentic_rag_ai/
│
├── app.py              # (Legacy) Multi-agent logic (optional)
├── main.py             # Main entry point with single-model conversational logic
├── state_schema.py     # (Legacy) State management (optional)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Customization

- **Prompt Engineering:** The system prompt in `main.py` can be modified to adjust the tutor's personality and behavior.
- **Model Selection:** Easily switch to other LLMs supported by LangChain if desired.

## License

MIT License

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain)
- [Gradio](https://gradio.app/)
- [Google Gemini](https://ai.google.dev/gemini-api/docs/)

---

*Enjoy learning with your personalized AI tutor!*
Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
