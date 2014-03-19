# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

text = '''测试文本。测试文本2.啊哈大风阿拉山口煎熬！哦恩负啊！
我了个去！
尼玛卧槽喇？你才非主流你全家都非主流'''

print ("importing...")
from snownlp import normal
#from snownlp import seg
#from snownlp.summary import textrank
print ("import done")

if __name__ == '__main__':
	
    t = normal.zh2hans(text)
    sents = normal.get_sentences(t)
    print ("\n".join(sents))
	
        # words = seg.seg(sent)
        # words = normal.filter_stop(words)
        # doc.append(words)
    # rank = textrank.TextRank(doc)
    # rank.solve()
    # for index in rank.top_index(5):
        # print(sents[index])
    # keyword_rank = textrank.KeywordTextRank(doc)
    # keyword_rank.solve()
    # for w in keyword_rank.top_index(5):
        # print(w)
