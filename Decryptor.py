class Decrypt:

    def __init__(self,file,code) -> None:
        self.fileName=file
        self.code=code
        self.code1=(code//10)
        self.code2=code%10
        try:
            self.fileObj=open(self.fileName)
            try:
                self.fileContent=self.fileObj.read()
            except Exception as a:
                print(a)
        except Exception as e:
            print(e)
    
    def decrypt(self):
        self.decryptedText=[]
        self.sepLines()
        self.firstDecrypt()
        self.secondDecrypt()
        self.decryptDataFile()
    
    def sepLines(self):
        self.fileLines=self.fileContent.split("\n")
        print(self.fileLines)
        for i in range(len(self.fileLines)):
            self.fileLines[i]=self.fileLines[i].split(" ")
        print(self.fileLines)
    
    def subStrInt(self,my_char:int):
        new_code = ord(my_char) - self.code2
        shifted_char = chr(new_code)    
        return shifted_char
    
    def __str__(self) -> str:
        return f"file name: {self.fileName} code: {self.code}"
    
    def __del__(self):
        print("file closed.")
        self.fileObj.close()