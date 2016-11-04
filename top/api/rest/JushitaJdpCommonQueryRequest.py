'''
Created by auto_sdk on 2014.12.10
'''
from top.api.base import RestApi
class JushitaJdpCommonQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.cmd_name = None
		self.params = None

	def getapiname(self):
		return 'taobao.jushita.jdp.common.query'
