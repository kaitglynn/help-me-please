```python
import dropbox
from google.cloud import storage

# Dropbox API
class DropboxIntegration:
    def __init__(self, access_token):
        self.dbx = dropbox.Dropbox(access_token)

    def upload_file(self, file_path, destination_path):
        with open(file_path, 'rb') as f:
            self.dbx.files_upload(f.read(), destination_path)

    def download_file(self, file_path, destination_path):
        self.dbx.files_download_to_file(destination_path, file_path)

# Google Drive API
class GoogleDriveIntegration:
    def __init__(self, bucket_name):
        self.storage_client = storage.Client()
        self.bucket = self.storage_client.bucket(bucket_name)

    def upload_file(self, source_file_name, destination_blob_name):
        blob = self.bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)

    def download_file(self, source_blob_name, destination_file_name):
        blob = self.bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

# Usage
# dbx = DropboxIntegration('YOUR_ACCESS_TOKEN')
# dbx.upload_file('local_file.txt', '/dropbox_file.txt')
# dbx.download_file('/dropbox_file.txt', 'local_file.txt')

# gdrive = GoogleDriveIntegration('YOUR_BUCKET_NAME')
# gdrive.upload_file('local_file.txt', 'gdrive_file.txt')
# gdrive.download_file('gdrive_file.txt', 'local_file.txt')
```