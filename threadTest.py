# -*- coding=utf-8 -*-
from config.emailConf import sendEmail
from init import select_ticket_info
import thread
import time
import ronie.logger


def run():
    ronie = Ronie("99")
    ronie.post("t1")
    thread.start_new_thread(ronie.post, ("a1",))
    thread.start_new_thread(ronie.post, ("a2",))
    ronie.post("t2")

def Email():
    sendEmail(u"订票小助手测试一下")



class Ronie:
    def __init__(self,id):
        self.id = id

    def post(self, name):
        ronie.logger.log(name + " : id=" + self.id)
        ronie.logger.log(name + " : start")
        time.sleep(3)
        ronie.logger.log(name + " : done")




if __name__ == '__main__':
    run()
    # Email()