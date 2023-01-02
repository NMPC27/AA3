import collections

def count(file):
    f = open("books/"+file+".txt", "r")

    res = collections.Counter(f.read())

    data=dict(res)

    myKeys = list(data.keys())
    myKeys.sort()
    sorted_dict = {i: data[i] for i in myKeys}

    print(sorted_dict)

    f2 = open("count_"+file+".csv", "w",encoding="utf-8")

    f2.write("char,count\n")

    for key in sorted_dict:
        if key == '\n':
            continue
        f2.write(str(key) + "," + str(sorted_dict[key])+"\n")

    f2.close()
    f.close()


files=["en","fr","gr"]

for file in files:
    count(file)