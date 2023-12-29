import os

def process_json():
    package_name = input("Enter the package name to read the attribue from json line\n")

    name, ver = package_name.rsplit(':', 1)
    json_file = "{}.json".format(name.replace(":", "_"))
    print(json_file)


    with open(json_file, 'r') as fh:
        json_data = json.load(fh)
        for top, versions in json_data.items():
            for ver1, attribute in versions.items():
                if ver == ver1:
                    print(attribute['SourceUrl'])
                    print(attribute['BuildCmd'])

if __name__ == "__main__":
    process_json()
