#-*-coding:utf-8-*-
import jieba
def tk():
    text = open("threekingdoms.txt","r",encoding="utf-8").read()
    for i in '~！@#￥%……&*（）——+·-=【】、；，。/{}|：“”《》？':
        text = text.replace(i,"")
    return text
excludes = {"将军","却说","荆州","二人","不可","不能",\
            "如此","商议","如何","主公","军士","左右",\
            "军马","次日","引兵","大喜","天下","东吴",\
            "于是","今日","不敢","魏兵","陛下","都督",\
            "人马","不知","一人","汉中","只见","众将",\
            "后主"}
my = tk()
words = jieba.lcut(my)
count = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰" or word == "诸葛孔明":
        reword = "孔明"
    elif word == "关公" or word == "云长":
        reword = "关羽"
    elif word == "玄德" or word == "玄德曰" or word == "刘玄德":
        reword = "刘备"
    elif word == "孟德" or word == "丞相" or word == "丞相曰" or word == "曹孟德" or word == "曹公":
        reword = "曹操"
    else:
        reword = word
    count[reword] = count.get(reword,0) + 1
for word in excludes:
    del count[word]
ai = list(count.items())
ai.sort(key=lambda x:x[1],reverse=True)
for i in range(100):
    name,counts = ai[i]
    print("{:<10}{:>5}".format(name,counts))