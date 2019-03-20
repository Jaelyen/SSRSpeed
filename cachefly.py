#coding:utf-8
#Author:ranwen NyanChan

import time
import socket
import logging
logger = logging.getLogger("Sub")

def pingtcptest(host,port):
	alt=0
	suc=0
	fac=0
	while suc<5 and fac<5:
		try:
			s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			st=time.time()
			s.settimeout(3)
			s.connect((host,port))
			s.close()
			alt+=time.time()-st
			suc+=1
		except Exception as err:
			logger.exception("TCP Ping Exception:")
			fac+=1
	if suc==0:
		return (0,0)
	return (alt/suc,suc/(suc+fac))

def pinggoogletest(port=1080):
	alt=0
	for i in range(0,2):
		try:
			s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(10)
			s.connect(("127.0.0.1",port))
			st=time.time()
			s.send(b"\x05\x01\x00")
			s.recv(2)
			s.send(b"\x05\x01\x00\x03\x0agoogle.com\x00\x50")
			s.recv(10)
			s.send(b"GET / HTTP/1.1\r\nHost: google.com\r\nUser-Agent: curl/11.45.14\r\n\r\n")
			s.recv(1)
			s.close()
			alt+=time.time()-st
		except Exception as err:
			logger.exception("Google Ping Exception:")
			alt+=10000
	return alt/2
