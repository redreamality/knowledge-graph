import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags.py [file name] -k [top k]"

#parse option
parser = OptionParser(USAGE) 
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print USAGE
    sys.exit(1)

file_name = args[0]

#exception handle

if opt.topK is None:
    topK = 50
else:
    topK = int(opt.topK)


#read file
content = open(file_name, 'rb').read()

#return an array of tags.(see ..\jieba\analyse\__init__.py def extract_tags)
tags = jieba.analyse.extract_tags(content, topK=topK)

print ",".join(tags)
