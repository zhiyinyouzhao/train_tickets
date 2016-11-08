#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# author = "Mr zn"  
# date  = "2016/10/8"
import sys
import requests
import re 
import json
#获取车站信息
def station_info():
	#车站实际存储页面
	station_url='https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8969'
	#抓取页面信息
	headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",	
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",    "Accept-Encoding":"gzip, deflate, sdch",	
	"Accept-Language":"zh-CN,zh;q=0.8",	"Cache-Control":"max-age=0",	
	"Connection":"keep-alive"}
	r = requests.get(station_url,headers=headers,verify=False)
	#正则匹配站点信息
	stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', r.text)
	#将unicode转为中文
	string=json.dumps(dict(stations),ensure_ascii=False)+"\n";
	string=unicode.encode(string,'utf-8')
	print string
station_info()



