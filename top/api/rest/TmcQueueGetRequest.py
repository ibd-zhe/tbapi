'''
Created by auto_sdk on 2016.03.03
'''
from top.api.base import RestApi
class TmcQueueGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.group_name = None

	def getapiname(self):
		return 'taobao.tmc.queue.get'
