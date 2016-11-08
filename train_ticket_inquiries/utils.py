#!/usr/bin/env python
#coding=utf-8
import re
import datetime
from stations import station
#判断日期年，月，日是否合法
def date_vaild(date):
	new_date = date.split('-')
	y = int(new_date[0])
	m = int(new_date[1])
	d = int(new_date[2])
	try:
		datetime.date(y,m,d)
		return True
	except:
		print '你输入的日期非法，请输入合法的日期'
		return False
#判断日期是否符合xxxx-xx-xx的日期格式
def date_format(date):
	result = re.match(r'\d{4}-\d{2}-\d{2}',date)
	if result:
		return True
	else:
		print '你输入的日期格式不对，请输入xxxx-xx-xx的日期格式'
		return False
#比较日期，以前的日期无法查到数据,12月30日后，预售票日期调整为30天。
def date_scope(date):
	#获取今天的日期
	now = datetime.datetime.now()
	today = now.strftime('%Y-%m-%d')
	deadline_date = now + datetime.timedelta(days=30)
	deadline_date = deadline_date.strftime('%Y-%m-%d')
	if date <= deadline_date and date >= today:
		return True
	else:
		print '你输入的日期不对，请输入预售票期间的日期。当前预售期为：%s至%s' % (today,deadline_date)
		return False
#检查输入的车站是否合法
def station_vaild(from_station,to_station):
	if from_station in station and to_station in station:
		return True
	else:
		print '你输入的车站不存在，请确认后输入。'
		return False



