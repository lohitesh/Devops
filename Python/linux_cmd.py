import subprocess

# Define the command you want to execute
command = [
       'grep -rl "org" *',
       'ls',
       'pwd'
       ]

# Run the command
The stdout=subprocess.PIPE parameter captures the output of the command, which you can then access using result.stdout.
for cmd in command:
    result = subprocess.run(cmd, shell=True, check=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  # Print the output
    print(result.stdout)
    print(result.stderr, end='')
  # end='' used to remove newline
