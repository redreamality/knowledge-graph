# -*- coding:utf-8 -*-

import re

sents = ["啊哈我今天吃了一条鱼", "啊我死了","你脑有病啊哈"]
tag = ["啊哈","我"]

sums = {}.fromkeys(tag,[])
output = []
for sent in sents:
	for pattern in tag:     
		if re.search(pattern,sent): #match pattern 
			sums[pattern]=sums[pattern]+[sent]
		else:
			pass
	# to do: add exception handle: if there's no sufficient match

for k,v in sums.iteritems():
	sum4one = "。".join(v)
	s = "%s:\n%s。"%(k,sum4one)
	output.append(s)
	print s.decode("utf-8")
	
	
ss = "\n\n".join(output)
print ss.decode("utf-8")	
# for k,v in sums.iteritems():
	# s = "%s:\n%s。\n"%(k,"。".join(v))
	# output = output.append(s)
