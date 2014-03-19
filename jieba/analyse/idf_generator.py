import jieba
import math
import sys
import re
re_han = re.compile(ur"([\u4E00-\u9FA5]+)")

d={}
total = 0
for line in open("yuliao_onlyseg.txt",'rb'):
    sentence = line.decode('utf-8').strip()
    words = set(jieba.cut(sentence))
    for w in words:
        if w in jieba.FREQ:
            d[w]=d.get(w,0.0) + 1.0
    total+=1
    if total%10000==0:
        print >>sys.stderr,'sentence count', total

new_d = [(k,math.log(v/total)*-1 ) for k,v in d.iteritems()]

for k,v in new_d:
    print k.encode('utf-8'),v