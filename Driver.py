from Encrypter import Encrypt as en
from Decryptor import Decrypt as de
# choice=input("Enter your choice (Encrypt/Decrypt): ")
choice="D"
if choice=="E":

    # fname=input("Enter the name of file: ")
    # code=input("Enter a 3 digit code for the file: ")
    enObj=en("file.txt",123)
    print(enObj)
    enObj.encrypt()
    del enObj

if choice=="D":
    # fname=input("Enter the name of file: ")
    # code=input("Enter a 3 digit code for the file: ")
    enObj=de("file1.txt",123)
    # print(enObj)
    enObj.decrypt()
    del enObj