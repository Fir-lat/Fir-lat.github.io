import jieba
import wordcloud
from scipy.misc import imread
n = str(input("请输入文件名"))
txt = open(n,encoding="utf-8")
t = txt.read()
for i in '~！@#￥%……&*（）——+·-=【】、；‘，。/{}|：“《》？”1234567890':
    t = t.replace(i," ")
txt.close()
mk = imread("worldmap.jpg")
list = jieba.lcut(t)
text = " ".join(list)
w = wordcloud.WordCloud(height=800,width=1000,\
    font_path = "msyh.ttc",mask=mk,background_color="seashell")
w.generate(text)
w.to_file("hah.png")