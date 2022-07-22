import hashlib
import os
import wget


def download_staf(folder, path):  # функция даунлоуда
    with open(folder) as file:  # открывает файл и читает его списком
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            folders = line.split(", ")  # готовый список для каждой загрузки 0 - имя файла, 1 - ссылка, 2 - хеш256
            try:  # пробует загрузить новый файл
                wget.download(folders[1], path)  # загрузка файла
                print(f"загрузка завершена {folders[1]}")
                fileName = wget.filename_from_url(folders[1])
                with open(f"reclebin/{fileName}", "rb") as f:
                     bytesFile = f.read()  # читает файл в байтах
                     readable_hash = hashlib.sha256(bytesFile).hexdigest()  # получает хеш 256
                     print(readable_hash)
                     if folders[2] == readable_hash:  # сравнивает хеш нового файла с историей
                         print("актуальный файл уже скачан")
                         os.remove(f'reclebin/{fileName}')
                         # удаляет загруженный файл, если он соответствует файлу в базе
                     else:
                         print(f"по ссылке {folders[1]} найден новый файл {wget.filename_from_url(folders[1])}")
                         # сюда нужно дописать выгрузку на aws
                         os.remove(f'reclebin/{fileName}')
            except:  # действие в случае не удавшейся загрузки файла
                print("ни каких шишек, пока не докуришь гашиш")


if not os.path.exists("reclebin"):
    os.mkdir("reclebin")  # создает пустую папку для временного сохранения файлов

folder = os.path.abspath(os.path.join("list_url.txt"))  # путь к базе
path = os.path.abspath(os.path.join("reclebin"))

download_staf(folder, path)
