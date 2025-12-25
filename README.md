🤖 Telegram Downloader Bot

Telegram Downloader Bot adalah bot Telegram berbasis Python yang berfungsi untuk mengunduh berbagai konten (file, media, dll) langsung dari Telegram dan menyimpannya ke server. Bot ini dibuat dengan fokus pada kemudahan penggunaan, performa stabil, dan struktur sederhana.

Project ini cocok dijalankan di Termux, VPS, Linux server, maupun environment Python lainnya.


---

📥 Cara Instalasi & Menjalankan Bot

Panduan berikut menjelaskan instalasi lengkap Telegram Downloader Bot di berbagai environment.


---

📱 Instalasi di Termux (Android)

1️⃣ Update Termux

pkg update && pkg upgrade

2️⃣ Install dependency dasar

pkg install git python ffmpeg nodejs -y

Cek versi:

python --version
node --version
ffmpeg -version


---

3️⃣ Clone repository bot

git clone https://github.com/FanxyzXD-II/TelegramDownloader-Bot.git

cd TelegramDownloader-Bot


---

4️⃣ Install Python library yang dibutuhkan

pip install -U yt-dlp
pip install python-telegram-bot

Jika ingin lebih rapi, buat requirements.txt:

yt-dlp
python-telegram-bot
requests

Lalu install:

pip install -r requirements.txt


---

5️⃣ Konfigurasi Bot Token

Edit file utama:

nano Converter0x.py

Masukkan BOT TOKEN Telegram kamu:

TOKEN = "ISI_TOKEN_BOT_KAMU"

⚠️ Jangan upload token ke GitHub.


---

6️⃣ Jalankan bot

python Converter0x.py

Bot akan langsung aktif dan siap digunakan.


---

💻 Instalasi di VPS / Linux (Ubuntu/Debian)

1️⃣ Update server

sudo apt update && sudo apt upgrade -y

2️⃣ Install dependency

sudo apt install git python3 python3-pip ffmpeg nodejs -y


---

3️⃣ Clone repository

git clone https://github.com/FanxyzXD-II/TelegramDownloader-Bot.git

cd TelegramDownloader-Bot


---

4️⃣ Install Python dependency

pip3 install -U yt-dlp
pip3 install python-telegram-bot


---

5️⃣ Jalankan bot

python3 Converter0x.py


---

🖥️ Instalasi di Windows

1️⃣ Install software pendukung

Python 3.x → https://www.python.org

Git → https://git-scm.com

FFmpeg → https://ffmpeg.org


Pastikan semua sudah masuk PATH.


---

2️⃣ Clone repository

git clone https://github.com/FanxyzXD-II/TelegramDownloader-Bot.git
cd TelegramDownloader-Bot


---

3️⃣ Install dependency

pip install -U yt-dlp
pip install python-telegram-bot


---

4️⃣ Jalankan bot

python Converter0x.py


---

🔁 Menjalankan Bot 24 Jam (Opsional)

Termux

nohup python Converter0x.py &

VPS (screen)

screen -S tgdownloader
python3 Converter0x.py

Keluar screen: CTRL + A + D


---

⚠️ Catatan Penting

❌ Jangan upload downloads/ ke GitHub

❌ Jangan upload BOT TOKEN

✅ Gunakan Python versi terbaru

✅ FFmpeg wajib untuk download video



---

⭐ Jika bot ini bermanfaat, jangan lupa beri Star di GitHub ⭐
📥 Cara Penggunaan

1. Start bot di Telegram


2. Kirim perintah / link sesuai fitur bot


3. Bot akan memproses dan mengunduh file


4. File tersimpan di folder downloads/




---

⚠️ Catatan Penting

❌ Jangan upload token bot ke repository publik

❌ Jangan upload folder downloads/ ke GitHub

✅ Gunakan Python versi terbaru

✅ Cocok dijalankan di server Linux / VPS



---

🛠️ Pengembangan

Jika ingin mengembangkan bot:

git checkout -b fitur-baru

Commit perubahan:

git add .
git commit -m "tambah fitur baru"
git push origin fitur-baru


---

📄 Lisensi

Project ini menggunakan lisensi MIT. Bebas digunakan dan dikembangkan dengan tetap mencantumkan kredit.


---

👤 Developer

Nama: FanxyzXD

GitHub: https://github.com/FanxyzXD-II



---

⭐ Jika repository ini bermanfaat, jangan lupa beri Star di GitHub ⭐
