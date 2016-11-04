'''
Created by auto_sdk on 2016.10.20
'''
from top.api.base import RestApi
class LogisticsAddressReachableFeedbackRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param_address_reachable_feedback_top_request = None

	def getapiname(self):
		return 'taobao.logistics.address.reachable.feedback'
