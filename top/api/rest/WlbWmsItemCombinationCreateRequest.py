'''
Created by auto_sdk on 2016.05.17
'''
from top.api.base import RestApi
class WlbWmsItemCombinationCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.sub_item_list = None

	def getapiname(self):
		return 'taobao.wlb.wms.item.combination.create'
