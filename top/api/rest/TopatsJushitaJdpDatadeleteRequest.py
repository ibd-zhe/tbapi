'''
Created by auto_sdk on 2016.10.31
'''
from top.api.base import RestApi
class TopatsJushitaJdpDatadeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.start_date = None
		self.sync_types = None
		self.user_nick = None

	def getapiname(self):
		return 'taobao.topats.jushita.jdp.datadelete'
