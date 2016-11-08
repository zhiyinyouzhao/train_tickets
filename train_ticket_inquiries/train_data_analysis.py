#!/usr/bin/env python
#coding=utf-8

from prettytable import PrettyTable

class info_analysis(object):
	# 显示车次、出发/到达站、 出发/到达时间、历时、商务、特等、一等坐、二等坐、高级软卧、软卧、硬卧、软座、硬座、无座
	header = '车次 出发站/到达站 出发时间/到达时间 历时 商务座 特等座 一等座 二等座 高级软卧 软卧 硬卧 软座 硬座 无座'.split()
	def __init__(self,rows):
		self.rows = rows
	#获取车次时间
	@property
	def trains_info(self):
		for row in self.rows:
			#车次
			number = row['station_train_code']
			#出发/到达站
			station ='\n'.join([row['start_station_name'],row['end_station_name']])
			#出发/到达时间
			time ='\n'.join([row['start_time'],row['arrive_time']])
			#历时
			duration = row['lishi']
			#商务
			business = row['swz_num']
			#特等座
			special = row['yb_num']
			#一等座
			first = row['zy_num']
			#二等座
			second = row['ze_num']
			#高级软卧
			highsoft = row['gr_num']
			#软卧
			soft = row['rw_num']
			#硬卧
			hard_sleep = row['yw_num']
			#软座
			soft_sit = row['rz_num']
			#硬座
			hard_sit = row['yz_num']
			#无座
			nosit = row['wz_num']
			train_list = [number,station,time,duration,business,special,first,second,highsoft,soft,hard_sleep,soft_sit,hard_sit,nosit]
			yield train_list
	#美化显示数据
	def pretty_table(self):
		#设置每列标题
		pt = PrettyTable()
		pt._set_field_names(self.header)
		for train in self.trains_info:
			pt.add_row(train)
		print pt
