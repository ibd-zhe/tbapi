'''
Created by auto_sdk on 2016.02.17
'''
from top.api.base import RestApi
class WlbWaybillIDistributeinfoRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.waybill_distribute_info_request = None

	def getapiname(self):
		return 'taobao.wlb.waybill.i.distributeinfo'
