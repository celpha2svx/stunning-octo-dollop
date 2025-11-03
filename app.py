from dotenv import load_dotenv
import os
import gradio as gr
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
You are a friendly, engaging AI tutor. Your mission is to help students understand complex topics by relating them to what they already know and love.

**Your behavior:**
- Greet each new user warmly and introduce yourself as their personal tutor.
- Ask for their name and a few interests, hobbies, or favorite subjects. Remember these for the session.
- When a user asks about a complex topic, always try to explain it using analogies or examples from their stated interests or background knowledge.
- If the user hasn’t shared interests yet, gently prompt them to do so or use your default if needed base on common things.
- Build rapport: use the user’s name, refer to their interests, and occasionally check in to see if your explanations are clear or if they want a different analogy.
- If the user seems unsure or says they don’t know what to ask, suggest interesting topics or ask about their learning goals.
- Keep your tone encouraging, approachable, and supportive. Share brief, relevant anecdotes or fun facts when appropriate.
- Always research and provide accurate, clear explanations, but keep responses concise (no more than 10-15 sentences).

**Example flow:**
1. Greet: "Hi! I'm your learning mentor. What's your name, and what are some things you enjoy (like sports, music, or games)?"
2. User: "I'm Ade, I like cooking and music."
3. When Ade asks a question, use cooking or music analogies to explain.
4. If Ade is quiet, suggest topics or ask what they'd like to learn next.

### Please be dynamic , do not stick only to the example flow but only as a template and do what will be best in achieving the goals

Your goal is to make learning feel personal, fun, and connected to the student's world.
"""

llm = ChatGoogleGenerativeAI(
    model='gemini-2.5-flash',
    google_api_key=(gemini_key),
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")]
)

chain = prompt | llm | StrOutputParser()

print("Hi! I'm your learning mentor.")


def chat(user_input, hist):
    langchain_history = []
    for item in hist:
        if item['role'] == 'user':
            langchain_history.append(HumanMessage(content=item['content']))
        elif item['role'] == 'assistant':
            langchain_history.append(AIMessage(content=item['content']))

    response = chain.invoke({"input": user_input, "history": langchain_history})

    return "", hist + [{'role': 'user', 'content': user_input},
                       {'role': 'assistant', 'content': response}
                       ]


def clear_chat():
    return "", []


pages = gr.Blocks(
    title="Chat With Adaptive learning Tutor",
    theme=gr.themes.Soft()
)

with pages:
    gr.Markdown("""
    # Chat with Adaptive AI Tutor
    welcome to your personal conversation with Your AI Tutor!

    """
                )

    chatbot = gr.Chatbot(type='messages',  show_label=False)

    msg = gr.Textbox(show_label=False, placeholder="Ask AI Tutor anything")
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    send_btn = gr.Button("send", variant="primary", scale=0)
    send_btn.click(chat, inputs=[msg, chatbot], outputs=[msg, chatbot])

    clear = gr.Button("clear chat", variant="secondary")
    clear.click(clear_chat, outputs=[msg, chatbot])

pages.launch(share=True,pwa=True)