import os
from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
bot_token = os.getenv('BOT_TOKEN')

# Inisialisasi bot dengan token
bot = telebot.TeleBot(token=bot_token)

# Menangani perintah '/start' dari pengguna
@bot.message_handler(commands=['start'])
def handle_start(message):
    reply_message = 'Halo! Selamat datang di bot Telegram Gunadarma 2022/2023.\n' \
    'Ketik /help untuk bantuan lebih lanjut.'
    markup = types.InlineKeyboardMarkup()

    # Membuat tombol inline untuk tautan eksternal
    btn_baak = types.InlineKeyboardButton("BAAK", url="https://baak.gunadarma.ac.id/")
    btn_student = types.InlineKeyboardButton("Student Site", url="https://student.gunadarma.ac.id/")
    btn_vclass = types.InlineKeyboardButton("VClass", url="https://v-class.gunadarma.ac.id/")

    # Menambahkan tombol-tombol ke dalam markup
    markup.add(btn_baak)
    markup.add(btn_student)
    markup.add(btn_vclass)

    # Mengirim pesan bantuan dengan markup
    bot.send_message(message.chat.id, reply_message, parse_mode="HTML", reply_markup=markup)

# Menangani perintah '/ug' dari pengguna
@bot.message_handler(commands=['ug'])
def handle_ug(message):
    reply_message = 'Website Official Gunadarma: \nhttps://gunadarma.ac.id/'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/baak' dari pengguna
@bot.message_handler(commands=['baak'])
def handle_baak(message):
    reply_message = 'Website baak: \nhttps://baak.gunadarma.ac.id/'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/vclass' dari pengguna
@bot.message_handler(commands=['vclass'])
def handle_vclass(message):
    reply_message = 'Website Vclass: \nhttps://v-class.gunadarma.ac.id/'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/jadkul' dari pengguna
@bot.message_handler(commands=['jadkul'])
def handle_jadkul(message):
    reply_message = 'jadwal kuliah: \nhttps://baak.gunadarma.ac.id/jadwal/cariJadKul'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/walas' dari pengguna
@bot.message_handler(commands=['walas'])
def handle_walas(message):
    reply_message = 'Dosen Wali Kelas: \nhttps://baak.gunadarma.ac.id/kuliahUjian/3/1#undefined3'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/watkul' dari pengguna
@bot.message_handler(commands=['watkul'])
def handle_watkul(message):
    reply_message = 'Waktu Kuliah: \nhttps://baak.gunadarma.ac.id/kuliahUjian/6#undefined6'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/student' dari pengguna
@bot.message_handler(commands=['student'])
def handle_student(message):
    reply_message = 'Student Site: \nhttps://studentsite.gunadarma.ac.id/'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/library' dari pengguna
@bot.message_handler(commands=['library'])
def handle_library(message):
    reply_message = 'Waktu Kuliah: \nhttps://library.gunadarma.ac.id/'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/lepkom' dari pengguna
@bot.message_handler(commands=['lepkom'])
def handle_lepkom(message):
    reply_message = 'LepKom: \nhttps://kursusvmlepkom.gunadarma.ac.id/'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/tv' dari pengguna
@bot.message_handler(commands=['tv'])
def handle_tv(message):
    reply_message = 'UGTV: \nhttps://ugtv.co.id/live-streaming-new/'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/linktr' dari pengguna
@bot.message_handler(commands=['tv'])
def handle_linktr(message):
    reply_message = 'UGTV: \nhttps://linktr.ee/univgunadarma'
    bot.send_message(message.chat.id, reply_message)   

# Menangani perintah '/ig' dari pengguna
@bot.message_handler(commands=['ig'])
def handle_ig(message):
    reply_message = 'Instagram: \nhttps://instagram.com/gunadarma?igshid=MmU2YjMzNjRlOQ=='
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/fb' dari pengguna
@bot.message_handler(commands=['fb'])
def handle_fb(message):
    reply_message = 'Facebook: \nhttps://www.facebook.com/gunadarma'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/mail' dari pengguna
@bot.message_handler(commands=['mail'])
def handle_mail(message):
    reply_message = 'E-mail: mediacenter@gunadarma.ac.id'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/tw' dari pengguna
@bot.message_handler(commands=['tw'])
def handle_tw(message):
    reply_message = 'Twitter: \nhttps://twitter.com/gunadarma_'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/tt' dari pengguna
@bot.message_handler(commands=['tt'])
def handle_tt(message):
    reply_message = 'TikTok: \nhttps://www.tiktok.com/@univgunadarma'
    bot.send_message(message.chat.id, reply_message)

    # Menangani perintah '/tt' dari pengguna
@bot.message_handler(commands=['yt'])
def handle_yt(message):
    reply_message = 'Youtube: \nhttps://www.youtube.com/c/ugtvofficial'
    bot.send_message(message.chat.id, reply_message)

