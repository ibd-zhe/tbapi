'''
Created by auto_sdk on 2016.01.26
'''
from top.api.base import RestApi
class JushitaJdpRdsinfoGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.target_appkey = None

	def getapiname(self):
		return 'taobao.jushita.jdp.rdsinfo.get'
