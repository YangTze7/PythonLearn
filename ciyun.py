#coding:utf-8
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
background_Image = plt.imread('')

text_from_file_with_apath = open('text.txt' , 'rb').read()
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)
my_wordcloud = WordCloud(background_color="white",
                          margin=0,
                          width=512,
                          height=512,
                          mask=background_Image,
                          max_words=2000,
                          max_font_size=64,
                          random_state=42).generate(wl_space_split)
my_wordcloud.font_path = 'msyh.ttf'
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
