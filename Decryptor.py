import os

class Decrypt:

    def __init__(self,file,code):
        self.fileName=file
        self.code3=code%10
        code=code//10
        self.code2=code%10
        code=code//10
        self.code1=code
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
    
    def firstDecrypt(self):
        m=len(self.fileLines)
        for i in range(m):
            res=[]
            n=len(self.fileLines[i])
            for j in range(len(self.fileLines[i])):
                res.append(self.fileLines[i][(j-self.code1)%n])
            self.decryptedText.append(res)
        # print("first decrypt:\n",self.decryptedText)
     
    def subStrInt(self,my_char,num):
        if num==1:
            new_code = ord(my_char) - self.code2 
        else:
            new_code = ord(my_char) - self.code3     
        return chr(new_code)
    
    def secondDecrypt(self):
        m=len(self.decryptedText)
        res=""
        for i in range(m):
            n=len(self.decryptedText[i])
            for j in range(n):
                x=len(self.decryptedText[i][j])
                for k in range(x):
                    if k%2==0:
                        res+=self.subStrInt(self.decryptedText[i][j][k],2)
                    else:
                        res+=self.subStrInt(self.decryptedText[i][j][k],1)
                if j!=n-1:
                    res+=" "
            if i!=m-1:
                res+="\n"
        self.decryptedText=res
        print("second decrypt:\n"+self.decryptedText+"\n\n")

    def decryptDataFile(self):
        i=1
        while os.path.exists(f"file{i}.txt"):
            i+=1
        
        try:
            fileObj=open(f"file{i}.txt","w")
            fileObj.write(self.decryptedText)
            file_path = os.path.abspath(fileObj.name)
            print(f"New file created with decyphered text at :{file_path}")
            fileObj.close()
        except Exception as x:
            print(f"Error in creating encrypt file:\n{x}")
        

    def __str__(self) -> str:
        return f"file name: {self.fileName} code: {self.code}"
    
    def __del__(self):
        print("file closed.")
        self.fileObj.close()