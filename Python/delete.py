import requests
delete_url = "Artifact URL of the JFrog"
 headers = {
        "X-JFrog-Art-Api": jfrog_api_key (token in jfrog)
    }


response = requests.delete(delete_url, headers=headers)

if response.status_code == 204:
    print(f"File '{file_name}' deleted successfully.")
elif response.status_code == 404:
    print(f"File '{file_name}' not found in the repository.")
else:
    print(f"Failed to delete file '{file_name}' with status code: {response.status_code}")
    print(response.text)

