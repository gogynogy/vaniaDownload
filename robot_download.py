import hashlib
import yaml #pip install pyyaml
import os
import wget
import threading
import boto3



def download_staf(file, path):
    name, link, sha256summ = file["name"], file["link"], file["sha256summ"]
    try:
        wget.download(link, path)
        fileName = wget.filename_from_url(link)
        with open(f"{path}/{fileName}", "rb") as file:
            bytesFile = file.read()
            readable_hash = hashlib.sha256(bytesFile).hexdigest()
            if sha256summ != readable_hash:
                os.remove(f'{path}/{fileName}')
            else:
                if name not in s3.buckets.all:
                    s3.download_file(name)
    except:
        pass


if not os.path.exists("fresh_soft"):
    os.mkdir("fresh_soft")

folder = os.path.abspath(os.path.join("list_url.txt"))
path = os.path.abspath(os.path.join("fresh_soft"))
s3 = boto3.resource("s3")

with open(folder) as f:
    templates = yaml.safe_load(f)
    for file in templates:
        my_thread = threading.Thread(target=download_staf, args=(file, path))
        my_thread.start()