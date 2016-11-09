## 项目说明: 
		该工具用来查询火车票余票信息，所有数据据均来自铁道部官网12306.
## 安装说明：
		cd /opt
		git clone git@github.com:zhiyinyouzhao/train_tickets.git
		cd train_tickets.git
		python setup.py install
## 使用说明：
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
    				tickets 上海 北京 2016-11-09
## 输出结果：
        +------+---------------+-------------------+-------+-----  ---+--------+--------+--------+----------+------+------+------+
		| 车次 | 出发站/到达站 | 出发时间/到达时间 |  历时 | 商务座 | 特等座 | 一等座 | 二等座 | 高级软卧 | 软卧 | 硬卧 | 软座 | 硬座 | 无座 |
		+------+---------------+-------------------+-------+--------+--------+--------+--------+----------+------+------+------+------+------+
		| G102 |    上海虹桥   |       06:39       | 05:39 |   13   |   --   |   38   |  327   |    --    |  --  |  --  |  --  |  --  |  --  |
		|      |     北京南    |       12:18       |       |        |        |        |        |          |      |      |      |      |      |
		| G104 |    上海虹桥   |       06:53       | 05:30 |   21   |   --   |  120   |  368   |    --    |  --  |  --  |  --  |  --  |  --  |
		|      |     北京南    |       12:23       |       |        |        |        |        |          |      |      |      |      |      |
		|  G6  |    上海虹桥   |       07:00       | 04:55 |   无   |   --   |   无   |   7    |    --    |  --  |  --  |  --  |  --  |  --  |
		|      |     北京南    |       11:55       |       |        |        |        |        |          |      |      |      |      |      |
		| G106 |    上海虹桥   |       07:10       | 05:32 |   1    |   --   |   无   |  127   |    --    |  --  |  --  |  --  |  --  |  --  |
		|      |     北京南    |       12:42       |       |        |        |        |        |          |      |      |      |      |      |
		| G108 |    上海虹桥   |       07:20       | 05:51 |   21   |   --   |   74   |  382   |    --    |  --  |  --  |  --  |  --  |  --  |

        
## 个人小结：
		1.火车票站点信息的保存,站名用{拼音:代号}会不准确，因为拼音有重复。
		所以用{中文:代号}的字典保存形式比较科学。例如，'西安北':‘EAY’。
		2.正则抓取站名时,python2的环境下输出是unicode，需要得到中文比较麻烦。
		3.stations.py 里面的字典station格式不好看，由于unicode转中文的缘故，
		pprint美化输出不成功。
		4.列车信息是Json格式的，解析时需要小心观察。
		5.在查不到数据或者票已经售完的情况下，r.json()会返回错误，需要处理这种情况。
		6.stations.py里的字典数据是station_data.py输出重定向得到的。
		7.预售期按照铁道部最新规定，设定为30天。
