with open(local_file_path, "rb") as file:
    response = requests.put(upload_url, data=file, headers=self.headers)

if response.status_code == 201:
    print("Upload successful.")
else:
    print(f"Upload failed with status code: {response.status_code}")
    print(response.text)
