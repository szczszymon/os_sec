import os
import shutil
from itertools import count

device = "E:"
directory = "E:\\pliki"
size = 1024 ** 2

for i in range(3):
    os.makedirs(directory, exist_ok=True)
    free = shutil.disk_usage(device).free

    for i in count():
        if free-size >= size:
            with open(f"{directory}\\{i}.txt", "wb") as file:
                file.write(b'\x00' * size)
            free -= size
        else:
            break

    shutil.rmtree(directory)