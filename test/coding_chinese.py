#coding=UTF-8

import sys
mystr = "卧槽"
print mystr
type = sys.getfilesystemencoding()
print mystr.decode('utf-8').encode(type)