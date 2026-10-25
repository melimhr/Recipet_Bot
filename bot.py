import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

os.makedirs("photos", exist_ok=True)

async def start(update, context):
    await update.message.reply_text("سلام")

async def get_photo(update, context):
    caption = update.message.caption
    photo = update.message.photo[-1]
    file = await photo.get_file()
    await file.download_to_drive(f"photos/{photo.file_unique_id}.jpg")
    if caption:
        await update.message.reply_photo(photo=photo.file_id, caption=caption)

app = ApplicationBuilder().token("token").build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.PHOTO, get_photo))
app.run_polling()