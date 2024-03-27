import os
from Encrypter import Encrypt as en
from Decryptor import Decrypt as de

choice=input("Enter your choice (E for Encryption/D for Decryption): ")
if choice=="E" or choice == "e":
    while True:
        fname=input("Enter the name of the file:")
        if os.path.exists(fname):
            break
        elif os.path.exists(f"{fname}.txt"):
            fname=f"{fname}.txt"
            break
        else:
            print("Entered name of file does not exists.Enter another name.")
            continue
        
    code=(int)(input("Enter a 3 digit code for the file: "))
    enObj=en(fname,code)
    enObj.encrypt()
    del enObj

if choice=="D" or choice=="d":
    while True:
        fname=input("Enter the name of the file:")
        if os.path.exists(fname):
            break
        elif os.path.exists(f"{fname}.txt"):
            fname=f"{fname}.txt"
            break
        else:
            print("Entered name of file does not exists.Enter another name.")
            continue
    code=(int)(input("Enter a 3 digit code for the file: "))
    deObj=de(fname,code)
    deObj.decrypt()
    del deObj