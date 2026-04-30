# 🤖 Telegram ID Grabber

A simple Telegram bot that helps you quickly discover **Chat IDs**, **Channel IDs**, **Group IDs**, or **User IDs**.

Perfect for developers who need Telegram IDs for bots, automation systems, or integrations.

---

## Features

* ✅ Detect Telegram **Channel ID**
* ✅ Detect **Group Chat ID**
* ✅ Detect **User Chat ID**
* ✅ Works using forwarded messages
* ✅ Beginner-friendly setup
* ✅ Lightweight single-file bot

---

## How It Works

1. Start the bot.
2. Forward a message **from your Telegram channel** to the bot.
3. The bot instantly returns:

   * Chat name
   * Chat ID
   * Chat type

If no message is forwarded, the bot shows the current chat ID instead.

---

## 📁 Project Structure

```bash
chat-id-grabber/
│
├── main.py
└── README.md
```

---

## 1. Requirements

* Python 3.9+
* Telegram Bot Token

---

## 2. Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/telegram-chat-id-finder.git
cd telegram-chat-id-finder
```

Install dependency:

```bash
pip install python-telegram-bot
```

---

## 3. Configuration

Open **main.py** and add your bot token:

```python
BOT_TOKEN = "YOUR-TELEGRAM-BOT-TOKEN"
```

### 4. Getting a Bot Token

1. Open Telegram
2. Search **@BotFather**
3. Create a new bot
4. Copy the token provided

---

## 5. Running the Bot

```bash
python main.py
```

Console output:

```bash
🤖 Bot is running — Forward a message from your channel to get its ID.
```

---

## How to Get a Channel ID

1. Add your bot as **Admin** in your Telegram channel.
2. Send any message in the channel.
3. Forward that message to the bot.
4. The bot replies with:

```bash
✅ Channel forwarded:
📛 Name: My Channel
🆔 ID: -100XXXXXXXXXX
🌀 Type: channel
```

---

## Use Cases

* Telegram automation bots
* Channel posting bots
* Notification systems
* Trading signal bots
* Backend integrations

---

## Tech Stack

* Python
* python-telegram-bot
* AsyncIO

---

## Contributing

Contributions are welcome!

1. Fork the repository
2. Create a branch
3. Submit a Pull Request

---

## License

MIT License — free to use and modify.

---

## ⭐ Support

If this tool saved you time, consider giving the repository a ⭐ on GitHub!
