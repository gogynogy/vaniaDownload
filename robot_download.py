import hashlib
import os
import wget


def download_staf(folder, path):  # сама функция даунлоуда
    with open(folder) as file:  # открывает файл и читает его списком
        lines = [line.rstrip('\n') for line in file]
        for line in lines:
            folders = line.split(", ")  # готовый список для каждой загрузки 0 - имя файла, 1 - ссылка, 2 - хеш256
            try:  # пробует загрузить новый файл
                wget.download(folders[1], path)  # загрузка файла
                print(f"загрузка завершена {folders[0]}")
                with open(f"reclebin/{folders[0]}", "rb") as f:
                     bytesF = f.read()  # читает файл в байтах
                     readable_hash = hashlib.sha256(bytesF).hexdigest()  # получает хеш 256
                     if folders[2] == readable_hash:  # сравнивает хеш нового файла с историей
                         print("актуальный файл уже скачан")
                         os.remove(f'reclebin/{folders[0]}')  # удаляет загруженный файл, если он соответствует файлу в базе
                     else:
                         print(f"по ссылке {folders[1]} найден новый файл {wget.filename_from_url(folders[1])}")
                         folders[0] = wget.filename_from_url(folders[1])  # обновление имени загруженного файла
                         folders[2] = readable_hash  # обновление хеша
                         pass
            except:  # действие в случае не удавшейся загрузки файла
                print("ни каких шишек, пока не докуришь гашиш")


if not os.path.exists("reclebin"):
    os.mkdir("reclebin")  # создает пустую папку для временного сохранения файлов

folder = os.path.abspath(os.path.join("list_url.txt"))  # путь к базе
path = os.path.abspath(os.path.join("reclebin"))

download_staf(folder, path)
