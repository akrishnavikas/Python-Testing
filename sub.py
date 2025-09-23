import subprocess

# Run a simple shell command
result = subprocess.run(["echo", "Hello Hadoop"], capture_output=True, text=True)
print(result.stdout)
