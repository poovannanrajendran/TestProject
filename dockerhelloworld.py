import subprocess
import datetime
import sys

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

# Define the image name (e.g., 'hello-world')
image_name = "hello-world"

# Step 1: Create a new container from the specified image
print("Creating container...")
create_command = ["docker", "create", image_name]
print(create_command)
container_id = run_docker_command(create_command)
print(f"Container created with ID: {container_id}")

# Step 2: Run the container (the 'hello-world' image will just print "Hello from Docker!" by default)
print("Running container...")
run_command = ["docker", "start", container_id]
run_docker_command(run_command)
print(f"Container {container_id} is running.")

# Step 3: Remove the container after it has finished running
print("Removing container...")
remove_command = ["docker", "rm", container_id]
run_docker_command(remove_command)
print(f"Container {container_id} has been removed.")
