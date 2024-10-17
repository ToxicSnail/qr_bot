## QR Code Generator Telegram Bot

This project is a Telegram bot that generates QR codes based on the system's uptime in milliseconds, hashes the uptime using SHA-256, and then creates a QR code from the resulting hash.

## Features

- Generates a QR code based on the time the system has been running.
- Uses SHA-256 hash of the system uptime to create unique QR codes.
- Sends the generated QR code to the user via Telegram.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/qr-code-telegram-bot.git
   cd qr-code-telegram-bot
2. **Set up a virtual environment (optional but recommended)**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows, use venv\Scripts\activate
```
3. **Install the required dependencies**:
  ```bash
  pip install -r requirements.txt
```
4. Create a `token.txt` file in the root directory of the project and add your Telegram bot token in it:
  ``"YOUR_TELEGRAM_BOT_TOKEN"``