# Menangani perintah '/boost' dari pengguna
@bot.message_handler(commands=['boost'])
def handle_boost(message):
    reply_message = 'Mode Mudah bot Telegram Gunadarma'
    markup = types.InlineKeyboardMarkup()

    # Membuat tombol inline untuk tautan eksternal
    btn_baak = types.InlineKeyboardButton("BAAK", url="https://baak.gunadarma.ac.id/")
    btn_student = types.InlineKeyboardButton("Student Site", url="https://student.gunadarma.ac.id/")
    btn_ug = types.InlineKeyboardButton("Gunadarma", url="https://student.gunadarma.ac.id/")
    btn_vclass = types.InlineKeyboardButton("VClass", url="https://v-class.gunadarma.ac.id/")
    btn_jadkul = types.InlineKeyboardButton("Jadwal Kuliah", url="https://baak.gunadarma.ac.id/jadwal/cariJadKul")
    btn_walas = types.InlineKeyboardButton("Daftar Wali Kelas", url="https://baak.gunadarma.ac.id/kuliahUjian/3/1#undefined3")
    btn_watkul = types.InlineKeyboardButton("Jam Waktu Kuliah", url="https://baak.gunadarma.ac.id/kuliahUjian/6#undefined6")
    btn_library = types.InlineKeyboardButton("Library", url="https://library.gunadarma.ac.id/")
    btn_lepkom = types.InlineKeyboardButton("Lepkom", url="https://kursusvmlepkom.gunadarma.ac.id/")
    btn_tv = types.InlineKeyboardButton("UGTV", url="https://ugtv.co.id/live-streaming-new/")
    btn_linktr = types.InlineKeyboardButton("LinkTree", url="https://linktr.ee/univgunadarma")
    btn_ig = types.InlineKeyboardButton("Instagram", url="https://instagram.com/gunadarma?igshid=MmU2YjMzNjRlOQ==")
    btn_fb = types.InlineKeyboardButton("Facebook", url="https://www.facebook.com/gunadarma")
    btn_email = types.InlineKeyboardButton("Email", url="mediacenter@gunadarma.ac.id")
    btn_tw = types.InlineKeyboardButton("Twitter", url="https://twitter.com/gunadarma_")
    btn_tt = types.InlineKeyboardButton("TikTok", url="https://www.tiktok.com/@univgunadarma")
    btn_yt = types.InlineKeyboardButton("Youtube", url="https://www.youtube.com/c/ugtvofficial")

    # Menambahkan tombol-tombol ke dalam markup
    markup.add(btn_baak)
    markup.add(btn_student)
    markup.add(btn_vclass)
    markup.add(btn_ug)
    markup.add(btn_jadkul)
    markup.add(btn_walas)
    markup.add(btn_watkul)
    markup.add(btn_library)
    markup.add(btn_lepkom)
    markup.add(btn_tv)
    markup.add(btn_linktr)
    markup.add(btn_ig)
    markup.add(btn_fb)
    markup.add(btn_tw)
    markup.add(btn_tt)
    markup.add(btn_email)
    markup.add(btn_yt)

    # Mengirim pesan bantuan dengan markup
    bot.send_message(message.chat.id, reply_message, parse_mode="HTML", reply_markup=markup)

# Menangani perintah '/help' dari pengguna
@bot.message_handler(commands=['help'])
def handle_help(message):
    reply_message = "<b>BOT TELEGRAM GUNADARMA</b>\n\n" \
    "Anda bisa menggunakan perintah-perintah berikut:\n\n" \
    "=========== PERINTAH ============\n" \
    "/start - Memulai bot Telegram Gunadarma\n" \
    "/help - Menampilkan bantuan\n" \
    "/boost - Menampilkan semua perintah dengan button\n" \
    "=================================\n\n" \
    "=========== AKADEMIK ============\n" \
    "/ug = Website Gunadarma\n" \
    "/baak - Website BAAK Gunadarma\n" \
    "/vclass - Website virtual class\n" \
    "/jadkul - Mencari Jadwal Kuliah\n" \
    "/walas - Mencari Daftar Wali Kelas\n" \
    "/watkul - Mengetahui Jam Waktu Kuliah\n" \
    "/student - Website Mahasiswa\n" \
    "/library - Perpustakaan Gunadarma\n" \
    "/lepkom - LepKom Gunadarma\n" \
    "/tv - Website UGTV\n" \
    "/linktr - Linktree Gundarma\n" \
    "=================================\n\n" \
    "============ SOSMED =============\n" \
    "/ig - Akun Instagram Gunadarma\n" \
    "/fb - Akun Facebook Gundarma\n" \
    "/mail - Akun Email Gunadarma\n" \
    "/tw - Akun Twitter Gundarma\n" \
    "/tt - Akun TikTok Gundarma\n" \
    "/yt - Akun Youttube Gundarma\n" \
    "=================================\n\n"
    bot.send_message(message.chat.id, reply_message, parse_mode="HTML")

# Menangani pesan teks dari pengguna
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    bot.reply_to(message, 'Maaf pesan "' + message.text + '" tidak terdapat dalam perintah bot Telegram Gunadarma 2022/2023')

# Menjalankan bot
bot.polling()
