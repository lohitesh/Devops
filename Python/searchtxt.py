import os
for roor, dir, files in os.walk("/home/ubuntu"):
    for file in files:
        if file.endswith(".txt"):
            print(file)
