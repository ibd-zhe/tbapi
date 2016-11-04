import top
import psycopg2
import codecs
import sys
import math

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)


class GetInv:
    def __init__(self):
        top.setDefaultAppInfo("21206983", "2b7aa50061dcc3aba1a5777b55d89085")
        self.session = '6201812c38514ee9fddace5eeZZee6f8aee063af7653a82894689296'

    def start(self):


    def insert_all_itemid(self):

    def get_all_itemid(self):
        page_size =200
        items_on_sale = top.api.ItemsOnsaleGetRequest()
        items_on_sale.fields = 'num_iid'
        items_on_sale.page_size = page_size
        first_r = items_on_sale.getResponse(self.session)

        total = first_r['items_onsale_get_response']['total_results']
        items_id = [i['num_iid'] for i in first_r['items_onsale_get_response']['items']['item']]
        total_page = math.floor(total/page_size)
        for i in xrange(2, total_page + 1):
            items_on_sale.page_no = i
            items_id.extend([i['num_iid'] for i in items_on_sale.getResponse(self.session)['items_onsale_get_response'][
                'items']['item']])

        return items_id

    



