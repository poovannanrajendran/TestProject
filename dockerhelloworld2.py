import subprocess
import datetime
import sys
import os

# Function to run a Docker command and handle errors
def run_docker_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Failed to run {' '.join(command)}: {e.stderr}")
        exit(1)

# Print a simple greeting
print("Hello, World!")

# Get the current date and time
current_datetime = datetime.datetime.now()
print("Current Date and Time:", current_datetime)

# Print Python version information
print("Python version:")
print(sys.version)
print(sys.platform)

# Define the image name (e.g., 'python:3.8-slim' for a lightweight Python environment)
image_name = "python:3.8-slim"

# Create a Python script to print environment and Python version information inside the container
python_script = """
import os
import sys

print("Environment Information:")
for key, value in os.environ.items():
    print(f"{key}: {value}")

print("\\nPython version from within Docker:")
print(sys.version)
print(sys.platform)
"""

# Save the Python script to a file
script_path = "container_info.py"
with open(script_path, "w") as f:
    f.write(python_script)

# Step 1: Create a new container from the specified image and add the Python script
print("Creating container...")
create_command = [
    "docker", "create", "--name", "info_container", "-v", f"{os.path.abspath(script_path)}:/usr/src/app/container_info.py", image_name, "python", "/usr/src/app/container_info.py"
]
print(create_command)
container_id = run_docker_command(create_command)
print(f"Container created with ID: {container_id}")

# Step 2: Run the container
print("Running container...")
run_command = ["docker", "start", "-i", container_id]
run_docker_command(run_command)
print(f"Container {container_id} is running.")

# Step 3: Remove the container after it has finished running
print("Removing container...")
remove_command = ["docker", "rm", container_id]
run_docker_command(remove_command)
print(f"Container {container_id} has been removed.")

# Clean up the Python script file
os.remove(script_path)
