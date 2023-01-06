import collections

chars = ["\n"," ",",",".","!","?",";",":","'","\"","(",")","[","]","{","}","<",">","/","\\",
        "|","@","#","$","%","^","&","*","-","+","=","_","~","`"
        "©"," ","‰","¨","´","¹","»","®","¢","ª","ˆ","¯","«","¼","©","¤"]

def count(file):
    f = open("books/"+file+".txt", "r")

    res = collections.Counter(f.read().upper())

    data=dict(res)

    sorted_dict={k: v for k, v in sorted(data.items(), key=lambda item: item[1],reverse=True)}
    soma=sum(sorted_dict.values())

    for key in sorted_dict:
        if key in chars:
            soma-=sorted_dict[key]

    f2 = open("ExactCount_"+file+".csv", "w",encoding="utf-8")

    f2.write("char,count,percentage\n")

    for key in sorted_dict:
        if key in chars:
            continue
        f2.write(str(key) + "," + str(sorted_dict[key])+","+str(sorted_dict[key]/soma*100)+"\n")

    f2.close()
    f.close()


files=["en","fr","gr"]

for file in files:
    count(file)