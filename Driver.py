from Encrypter import Encrypt as en

# choice=input("Enter your choice (Encrypt/Decrypt): ")
choice="E"
if choice=="E":

    # fname=input("Enter the name of file: ")
    # code=input("Enter a 3 digit code for the file: ")
    enObj=en("file.txt",123)
    print(enObj)
    enObj.encrypt()
    del enObj
# else:
    # try:
        
    # except Exception as e:
    #     print(e)