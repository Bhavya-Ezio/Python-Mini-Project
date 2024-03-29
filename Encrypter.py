import os

class Encrypt:
    def __init__(self,file,code) -> None:
        self.fileName=file
        self.code3=code%10
        code=code//10
        self.code2=code%10
        code=code//10
        self.code1=code
        try:
            self.fileObjRead=open(self.fileName,"r")
            try:
                self.fileContent=self.fileObjRead.read()
            except Exception as a:
                print(a)
        except Exception as e:
            print(f"Error in reading the file:\n{e}")
        finally:
            self.fileObjRead.close()

    def encrypt(self):
        self.encryptedText=[]
        self.sepLines()
        self.firstCypher()
        self.secondCypher()
        self.encryptedText+="\nen"
        self.encryptDataFile()
        print("\nfile updated")

    def sepLines(self):
        self.fileLines=self.fileContent.split("\n")
        # print(self.fileLines)
        for i in range(len(self.fileLines)):
            self.fileLines[i]=self.fileLines[i].split(" ")
        # print(self.fileLines)
    
    def firstCypher(self):
        m=len(self.fileLines)
        for i in range(m):
            res=[]
            n=len(self.fileLines[i])
            for j in range(len(self.fileLines[i])):
                res.append(self.fileLines[i][(j+self.code1)%n])
            self.encryptedText.append(res)
        # print("cypher text:",self.encryptedText)

    def addStrInt(self,my_char,num):
        if num==1:
            new_code = ord(my_char) + self.code2 
        else:
            new_code = ord(my_char) + self.code3   
        return chr(new_code)

    def secondCypher(self):
        m=len(self.encryptedText)
        res=""
        for i in range(m):
            n=len(self.encryptedText[i])
            for j in range(n):
                x=len(self.encryptedText[i][j])
                for k in range(x):
                    if k%2==0:
                        res+=self.addStrInt(self.encryptedText[i][j][k],2)
                    else:
                        res+=self.addStrInt(self.encryptedText[i][j][k],1)
                if j!=n-1:
                    res+=" "
            if i!=m-1:
                res+="\n"
        self.encryptedText=res
        # print("\n\nSecond cypher:\n"+self.encryptedText)

    def encryptDataFile(self):
        self.fileObjWrite=open(self.fileName,"w")    
        self.fileObjWrite.write(self.encryptedText) 
        self.fileObjWrite.close()   

    def __str__(self) -> str:
        return f"file name: {self.fileName}\ncode: {self.code1,self.code2,self.code3}"

