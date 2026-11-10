import os

directory_path = "/storage/emulated/0"

try:
    contents = os.listdir(directory_path)

    for item in contents:
        print(item)

except OSError as e:
    print("Error:", e)