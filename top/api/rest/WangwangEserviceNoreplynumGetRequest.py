'''
Created by auto_sdk on 2014.03.18
'''
from top.api.base import RestApi
class WangwangEserviceNoreplynumGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.service_staff_id = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.wangwang.eservice.noreplynum.get'
