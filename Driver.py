from Encrypter import Encrypt as en
from Decryptor import Decrypt as de

choice=input("Enter your choice (E for Encryption/D for Decryption): ")
if choice=="E" or choice == "e":
    fname=input("Enter the name of file: ")
    code=(int)(input("Enter a 3 digit code for the file: "))
    enObj=en(fname,code)
    print(enObj)
    enObj.encrypt()
    del enObj

if choice=="D" or choice=="d":
    fname=input("Enter the name of file: ")
    code=(int)(input("Enter a 3 digit code for the file: "))
    deObj=de(fname,code)
    deObj.decrypt()
    del deObj