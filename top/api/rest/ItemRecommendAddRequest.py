'''
Created by auto_sdk on 2016.08.18
'''
from top.api.base import RestApi
class ItemRecommendAddRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.num_iid = None

	def getapiname(self):
		return 'taobao.item.recommend.add'
