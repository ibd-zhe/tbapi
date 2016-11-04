class MailLogic:
    """
    * 这一个mail的特点是,一个快递单号,一个地址和收货人
    * order number does not matter, what matter is real product
    * mail_info {'useinfo':   {'user_id': str},
                 'orderinfo': [{'number': int,
                                'time': str,
                                'state': str,
                                'seller_note': str,
                                'buyer_note': str
                                'items': [{'itemid': int,
                                           'color': str,
                                           'tsc': str,
                                           'q': int,
                                           'px': float,
                                           'title: str,
                                           'state': str,
                                         }]
                              }]
                }

    * 目的, 决定是否打印这组订单
    """
    def __init__(self, mail_info, invsrc, ordsrc):
        self.mail_info = mail_info
        self.invsrc = invsrc
        self.ordsrc = ordsrc

    def start(self):
        if self.should_pass:
            print 'pass'
            return
        else:



    def start1(self):
        if self.is_refunded:
            print("refund")
        elif self.printed:
            print('already printed')
        else:
            if len([i for i in self.items_response if i['state'] in exit_state]) == 0:
                if len([i for i in self.items_response if i['shipable']]) == len(self.items_response):
                    if self.find_gendan(self.items_response):
                        self.selected()
                else:
                    self.process_unshiped(self.items_response)
            else:
                unshiped = [i for i in self.items_response if i['state'] not in exit_state]
                self.process_unshiped(unshiped)

    @property
    def should_pass(self):
        return self.is_refunded or self.printed or self.successed

    @property
    def is_refunded(self):
        return False

    @property
    def printed(self):
        return False

    @property
    def successed(self):
        return False

class ItemLogic: