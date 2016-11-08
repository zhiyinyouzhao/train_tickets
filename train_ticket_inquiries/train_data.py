#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# author = "Mr zn" 
# date  = "2016/10/9" 


"""Train tickets query via command-line.

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

Example:
    tickets 上海 北京 2016-08-25
"""
from docopt import docopt
import requests
from stations import station
from train_data_analysis import info_analysis
import datetime
from utils import date_vaild,date_format,date_scope,station_vaild
import re

def click_information():
	arguments = docopt(__doc__)
	from_station = station.get(arguments['<from>'])
	to_station = station.get(arguments['<to>'])
	date = arguments['<date>']
	#判断日期和车站是否合法
	if station_vaild(arguments['<from>'],arguments['<to>']):
		if date_format(date):
			if date_vaild(date):
				if date_scope(date):
					#设置查询余票的url
					url = 'https://kyfw.12306.cn/otn/lcxxcx/query?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(date,from_station,to_station)
					#设置http头信息
					headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",    "Accept-Encoding":"gzip, deflate, sdch",
	"Accept-Language":"zh-CN,zh;q=0.8",    
	"Cache-Control":"max-age=0",
	"Connection":"keep-alive"}
					#获取数据
					try:
						r = requests.get(url,headers=headers,verify=False)
						rows = r.json()['data']['datas']
					except:
						print '无法得到数据，可能票已售完。'
					else:
						#创建类info_analysis的对象
						train_data = info_analysis(rows)
						result = train_data.pretty_table()
						return result 
if __name__ == '__main__':
    click_information()
