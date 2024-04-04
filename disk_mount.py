import os

# Mount the USB mass storage device
#machine.UF2Boot.USB
#uos.mount(machine.UF2Boot.USB, "/usb")

# List files on the USB mass storage
usb_mount_path = '/'  # USB 마운트된 디렉토리 경로
print("Files on USB mass storage:")
print(os.listdir(usb_mount_path))
    
# Create or open a file on the USB mass storage
file_path = 'test_file.txt'
with open(file_path, 'w') as file:
    file.write("Hello, USB mass storage!")
print("File written successfully to USB mass storage:", file_path)

# Read the contents of the file
with open(file_path, 'r') as file:
    content = file.read()
print("File content:")
print(content)

# Delete the file
os.remove(file_path)
print("File deleted successfully from USB mass storage")
print(os.listdir(usb_mount_path))

# Unmount the filesystem
os.umount(usb_mount_path)
print("USB mass storage device unmounted")