import hashlib
import os
import wget
import urllib.request

if not os.path.exists("reclebin"):
    os.mkdir("reclebin") #создает пустую папку для сохранения файлов

folder = os.path.abspath(os.path.join("list_url.txt"))#путь к базе
path = os.path.abspath(os.path.join("reclebin"))

def download_staf(): #сама функция даунлоуда
    with open("list_url.txt") as file:#открывает файл и чмтает его списком
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            folders = line.split(", ")#готовый список для каждой загрузки 0 - имя файла, 1 - ссылка, 2 - хеш256
            wget.download(folders[1], path)#загрузка файла
            print(f"загрузка завершена {folders[0]}")
            with open(f"reclebin/{folders[0]}", "rb") as f:
                 bytes = f.read() # читает файл в байтах
                 readable_hash = hashlib.sha256(bytes).hexdigest()#получает хеш 256
                 if folders[2] == readable_hash:#сравнивает хеш нового файла с историей
                     print("актуальный файл уже скачан")
                     os.remove(f'reclebin/{folders[0]}')
                 else:
                     folders[0] = wget.filename_from_url(folders[1])  # обновление имени загруженного файла
                     pass


download_staf()

