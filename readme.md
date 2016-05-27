# py-ha-decorator
-------
简易的HA方案. 基于zookeeper实现的一个python HA装饰器.

### Note
-------
py-ha-decorator当前版本0.1.0

### Install Package
--------
	$ pip install py-ha-decorator

### Install Dependencies
--------
	$ pip install -r requirements.txt
	
### Usage
--------

适用于nsq consumer的ha, 可以启动两个甚至多个nsq consumer.     
使用时需要指定zookeeper host列表.

代码示例    
demo1.py:
	
	import time
	import pyhadecorator.ha_decorator import HaDecorator
	
	# specified zk hosts
	@HaDecorator("localhost:2181")
	def echo(args):
		print args
		time.sleep(10000)
	
	if __name__ == '__main__':
		echo("test demo 1")
	
demo2.py:

	import time
	import pyhadecorator.ha_decorator import HaDecorator
	
	# specified zk hosts
	@HaDecorator("localhost:2181")
	def echo(args):
		print args
		time.sleep(10000)
	
	if __name__ == '__main__':
		echo("test demo 2")

demo1.py和demo2.py会根据启动顺序, 以master, slave方式运行; 当master挂掉之后, slave会充当master, 继续运行

	$ python demo1.py
	[2016-05-18 17:40:50,950] INFO     Connecting to 192.168.99.100:2181
	[2016-05-18 17:40:50,953] INFO     Zookeeper connection established, state: CONNECTED
	test demo 1
	
	
	$ python demo2.py
	[2016-05-18 17:40:55,354] INFO     Connecting to 192.168.99.100:2181
	[2016-05-18 17:40:55,358] INFO     Zookeeper connection established, state: CONNECTED
	
	### kill demo1.py
	test demo 2


### Bugs
-------
