f = open("file.txt","r")

def Del():
    count = 0
    for data in f.readlines():
        for word in data.split():
            count+=1
            if count%4==0:
                continue
            print(word,end=" ")

Del()

f.close()
