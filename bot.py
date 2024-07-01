from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,WebAppInfo

app = Client("my_bot", api_id="4626556", api_hash="e692aee631de6d8f42d6fe5792810885", bot_token="5052128609:AAGNjLmDrC3u7AFAO7_6DBUiGZxRJieZI3M")
secret_key = "Mohammad"  # یک کلید مخفی برای امضا کردن JWT
webapp_site = "https://mohammadm938.github.io/simple_webapp/"



@app.on_message(filters.command("start"))
def start(client, message):
    payload = {
        "user_id": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name
    }

    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Open Web App", web_app=WebAppInfo(url=webapp_site))]
        ]
    )

    message.reply(
        "Hello! Click the button below to open the web app.",
        reply_markup=keyboard
    )

app.run()