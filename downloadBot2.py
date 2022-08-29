import hashlib, ssl, os, wget, threading, boto3, yaml #pip install pyyaml
ssl._create_default_https_context = ssl._create_unverified_context

import telebot
bot = telebot.TeleBot("5645949742:AAGDmze2SXINA1kqc4UJjAsSVVNaE9aDjik")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "грузим сиськи!")

id_gosha = 498332094

s3 = boto3.resource("s3")
folder = os.path.abspath(os.path.join("list_url.txt"))
path = os.path.abspath(os.path.join("fresh_soft"))
siski = os.path.abspath(os.path.join("siski"))

def download_staf(file, path):
    try:
        name, link, sha256summ = file["name"], file["link"], file["sha256summ"]
        print('3')
        wget.download(link, path)
        print('4')
        fileName = wget.filename_from_url(link)
        with open(f"{path}/{fileName}", "rb") as file:
            bytesFile = file.read()
            readable_hash = hashlib.sha256(bytesFile).hexdigest()
            if sha256summ != readable_hash:
                print("33")
                os.remove(f'{path}/{fileName}')
            else:
                print('1')
                gif = open('221928.gif', 'rb')
                bot.send_animation(id_gosha, gif)
                print("2")
                #
                # if name not in s3.buckets.all:
                #     s3.download_file(name)
    except:
        print("kosiakus")



if not os.path.exists("fresh_soft"):
    os.mkdir("fresh_soft")


def start():
    with open(folder) as f:
        templates = yaml.safe_load(f)
        for file in templates:
            download_staf(file, path)
            my_thread = threading.Thread(target=download_staf, args=(file, path))
            my_thread.start()


start()


bot.polling(none_stop = True)