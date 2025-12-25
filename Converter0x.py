import os
import json
from datetime import datetime
from yt_dlp import YoutubeDL
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters
)
from telegram.request import HTTPXRequest

# ================= CONFIG =================
BOT_TOKEN = "token_bot"
DOWNLOAD_DIR = "downloads"
USER_DB = "users.json"

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

USER_LINK = {}
ACTIVE_USERS = set()
ALL_USERS = set()

# ================= LOAD & SAVE USER =================
def load_users():
    global ALL_USERS
    if os.path.exists(USER_DB):
        with open(USER_DB, "r") as f:
            ALL_USERS = set(json.load(f))
    else:
        ALL_USERS = set()

def save_users():
    with open(USER_DB, "w") as f:
        json.dump(list(ALL_USERS), f)

# ================= BANNER =================
def show_banner():
    os.system("clear")
    print("\033[1;36m")
    print("██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ ")
    print("██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
    print("██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝")
    print("██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗")
    print("██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║")
    print("╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print("\033[1;32m        MULTI DOWNLOADER TELEGRAM BOT")
    print(f"\033[1;33m        TOTAL USERS  : {len(ALL_USERS)}")
    print(f"\033[1;33m        ACTIVE USERS : {len(ACTIVE_USERS)}")
    print("\033[0m\n")

# ================= LOG =================
def log_chat(update, tag="CHAT", extra=""):
    user = update.effective_user

    ACTIVE_USERS.add(user.id)

    if user.id not in ALL_USERS:
        ALL_USERS.add(user.id)
        save_users()

    username = f"@{user.username}" if user.username else "NO_USERNAME"
    text = "-"
    if update.message and update.message.text:
        text = update.message.text

    time = datetime.now().strftime("%H:%M:%S")
    print(
        f"[{time}] [{tag}] {user.id} | {username} | {text} {extra} "
        f"| TOTAL: {len(ALL_USERS)} | ACTIVE: {len(ACTIVE_USERS)}"
    )

# ================= START =================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_chat(update, "START")
    await update.message.reply_text(
        """👋 Selamat datang di Multi-Downloader Bot! 🤖💎
Bingung mau download video tapi ada watermark-nya? Atau mau ambil audionya aja? Tenang, aku bisa bantu semua!

📌 Cara pakai:
Cukup tempel (paste) link video/audio di bawah.

Gratis, cepat, dan kualitas mantap! 🔥

Kirim link lalu pilih:
🎵 Audio atau 🎬 Video
Join Community:
https://t.me/tiktokvideodownloader_byBot"""
    )

# ================= RECEIVE LINK =================
async def receive_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    if not text.startswith("http"):
        return

    USER_LINK[update.effective_user.id] = text
    log_chat(update, "CHAT")

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🎵 Audio", callback_data="audio"),
            InlineKeyboardButton("🎬 Video", callback_data="video")
        ]
    ])

    await update.message.reply_text("Pilih format:", reply_markup=keyboard)

# ================= CHOICE =================
async def choose(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    log_chat(update, "CHOICE", query.data.upper())

    url = USER_LINK.get(query.from_user.id)
    if not url:
        await query.edit_message_text("❌ Link kadaluarsa.")
        return

    await query.edit_message_text("⏳ Memproses...")

    if query.data == "audio":
        await download_audio(query.from_user, url)
    else:
        await download_video(query.from_user, url)

# ================= AUDIO =================
async def download_audio(user, url):
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "quiet": True,
        "noplaylist": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "128",
        }],
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp3"

        with open(file, "rb") as f:
            await user.send_audio(audio=f, caption="✅ Audio siap diputar")

        os.remove(file)

    except Exception as e:
        print("[ERROR AUDIO]", e)
        await user.send_message("❌ Gagal mengunduh audio")

# ================= VIDEO =================
async def download_video(user, url):
    ydl_opts = {
        "format": "bv*[height<=720]+ba/best[height<=720]/best",
        "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
        "merge_output_format": "mp4",
        "quiet": True,
        "noplaylist": True,
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file = ydl.prepare_filename(info)

        try:
            await user.send_video(open(file, "rb"), supports_streaming=True,
                                  caption="✅ Video jernih + suara OK")
        except:
            await user.send_document(open(file, "rb"),
                                     caption="⚠️ Video dikirim sebagai file")

        os.remove(file)

    except Exception as e:
        print("[VIDEO ERROR]", e)
        await user.send_message("❌ Gagal mengunduh video")

# ================= MAIN =================
def main():
    load_users()
    show_banner()

    request = HTTPXRequest(connect_timeout=60, read_timeout=600, write_timeout=600)
    app = ApplicationBuilder().token(BOT_TOKEN).request(request).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, receive_link))
    app.add_handler(CallbackQueryHandler(choose))

    print("🤖 Bot aktif | By FanxyzXD With AI| LOGGING ON\n")
    app.run_polling()

if __name__ == "__main__":

    main()
