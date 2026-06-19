import random,string

def translateFile(path,newPath,fromStr="",toStr="",remove="",inserts=("",),insertChance=0.5):
    try: 
        newFile = open(newPath,"x")
    except FileExistsError: 
        newFile = open(newPath,"w")
    with open(path, "r") as file:
        first = file.readline()
        try: 
            random.seed(ord(first[0]))
        except: 
            random.seed(1)
        table = str.maketrans(fromStr,toStr,remove)
        lines,newLines = file.readlines(),[]
        for line in lines:
            newLines.append(line.translate(table))
        for i in range(len(newLines)):
            if (random.random() < insertChance) and (i != len(newLines)-1): 
                newLines[i] = newLines[i][:-1]+f" {random.choice(inserts)}\n"
        newFile.write(first.translate(table))
        for i in newLines: 
            newFile.write(i)
        file.close()
       
fromStr = "LlRr"
toStr = "WwWw"
remove = ""
inserts = (":3","^^","Nyaa~","Meow~","UwU","OwO","Teehee...",">w<")
insertChance = 0.5
toAdd = "UwU"
path = input("File path:")
fileEnd = path[path.find("."):] if "." in path else ""
newPath = path.rstrip(fileEnd)+f"{toAdd}{fileEnd}"

translateFile(path,newPath,fromStr,toStr,remove,inserts,insertChance)
