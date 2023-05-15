import pyzipper

def open_password_protected_zip(file_path, password):
    try:
        with pyzipper.AESZipFile(file_path, 'r', compression=pyzipper.ZIP_LZMA) as zip_ref:
            zip_ref.extractall(pwd=password.encode())
        print(f"Password is {password}")
        return True
    except RuntimeError as e:
        return False


file_path = input("Enter the location of the zip file: ")
password_list_file = input("Enter the location of the file containing the list of passwords: ")

with open(password_list_file, 'r') as file:
    for line in file:
        password = line.strip()
        if open_password_protected_zip(file_path, password):
            break
