rawfile = input("enter the file containing raw email data:")
destfile = input("Enter the file to create which will contain output")

raw_file = open(rawfile,"r")
rawdata = raw_file.read()
emails = re.findall(r"\w+@\w+\.\w+",rawdata)
raw_file.close()
email_file = open(destfile, "w")
for line in emails:
	  email_file.write(line + "\n")
email_file.close()
