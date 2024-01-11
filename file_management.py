```python
import os
import shutil

def create_directory(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        print(f"Directory {path} already exists.")

def delete_directory(path):
    try:
        shutil.rmtree(path)
    except FileNotFoundError:
        print(f"Directory {path} does not exist.")

def create_file(path):
    try:
        open(path, 'x').close()
    except FileExistsError:
        print(f"File {path} already exists.")

def delete_file(path):
    try:
        os.remove(path)
    except FileNotFoundError:
        print(f"File {path} does not exist.")

def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
    except FileNotFoundError:
        print(f"File {source_path} does not exist.")

def copy_file(source_path, destination_path):
    try:
        shutil.copy2(source_path, destination_path)
    except FileNotFoundError:
        print(f"File {source_path} does not exist.")

def rename_file(source_path, new_name):
    try:
        os.rename(source_path, new_name)
    except FileNotFoundError:
        print(f"File {source_path} does not exist.")
```