import qrcode
import hashlib
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

def get_uptime_milliseconds():
    return int(time.time() * 1000)

def generate_hash_from_uptime():
    uptime = get_uptime_milliseconds()
    return hashlib.sha256(str(uptime).encode()).hexdigest()

def generate_qr(data, filename='qrcode.png'):
    img = qrcode.make(data)
    img.save(filename)
    return filename
    
def get_token_from_file(filepath='token.txt'):
    with open(filepath, 'r') as file:
        token = file.read().strip()
    return token

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я могу сгенерировать QR-код на основе времени запуска ПК.")

async def generate_qr_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    hash_value = generate_hash_from_uptime()
    
    qr_filename = generate_qr(hash_value)
    
    with open(qr_filename, "rb") as qr_image:
        await update.message.reply_photo(qr_image, caption=f"Вот твой QR-код!\n")

async def main():
    token = get_token_from_file()

    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("generate_qr", generate_qr_code))

    await application.initialize()

    await application.start()
    await application.updater.start_polling()

    await asyncio.Future()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
