#! /usr/bin/env python  
#! /usr/bin/env python  
#coding=utf-8  
#Author: JarvisChu  
#Blog: blog.csdn.net/jarvischu  
import sys,urllib2,appGetWeather_help  
  
#Locate the city  
city_info = urllib2.urlopen( 'http://pv.sohu.com/cityjson').read()    
print city_info
city = "֣ݭʡڼםː"
# city = city_info.split('=')[1].split(',')[2].split('"')[3]  #split out the city name'''  
print u"źքԇː:",city  
#------------------------------------------------------------------------------  
  
#convert city name to short  
cityName=appGetWeather_help.convertName(city)  
#print cityName  
  
#convert city name to cityID  
cityID=appGetWeather_help.getCityCodeFromName(cityName)  
#print "cityId:",cityID  
#---------------------------------------------------  
  
#get the weather  
msg = appGetWeather_help.getCityWeather_RealTime(cityID)  
print u'ԇː:    ',msg['city']  
print u'Ǹς:    ',msg['temp']  
print u'اвú   ',msg['wind']  
print u'ʪ׈ú   ',msg['sd']  
print u'ټтʱݤ:',msg['time']#! /usr/bin/env python  
#coding=utf-8  
#Author: JarvisChu  
#Blog: blog.csdn.net/jarvischu  
  
import sys,urllib2,appGetWeather_help  
  
#Locate the city  
city_info = urllib2.urlopen( 'http://pv.sohu.com/cityjson').read()    
print city_info
city = "֣ݭʡڼםː"
# city = city_info.split('=')[1].split(',')[2].split('"')[3]  #split out the city name'''  
print u"źքԇː:",city  
#------------------------------------------------------------------------------  
  
#convert city name to short  
cityName=appGetWeather_help.convertName(city)  
#print cityName  
  
#convert city name to cityID  
cityID=appGetWeather_help.getCityCodeFromName(cityName)  
#print "cityId:",cityID  
#---------------------------------------------------  
  
#get the weather  
msg = appGetWeather_help.getCityWeather_RealTime(cityID)  
print u'ԇː:    ',msg['city']  
print u'Ǹς:    ',msg['temp']  
print u'اвú   ',msg['wind']  
print u'ʪ׈ú   ',msg['sd']  
print u'ټтʱݤ:',msg['time']
#Author: JarvisChu  
#Blog: blog.csdn.net/jarvischu  
  
import sys,urllib2,appGetWeather_help  
  
#Locate the city  
city_info = urllib2.urlopen( 'http://pv.sohu.com/cityjson').read()    
print city_info
city = "֣ݭʡڼםː"
# city = city_info.split('=')[1].split(',')[2].split('"')[3]  #split out the city name'''  
print u"źքԇː:",city  
#------------------------------------------------------------------------------  
  
#convert city name to short  
cityName=appGetWeather_help.convertName(city)  
#print cityName  
  
#convert city name to cityID  
cityID=appGetWeather_help.getCityCodeFromName(cityName)  
#print "cityId:",cityID  
#---------------------------------------------------  
  
#get the weather  
msg = appGetWeather_help.getCityWeather_RealTime(cityID)  
print u'ԇː:    ',msg['city']  
print u'Ǹς:    ',msg['temp']  
print u'اвú   ',msg['wind']  
print u'ʪ׈ú   ',msg['sd']  
print u'ټтʱݤ:',msg['time']