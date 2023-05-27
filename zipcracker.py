# imports
import pyzipper
import zlib
import time
import threading

def open_password_protected_zip(file_path, password):
    try:
        with pyzipper.AESZipFile(file_path, 'r') as zip_ref:
            # decrypt the zip file using the provided password
            zip_ref.setpassword(password.encode())
            # check if the zip file can be read successfully
            zip_ref.read(zip_ref.infolist()[0])
            # if no exception is raised, the password is correct
            zip_ref.extractall(path=path_extract)
            # if the password is correct, extract the contents of the zipfile
            return True
    except (pyzipper.BadZipFile, zlib.error):
        # if an exception is raised, the password is incorrect or the zip file is invalid
        return False

def crack_password(passwords):
    success = False
    for password in passwords:
        if open_password_protected_zip(file_path, password):
            success = True
            print(f"\nPassword cracked successfully. Password is: {password}")
            break

    if not success:
        print("\nUnable to crack the password. Password not found.")

banner = '\033[91m' + '''
.___________. __  .___________.    ___      .__   __. 
|           ||  | |           |   /   \     |  \ |  | 
`---|  |----`|  | `---|  |----`  /  ^  \    |   \|  | 
    |  |     |  |     |  |      /  /_\  \   |  . `  | 
    |  |     |  |     |  |     /  _____  \  |  |\   | 
    |__|     |__|     |__|    /__/     \__\ |__| \__| 
              By: PixelRazer & Trace
    Contributers: JustinsRepo
''' + '\033[0m'

print(banner)

file_path = input("Enter the location of the zip file: ")
password_list_file = input("Enter the location of the file containing the list of passwords: ")
path_extract = input("Directory where you want to extract the contents of the files to: ")

with open(password_list_file, 'r', encoding='latin-1') as file:
    passwords = [password.strip() for password in file.readlines()]

print(f"\nCracking password...\n")

#splitting password threads
num_threads = 4
password_chunks = [passwords[i:i+num_threads] for i in range(0, len(passwords), num_threads)]

#thread creation
threads = []
for chunk in password_chunks:
    thread = threading.Thread(target=crack_password, args=(chunk,))
    thread.start()
    threads.append(thread)

#thread finish
for thread in threads:
    thread.join()
