import collections

def count(file):
    f = open("books/"+file+".txt", "r")

    res = collections.Counter(f.read())

    data=dict(res)

    sorted_dict={k: v for k, v in sorted(data.items(), key=lambda item: item[1])}

    f2 = open("exact_count_"+file+".csv", "w",encoding="utf-8")

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