import schedule
import time
import os
import wget

folder = os.path.abspath(os.path.join("list_url.txt"))
path = os.path.abspath(os.path.join("reclebin"))
file = open(folder, "r")
urls = file.readlines()
file.close()
def download_staf(url, path): #сама функция даунлоада
    for url in urls:
        if url in path:
            print("файл уже скачан")
        else:
            wget.download(url, path)
            print(f"загрузка завершена {url}")


url = "https://www.python.org/ftp/python/3.8.9/python-3.8.9-amd64.exe"

# schedule.every(7).day.at("16:20").do(download_staf, url, path) #вызывает функцию загрузки раз в неделю
schedule.every(1).second.do(download_staf, url, path)

while True:
    schedule.run_pending()
    time.sleep(1)