
import subprocess
import os
import stat
with open ("/etc/os-release","r") as file:
	lines = file.readlines()
os_name = " "
version = " "
user_id = os.geteuid()
is_root = (user_id == 0)
path = "/etc/shadow"
metadata = os.stat(path)
mode = stat.S_IMODE(metadata.st_mode)

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
print("Operating System   :", os_name)
print("Version            :", version)
print("User               :", result.stdout.strip())
print("user ID            :", user_id)
print("root user          :", is_root)

if is_root:
	print("Status            : Running as a root user")
else :
	print("Status            : Running as a non-root user")

print("File               :", path)
print("Permission mode    :", mode)

def check_permissions(path):
	metadata = os.stat(path)
	mode = stat.S_IMODE(metadata.st_mode)
	print("Shadow permissions :", oct(check_permissions("/etc/shadow")))
	print("Passwd permissions :", oct(check_permissions("/etc/passwd")))
