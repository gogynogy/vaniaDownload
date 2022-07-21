import hashlib
import os
import wget
import urllib.request

if not os.path.exists("reclebin"):
    os.mkdir("reclebin") #создает пустую папку для сохранения файлов

folder = os.path.abspath(os.path.join("list_url.txt"))
path = os.path.abspath(os.path.join("reclebin"))
file = open(folder, "r")
urls = file.readlines()
file.close()
folders = []
downloaded_files = []
def download_staf(): #сама функция даунлоуда
    for url in urls:
        print(file)
        wget.download(url, path)
        print(f"загрузка завершена {url}")

download_staf()