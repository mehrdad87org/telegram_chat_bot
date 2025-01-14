# Telegram Llama Chatbot

This is a Python-based Telegram chatbot that integrates with the Llama model for generating responses. The bot allows users to interact with the Llama model, provides help and contact information, and includes features like quitting the chat and returning to the main menu.

## Features

- **Llama Integration**: Connects to a locally hosted Llama model for generating responses.
- **Telegram Bot**: Built using the `telebot` library to interact with users on Telegram.
- **Interactive Menu**: Provides buttons for easy navigation (e.g., About Us, Contact Us, Quit).
- **Error Handling**: Automatically reconnects if the bot encounters an error.

## Technologies Used

- **Python**: The core programming language used for the bot.
- **Telebot**: A Python wrapper for the Telegram Bot API.
- **Requests**: Used to send HTTP requests to the Llama model API.
- **Llama Model**: A locally hosted Llama model for generating responses.
- **You should write "ollama run llama3.2" in your command prompt.**
## Prerequisites

- **Telegram Bot Token**: Obtain a bot token from [BotFather](https://core.telegram.org/bots#botfather).
- **Llama Model**: Ensure the Llama model is running locally at `http://localhost:11434/api/generate`.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mehrdad87org/telegram_chat_bot.git
   cd telegram_chat_bot
   pip install -r requirements.txt
   python bot.py
