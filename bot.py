name: LBank Scanner Bot

on:
  workflow_dispatch:

jobs:
  run-bot:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - run: pip install -r requirements.txt

      - run: python bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN =8431896631:AAH8ai8Jg6B5VoNFVuJXEvP32jzrw9oWAdw

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ ربات فعال شد.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
