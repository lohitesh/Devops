import requests
import os
import tarfile

path = "/home/ubuntu"
file_path = os.path.join(path, "apache_tomcat.tar.gz")
source_url = "https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz"

try:
    response = requests.get(source_url)
    response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print("Tar file downloaded successfully.")

    with tarfile.open(file_path, 'r') as tar:
        tar.extractall("/home/ubuntu")
    print("Tar file extracted successfully.")

except requests.exceptions.RequestException as e:
    print(f"Failed to download the tar file. Error: {e}")

except tarfile.TarError as e:
    print(f"Error during tar extraction: {e}")
