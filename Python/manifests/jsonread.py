import json
import os

with open("org.springframework_spring-core.json", 'r') as fh:
    json_data = json.load(fh)
    for top, versions in json_data.items():
        for version, attribute in versions.items():
            print(version)
            print(attribute)
            #if ver == version:
             #   build_cmd = attribute.get("BuildCmd", [])

