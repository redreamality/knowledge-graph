# -*- coding: utf-8 -*-
import jieba
import os
import codecs
try:
    from analyzer import ChineseAnalyzer
    print("ChineseAnalyzer Imported")
except ImportError:
    print("ImportError")
    
tfidf_threshold = 0.045 #可以更改
newword_bias = 2 #可以更改
    
_curpath=os.path.normpath( os.path.join( os.getcwd(), os.path.dirname(__file__) )  )
f_name = os.path.join(_curpath,"idf.txt")
content = open(f_name,'rb').read().decode('utf-8')

idf_freq = {}
lines = content.split('\n')
for line in lines:
    word,freq = line.split(' ')
    idf_freq[word] = float(freq)#idf_freq:[word:freq,word:freq] #

median_idf = sorted(idf_freq.values())[len(idf_freq)/2] # idf_freq.value:所有IDF值的数组,median_idf,idf值的中位数
# print "median_idf:",median_idf,"\n"
stop_words= set([
"the","of","is","and","to","in","that","we","for","an","are","by","be","as","on","with","can","if","from","which","you","it","this","then","at","have","all","not","one","has","or","that"
])

# return tags(a list), here tfidf'ed.
def extract_tags(sentence,topK=20):
    #words
    words = jieba.cut(sentence)
    
    freq = {}#词频
    
    for w in words:
        if len(w.strip())<2: continue#to remove whitespaces
        if w.lower() in stop_words: continue
        freq[w]=freq.get(w,0.0)+1.0 #get(w（在字典freq里）,0.0（没找到就赋初值0.0）)
    total = sum(freq.values())
    freq = [(k,v/total) for k,v in freq.iteritems()] #词频

    tf_idf_list = [(v * idf_freq.get(k,median_idf+newword_bias),k) for k,v in freq] #同样，get没找到就赋给初值median+bias
    
    st_list = sorted(tf_idf_list,reverse=True)
    # #-------获取tfidf值------------
    # myfile = codecs.open("tfidf_value2.txt", 'wb','utf-8')
    # for v,k in st_list:
        # ss = "%s:%s\n"%(k,str(v))
        # myfile.write(ss)
        
    # myfile.close()
    
    #----------将阈值和topk比较，去掉垃圾词-----------
    values = [a[0] for a in st_list if a[0]>tfidf_threshold]#阈值，可更改
    length_K=len(values)
    topK,reduced = (topK,0) if (length_K>topK) else (length_K,1)
    top_tuples= st_list[:topK]
    #
    tags = [a[1] for a in top_tuples]
    return tags,reduced
