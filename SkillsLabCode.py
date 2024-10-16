count=0
name=input("Enter a name: ")
lowercaseName=name.lower()
letterInput=input("Enter a letter: ")
lowercaseLetter=letterInput.lower()
for letter in lowercaseName:
    if lowercaseLetter==letter:
        count+=1
print("Number of ", letterInput, "'s in ", name,": ",count,sep="")
