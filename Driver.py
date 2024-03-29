import os
from Encrypter import Encrypt as en
from Decryptor import Decrypt as de

choice=input("Enter your choice (E for Encryption/D for Decryption): ")
if choice=="E" or choice == "e":
    while True:
        fileName=input("Enter the name of the file: ")
        if os.path.exists(fileName):
            break
        elif os.path.exists(f"{fileName}.txt"):
            fileName=f"{fileName}.txt"
            break
        else:
            print("Entered name of file does not exists.Enter another name.")
            continue
        
    code=(int)(input("Enter a 3 digit code for the file: "))
    enObj=en(fileName,code)
    enObj.encrypt()
    del enObj

elif choice=="D" or choice=="d":
    while True:
        fileName=input("Enter the name of the file: ")
        if os.path.exists(fileName):
            break
        elif os.path.exists(f"{fileName}.txt"):
            fileName=f"{fileName}.txt"
            break
        else:
            print("Entered name of file does not exists.Enter another name.")
            continue
    code=(int)(input("Enter a 3 digit code for the file: "))
    deObj=de(fileName,code)
    deObj.decrypt()
    del deObj

else:
    print("Incorrect choice.")