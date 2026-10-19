import subprocess
import os
with open ("/etc/os-release","r") as file:
	lines = file.readlines()
os_name = " "
version = " "
user_id = os.geteuid()
is_root = (user_id == 0)
for line in lines:
	if line.startswith("NAME="):
		os_name=line.split("=",1)[1].strip().strip('"')
	if line.startswith("VERSION="):
		version=line.split("=",1)[1].strip().strip('"')
		break
result = subprocess.run(
	["whoami"],
	capture_output = True,
	text = True
)
print("================================")
print("  MY SECURITY AUDITOR SESSION")
print("================================")
print("Operating System :", os_name)
print("Version          :", version)
print("User             :", result.stdout.strip())
print("user ID          :", user_id)
print("root user        :", is_root)

