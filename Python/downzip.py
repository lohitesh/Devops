import os
import sys
import requests
import zipfile
import json

destination_path = "/home/ubuntu/test/"
filename = f"pkg.zip"

compressed_file_path = os.path.join(destination_path, filename)


package_name = input("Enter the package name to read the attribue from json line\n")
print(package_name)

name, ver = package_name.rsplit(':', 1)
print(name)
print(ver)
json_file = "{}.json".format(name.replace(":", "_"))

json_path = os.path.join("manifests", json_file)
print(json_file)


with open(json_path, 'r') as fh:
    json_data = json.load(fh)
    for top, versions in json_data.items():
        for ver1, attribute in versions.items():
            if ver == ver1:
                source = attribute['SourceUrl']
                print(source)

if os.path.exists(compressed_file_path):
    print('file already downloaded skipping download')
    sys.exit(0)


response = requests.get(source)

if response.status_code == 200:
    with open(compressed_file_path, 'wb') as file:
        file.write(response.content)
    print("zip file downloaded successfully.")
else:
    print("Failed to download the zip file.")

with zipfile.ZipFile(compressed_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_path)
print("extracted")
