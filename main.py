import os
import asyncio
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()
# Tokenlarni tekshirib oling
TELEGRAM_TOKEN = "8010808688:AAH1R4biIKotGmCU3vZ58-UkDtkI5__edP8"
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("Salom! Internet ulanishi tiklandi. Men tayyorman!")

@dp.message()
async def chat_handler(message: types.Message):
    try:
        await bot.send_chat_action(message.chat.id, "typing")
        response = model.generate_content(message.text)
        await message.answer(response.text)
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
        await message.answer("Hozircha javob bera olmayman, internetni tekshiring.")

async def main():
    print("🚀 Bot qayta ishga tushmoqda...")
    # Avvalgi eski xabarlarni o'chirib tashlaymiz (skip_updates)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot to'xtatildi.")