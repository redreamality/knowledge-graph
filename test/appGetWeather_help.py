#! /usr/bin/env python  
#coding=utf-8  
#Author: JarvisChu  
#Blog: blog.csdn.net/jarvischu  
  
#import os, io, re, time, base64  
import sys,urllib2  
  
  
cityList_main = [   #全国主要城市  
    #华北  
    {'code':"101010100", 'name':"北京"},  
    {'code':"101030100", 'name':"天津"},  
    {'code':"101090101", 'name':"石家庄"},  
    {'code':"101100101", 'name':"太原"},  
    {'code':"101080101", 'name':"呼和浩特"},  
    {'code':"101090201", 'name':"保定"},  
    {'code':"101100201", 'name':"大同"},  
    {'code':"101080201", 'name':"包头"},  
    {'code':"101090402", 'name':"承德市"},  
    {'code':"101100401", 'name':"晋中"},  
    {'code':"101080501", 'name':"通辽"},  
    {'code':"101091101", 'name':"秦皇岛"},  
    #东北  
    {'code':"101050101", 'name':"哈尔滨"},  
    {'code':"101060101", 'name':"长春"},  
    {'code':"101070101", 'name':"沈阳"},  
    {'code':"101050201", 'name':"齐齐哈尔"},  
    {'code':"101060201", 'name':"吉林"},  
    {'code':"101070201", 'name':"大连"},  
    {'code':"101050301", 'name':"牡丹江"},  
    {'code':"101060301", 'name':"延吉"},  
    {'code':"101070301", 'name':"鞍山"},  
    {'code':"101050501", 'name':"绥化"},  
    {'code':"101060601", 'name':"白城"},  
    {'code':"101071401", 'name':"葫芦岛"},  
    #华南  
    {'code':"101280101", 'name':"广州"},  
    {'code':"101300101", 'name':"南宁"},  
    {'code':"101310101", 'name':"海口"},  
    {'code':"101320101", 'name':"香港"},  
    {'code':"101330101", 'name':"澳门"},  
    {'code':"101280601", 'name':"深圳"},  
    {'code':"101300501", 'name':"桂林"},  
    {'code':"101310201", 'name':"三亚"},  
    {'code':"101280701", 'name':"珠海"},  
    {'code':"101281701", 'name':"中山"},  
    {'code':"101301001", 'name':"百色"},  
    {'code':"101310215", 'name':"万宁"},  
    #西北  
    {'code':"101110101", 'name':"西安"},  
    {'code':"101160101", 'name':"兰州"},  
    {'code':"101150101", 'name':"西宁"},  
    {'code':"101170101", 'name':"银川"},  
    {'code':"101130101", 'name':"乌鲁木齐"},  
    {'code':"101110300", 'name':"延安"},  
    {'code':"101110901", 'name':"宝鸡"},  
    {'code':"101160901", 'name':"天水"},  
    {'code':"101170301", 'name':"吴忠"},  
    {'code':"101130501", 'name':"吐鲁番"},  
    {'code':"101160801", 'name':"酒泉"},  
    {'code':"101170401", 'name':"固原"},  
    #西南  
    {'code':"101040100", 'name':"重庆"},  
    {'code':"101270101", 'name':"成都"},  
    {'code':"101260101", 'name':"贵阳"},  
    {'code':"101290101", 'name':"昆明"},  
    {'code':"101140101", 'name':"拉萨"},  
    {'code':"101270401", 'name':"绵阳"},  
    {'code':"101260201", 'name':"遵义"},  
    {'code':"101290201", 'name':"大理"},  
    {'code':"101271401", 'name':"乐山"},  
    {'code':"101260801", 'name':"六盘水"},  
    {'code':"101291401", 'name':"丽江"},  
    #华东  
    {'code':"101020100", 'name':"上海"},  
    {'code':"101230101", 'name':"福州"},  
    {'code':"101220101", 'name':"合肥"},  
    {'code':"101240101", 'name':"南昌"},  
    {'code':"101120101", 'name':"济南"},  
    {'code':"101210301", 'name':"嘉兴"},  
    {'code':"101190101", 'name':"南京"},  
    {'code':"101210401", 'name':"宁波"},  
    {'code':"101210101", 'name':"杭州"},  
    {'code':"101190401", 'name':"苏州"},  
    {'code':"101120201", 'name':"青岛"},  
    {'code':"101230201", 'name':"厦门"},  
    {'code':"101340101", 'name':"台北市"},  
    #华中  
    {'code':"101180101", 'name':"郑州"},  
    {'code':"101200101", 'name':"武汉"},  
    {'code':"101250101", 'name':"长沙"},  
    {'code':"101180201", 'name':"安阳"},  
    {'code':"101200201", 'name':"襄阳"},  
    {'code':"101250201", 'name':"湘潭"},  
    {'code':"101250301", 'name':"株洲"},  
    {'code':"101180401", 'name':"许昌"},  
    {'code':"101250601", 'name':"常德"},  
    {'code':"101251101", 'name':"张家界"},  
    {'code':"101200401", 'name':"孝感"},  
    {'code':"101201401", 'name':"FINLAND"}  
]  
  
''''' 
{"weatherinfo":{"city":"北京","cityid":"101010100","temp":"25","WD":"东风", 
"WS":"2级","SD":"50%","WSE":"2","time":"20:30","isRadar":"1","Radar":"JC_RADAR_AZ9010_JB"}} 
'''  
#返回dict类型: twitter = {'city': city,'temp': temperature}  
def getCityWeather_RealTime(cityID):  
    url = "http://www.weather.com.cn/data/sk/" + str(cityID) + ".html"  
    try:  
        req=urllib2.Request(url)  
        stdout = urllib2.urlopen(url)  
        weatherInfomation = stdout.read().decode('utf-8')          
          
        msg={}  
        msg['city']=weatherInfomation.split('"''"')[5] 
        msg['temp']=weatherInfomation.split('"')[13]  
        msg['wind']=weatherInfomation.split('"''"')[17]+' '+weatherInfomation.split('"')[21]  
        msg['sd']=weatherInfomation.split('"''"')[25] 
        msg['time']=weatherInfomation.split('"')[33]  
          
    except (SyntaxError) as err:  
        print(">>>>>> SyntaxError: " + err.args)  
    except:  
        print(">>>>>> OtherError: ")  
    else:  
        return msg  
    finally:  
        None  
          
def getCityCodeFromName(cityName):  
    for item in cityList_main:  
        #n = unicode(item['name'],'utf-8')  
        #print n,cityName  
        if unicode(item['name'],'utf-8')==cityName:  
            #print 'equal'  
            return item['code']  
    return ''  
  
def convertName(cityName):  
    #将 “浙江省杭州市” 转换成“杭州”   
    #print 'convertName:',cityName  
    name = unicode(cityName, "gbk")  
      
    if name.find(u"省") !=-1:# 包含'省'   
        #print u'有省'  
        name=name.split(u'省')[1]  
    if name.find(u"市") != -1:#包含‘市’  
        #print u'有市'  
        name=name.split(u'市')[0]  
    return name  