# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import sys
import codecs
sys.path.append('../')
import time
import jieba
import jieba.analyse
from optparse import OptionParser

jieba.load_userdict("userdict.txt")

print ("importing snowNLP...")
from snownlp import normal
#from snownlp import seg
#from snownlp.summary import textrank
print ("snowNLP imported")


USAGE = "usage:    python extract_tags.py [file name] -k [top k]"

#parse option
parser = OptionParser(USAGE) 
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print (USAGE)
    sys.exit(1)

file_name = args[0]

#exception handle

if opt.topK is None:
    topK = 50
else:
    topK = int(opt.topK)


#read file
content = open(file_name, 'rb').read()



#----------------key words-------------------

#return an array of tags.(see ..\jieba\analyse\__init__.py def extract_tags)
tags,reduced = jieba.analyse.extract_tags(content, topK=topK)
if reduced:
    print ("keyword list reduced")
key_words=",".join(tags)
#----------------explanation-------------------

#return an array of explanation
t = content.decode("utf-8")
sums = normal.get_summary(tags,t) #in snowNLP

ss = "\n\n".join(sums)
# print (sums[0:1])

#timemark
timemark = time.strftime("%Y-%m-%d %X", time.localtime())
cutline = "\n------------------------%s-------------------------\n" % str(timemark) 

#file output
myfile = codecs.open("output3.txt", 'a+','utf-8')
myfile.write(ss)
myfile.write(cutline.decode('utf-8'))
myfile.close()

