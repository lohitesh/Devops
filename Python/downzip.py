import os
import sys
import requests
import zipfile

destination_path = "/tmp/"
filename = f"pkg.zip"

compressed_file_path = os.path.join(destination_path, filename)

source = "https://github.com/spring-projects/spring-framework/archive/refs/tags/v5.3.26.zip"
if os.path.exists(compressed_file_path):
    print('file already downloaded skipping download')
    sys.exit(0)
response = requests.get(source)

if response.status_code == 200:
    with open(compressed_file_path, 'wb') as file:
        file.write(response.content)
    print("tar file downloaded successfully.")
else:
    print("Failed to download the tar file.")

with zipfile.ZipFile(compressed_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)
print("extracted")
