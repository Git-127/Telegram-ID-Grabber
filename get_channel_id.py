from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

BOT_TOKEN = "YOUR-TELEGRAM-BOT-TOKEN"

async def get_chat_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message

    if not message:
        return

    # Check if it's a forwarded message from a chat (like a channel)
    if hasattr(message, 'forward_from_chat') and message.forward_from_chat:
        chat = message.forward_from_chat
        await message.reply_text(f"✅ Channel forwarded:\n📛 Name: {chat.title}\n🆔 ID: {chat.id}\n🌀 Type: {chat.type}")
    else:
        # Fallback: show the ID of the current chat (user or group)
        chat = message.chat
        await message.reply_text(f"ℹ️ This message is from:\n📛 Name: {chat.title or chat.username or 'N/A'}\n🆔 ID: {chat.id}\n🌀 Type: {chat.type}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, get_chat_id))
    print("🤖 Bot is running — Forward a message from your channel to get its ID.")
    app.run_polling()

