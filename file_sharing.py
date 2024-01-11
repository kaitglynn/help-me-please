```python
import os
from tkinter import filedialog
from tkinter import messagebox

# Schema for shared files
class FileSchema:
    def __init__(self, name, type, size, path):
        self.name = name
        self.type = type
        self.size = size
        self.path = path

# Function to share files
def shareFile():
    filepath = filedialog.askopenfilename()
    if filepath:
        try:
            file_info = os.stat(filepath)
            file_name = os.path.basename(filepath)
            file_type = os.path.splitext(filepath)[1]
            file_size = file_info.st_size
            shared_file = FileSchema(file_name, file_type, file_size, filepath)
            # Here you can add the code to send the file to the bot or another user
            # For example, you can use a server or a cloud service API
            # sendFileToBot(shared_file)
            messagebox.showinfo("File Shared", "File has been shared successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Cancelled", "File sharing was cancelled")

# Function to preview file before sending
def previewFile():
    filepath = filedialog.askopenfilename()
    if filepath:
        try:
            file_info = os.stat(filepath)
            file_name = os.path.basename(filepath)
            file_type = os.path.splitext(filepath)[1]
            file_size = file_info.st_size
            preview_file = FileSchema(file_name, file_type, file_size, filepath)
            # Here you can add the code to preview the file
            # For example, you can open the file with the default program
            # os.startfile(preview_file.path)
            messagebox.showinfo("File Preview", "File is ready for preview!")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showinfo("Cancelled", "File preview was cancelled")
```