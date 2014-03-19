# -*- coding:utf-8 -*-
#test_re
import re
pattern = "啊哈"
msgs = ["啊哈我今天吃了一条鱼", "啊我死了","你脑有病啊哈"]
sum = []

for msg in msgs:
	if re.search(pattern,msg):
		print msg.decode("utf-8"),"aha found"
		sum.append(msg)
	else:
		print msg.decode("utf-8"),"aha missed"
		
print "。".join(sum).decode("utf-8")