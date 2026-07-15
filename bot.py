from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

"8929946649:AAE-4vw4cHP7c051_BCSW1lvW1KTfFVFHWI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """🎉 Welcome!

I'm your Telegram group management bot.

Use /help to see my commands.

Let's keep our community safe and friendly! 😊"""
    )
    
    app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()