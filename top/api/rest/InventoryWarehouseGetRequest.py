'''
Created by auto_sdk on 2016.07.07
'''
from top.api.base import RestApi
class InventoryWarehouseGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.store_code = None

	def getapiname(self):
		return 'taobao.inventory.warehouse.get'
