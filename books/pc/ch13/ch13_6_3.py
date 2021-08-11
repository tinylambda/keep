import subprocess

text = b'''
hello world
this is a test
goodbye
'''

# launch a command with pipes
p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

# send the data and get the output
stdout, stderr = p.communicate(text)

# to interpret as text, decode
out = stdout.decode('utf-8') if stdout else None
err = stderr.decode('utf-8') if stderr else None

print(out)
print(err)
