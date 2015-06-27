#!/usr/bin/python
#coding: utf-8

'''
tsTserv.py (Example 16.1):
	timestamp TCP server (TCP时间戳服务器)
	creating a TCP server:
		creates a TCP server that accepts messages from clents and returns them
	with a timestamp prefix.
'''

from socket import *
from time import ctime

HOST = ''
PORT = 21556
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcpSerSock = socket()	#创建套接字，socket参数取其默认值
tcpSerSock.bind(ADDR)	#绑定套接字到服务器地址
tcpSerSock.listen(5)	#允许同时5个连接

'''
依次处理一个连接
若同时有多个连接请求
只有当当前连接断开后才去处理下一个连接
'''
while True:
	try:
		print 'waiting for connection...'
		tcpCliSock, addr = tcpSerSock.accept()	#阻塞式监听，
				#若有客户端发起连接请求,返回一个代表的连接的套接字和客户端地址
		print  '...connected from:', addr

		while True:
			data = tcpCliSock.recv(BUFSIZ) #等待客户发送数据
			if not data:
				break
			else:
				tcpCliSock.send('[%s] %s' % (ctime(), data)) #返回数据给客户
		tcpCliSock.close()
	except (EOFError, KeyboardInterrupt): #ctrl+d 无反应，why? 
										#ctrl+d正常， 客户端对此异常有反应
		tcpSerSock.close()
		break
