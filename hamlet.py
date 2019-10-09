def gettext():
    txt = open("hamlet.txt","r").read()
    txt = txt.lower()
    for ch in '!~@#$%^&*()_+`-={}|:"<>?[]\;,./':
        txt = txt.replace(ch, " ")
    return txt
hamletText = gettext()
words = hamletText.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(20):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))