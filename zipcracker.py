import pyzipper
import zlib
from tqdm import tqdm

def open_password_protected_zip(file_path, password):
    try:
        with pyzipper.AESZipFile(file_path, 'r') as zip_ref:
            # Attempt to decrypt the zip file using the provided password
            zip_ref.setpassword(password.encode())
            # Check if the zip file can be read successfully
            try:
                zip_ref.read(zip_ref.infolist()[0])
                # If no exception is raised, the password is correct
                zip_ref.extractall(path=path_extract)
                # If the passowrd is correct it will extract the contents of the zipfile
                return True
            except zlib.error:
                # If zlib.error is raised, the zip file has invalid stored block lengths
                return False
    except (pyzipper.BadZipFile, RuntimeError, pyzipper.LargeZipFile, ValueError, NotImplementedError, RuntimeError):
        # If an exception is raised, the password is incorrect
        return False

banner = '\033[91m' + '''
.___________. __  .___________.    ___      .__   __. 
|           ||  | |           |   /   \     |  \ |  | 
`---|  |----`|  | `---|  |----`  /  ^  \    |   \|  | 
    |  |     |  |     |  |      /  /_\  \   |  . `  | 
    |  |     |  |     |  |     /  _____  \  |  |\   | 
    |__|     |__|     |__|    /__/     \__\ |__| \__| 
              By: PixelRazer & Trace
''' + '\033[0m'

print(banner)

file_path = input("Enter the location of the zip file: ")
password_list_file = input("Enter the location of the file containing the list of passwords: ")
path_extract = input("directory on where you want to extract the contents of the files to ")

with open(password_list_file, 'r', encoding='latin-1') as file:
    passwords = file.readlines()
    passwords = [password.strip() for password in passwords]

print(f"\nCracking password...\n")

success = False

# Use tqdm to create a progress bar
with tqdm(total=len(passwords), ncols=80) as pbar:
    for password in passwords:
        pbar.set_description(f"Trying password: {password}")
        if open_password_protected_zip(file_path, password):
            success = True
            pbar.close()
            print(f"\nPassword cracked successfully. Password is: {password}")
            break
        pbar.update(1)

if not success:
    print("\nUnable to crack the password. Password not found.")
