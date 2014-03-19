#coding:utf-8
import codecs
sums = ["a:\n我了个大去","2:\n我了个草"]
ss = "\n\n".join(sums)

cutline = "\n-----------cut------------\n"
myfile = codecs.open("testit.txt", 'a+','utf-8')
myfile.write(ss.decode('utf-8'))
myfile.write(cutline.decode('utf-8'))
myfile.close()