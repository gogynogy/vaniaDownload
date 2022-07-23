import hashlib
import yaml #pip install pyyaml
import os
import wget
import threading


def download_staf(file, path):  # функция даунлоуда
    name, link, sha256summ = file["name"], file["link"], file["sha256summ"]  # получаем имя, ссылку хеш256 файла
    try:  # пробует загрузить новый файл
        print(f"начинается загузка с {link}")
        wget.download(link, path)  # загрузка файла
        print(f"загрузка {name} завершена")
        fileName = wget.filename_from_url(link)
        with open(f"reclebin/{fileName}", "rb") as f:
            bytesFile = f.read()  # читает файл в байтах
            readable_hash = hashlib.sha256(bytesFile).hexdigest()  # получает хеш 256
            if sha256summ == readable_hash:  # сравнивает хеш нового файла с историей
                print("актуальный файл уже скачан")
            else:
                print(f"по ссылке {link} найден новый файл {wget.filename_from_url(link)}")
                if input("загрузить новый файл на aws? y/n ").lower() == "y":
                    pass  # сюда нужно дописать выгрузку на aws
            os.remove(f'reclebin/{fileName}')  # удаляет загруженный файл
    except:  # действие в случае не удавшейся загрузки файла
        print(f"по ссылке: {link} файла не обнаружено")


if not os.path.exists("reclebin"):
    os.mkdir("reclebin")  # создает пустую папку для временного сохранения файлов

folder = os.path.abspath(os.path.join("list_url.txt"))  # путь к базе
path = os.path.abspath(os.path.join("reclebin"))
with ThreadPoolExecutor(max_workers=4) as executor:
with open(folder) as f:
    templates = yaml.safe_load(f)  # получает словарь списков из файла list_url.txt
    for file in templates:  # идем по спискам в словаре
        my_thread = threading.Thread(target=download_staf, args=(file, path))
        my_thread.start()  # запускаем потоками функцию загрузки