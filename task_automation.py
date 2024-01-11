```python
import os
import shutil
import time

class TaskAutomation:
    def __init__(self):
        pass

    def move_file(self, source, destination):
        try:
            shutil.move(source, destination)
            return True
        except Exception as e:
            print(f"Error occurred while moving file: {e}")
            return False

    def rename_file(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            return True
        except Exception as e:
            print(f"Error occurred while renaming file: {e}")
            return False

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            return True
        except Exception as e:
            print(f"Error occurred while deleting file: {e}")
            return False

    def create_directory(self, dir_path):
        try:
            os.makedirs(dir_path, exist_ok=True)
            return True
        except Exception as e:
            print(f"Error occurred while creating directory: {e}")
            return False

    def schedule_task(self, task, delay):
        try:
            time.sleep(delay)
            task()
            return True
        except Exception as e:
            print(f"Error occurred while scheduling task: {e}")
            return False
```