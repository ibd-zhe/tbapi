'''
Created by auto_sdk on 2016.03.05
'''
from top.api.base import RestApi
class WlbOrderConsignRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.wlb_order_code = None

	def getapiname(self):
		return 'taobao.wlb.order.consign'