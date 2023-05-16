import pyzipper
import time
import os

def open_password_protected_zip(file_path, password, extraction_directory):
    try:
        with pyzipper.AESZipFile(file_path, 'r', compression=pyzipper.ZIP_LZMA) as zip_ref:
            zip_ref.extractall(path=extraction_directory, pwd=password.encode())
        print(f"\nPassword is {password}")
        return True
    except RuntimeError as e:
        print(f"RuntimeError: {str(e)}")
        return False

def show_animation():
    animation = "|/-\\"
    idx = 0
    while True:
        print(f"\rCracking password... {animation[idx]}", end="")
        idx = (idx + 1) % len(animation)
        time.sleep(0.1)

banner = '''
.___________. __  .___________.    ___      .__   __. 
|           ||  | |           |   /   \     |  \ |  | 
`---|  |----`|  | `---|  |----`  /  ^  \    |   \|  | 
    |  |     |  |     |  |      /  /_\  \   |  . `  | 
    |  |     |  |     |  |     /  _____  \  |  |\   | 
    |__|     |__|     |__|    /__/     \__\ |__| \__| 
'''

print(banner)

file_path = input("Enter the location of the zip file: ")
password_list_file = input("Enter the location of the file containing the list of passwords: ")
extraction_directory = input("Enter the directory to extract the files to: ")

with open(password_list_file, 'r') as file:
    for line in file:
        password = line.strip()
        print(f"Trying password: {password}")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console screen
        print(banner)
        show_animation()
        success = open_password_protected_zip(file_path, password, extraction_directory)
        print(f"Password cracking attempt for {password}: {'Success' if success else 'Failed'}")
        if success:
            print("\nPassword cracked successfully.")
            break
    else:
        print("\nUnable to crack the password. Password not found.")
