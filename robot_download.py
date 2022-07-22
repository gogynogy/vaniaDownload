import hashlib
import yaml #pip install pyyaml
import os
import wget


def download_staf(folder, path):  # функция даунлоуда
    with open('list_url.txt') as f:
        templates = yaml.safe_load(f)  # получает словарь списков из файла list_url.txt
        for file in templates:  # идем по спискам в словаре
            name = file["name"]  # получаем имя файла
            link = file["link"]  # получаем ссылку файла
            sha256summ = file["sha256summ"]  # получаем хеш256 файла
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
                        os.remove(f'reclebin/{fileName}')  # удаляет загруженный файл
                    else:
                        print(f"по ссылке {link} найден новый файл {wget.filename_from_url(link)}")
                        if input("загрузить новый файл на aws? y/n").lower() == "y":
                            pass  # сюда нужно дописать выгрузку на aws
                        os.remove(f'reclebin/{fileName}')  # удаляет загруженный файл
            except:  # действие в случае не удавшейся загрузки файла
                print(f"по ссылке: {link} файла не обнаружено")


if not os.path.exists("reclebin"):
    os.mkdir("reclebin")  # создает пустую папку для временного сохранения файлов

folder = os.path.abspath(os.path.join("list_url.txt"))  # путь к базе
path = os.path.abspath(os.path.join("reclebin"))

download_staf(folder, path)
