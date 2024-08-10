import telebot
import io
from itertools import product

# Ganti dengan token bot Telegram kamu
bot = telebot.TeleBot("7164344975:AAG-nEENAr77GV1tqTBGtwtIeBQIDgQvQUM")

def generate_combinations(word):
    """Generate all possible combinations of upper and lowercase letters in a word.

    Args:
        word: The input word.

    Returns:
        A list of all possible email combinations.
    """
    combinations = []
    for combination in product(*zip(word.lower(), word.upper())):
        combinations.append(''.join(combination) + '@gmail.com')
    return combinations

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Silakan kirimkan kata yang ingin diubah menjadi kombinasi email.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    word = message.text
    combinations = generate_combinations(word)

    # Buat file dalam memori
    file_name = f"{word}_combinations.txt"
    with io.BytesIO() as output:
        for combo in combinations:
            output.write(combo.encode('utf-8'))
            output.write(b'\n')

        # Kirim file dengan nama dan caption yang sama
        output.seek(0)
        bot.send_document(message.chat.id, output, caption=file_name, visible_file_name=file_name)

bot.polling()
