secret = "abcdefghigklmnopqrstuvwxyz"
secretUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = int(input("Enter the number to move the text by: "))

summary = ""

def changeChar(char):
    if char in secret:
        return secret[(secret.index(char) + number) % len(secret)]
    elif char in secretUp:
        return secretUp[(secretUp.index(char) + number) % len(secretUp)]
    else:
        return char
        
with open("filename.txt", encoding="utf8") as myFile:
    for line in myFile:
        for char in line:
            summary += changeChar(char)
            
with open("output.txt", "w", encoding="utf8") as myFile:
    myFile.write(summary)