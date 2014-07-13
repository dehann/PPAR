import time
import json
import lcm
from ppar import msg_t


json_data=open('../data/example.json')
jsonFileContent = json.load(json_data)
json_data.close()
print "Data loaded from example.json"

def getFromJsonFile(reqstr):
    global jsonFileContent
    return eval("jsonFileContent" + reqstr)

def sendReplyMsg(old, result):
    old.utime = int(time.time() * 1000000)
    old.reqOrig = "pparService.py"
    old.str = result
    global lc
    lc.publish("PPAR_REPLY_MSIM", old.encode())

def my_handler(channel, data):
    msg = msg_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("   timestamp   = %s" % str(msg.utime))
    print("   random ID   = %s" % str(msg.reqRndID))
    print("   reqOrig     = %s" % str(msg.reqOrig))
    print("   request     = %s" % str(msg.str))
    print("")
    reqstr = str(msg.str)
    result = str(getFromJsonFile(reqstr))
    sendReplyMsg(msg, result)

lc = lcm.LCM()
subscription = lc.subscribe("PPAR_REQUEST_MSIM", my_handler)
print "Subscribed to : PPAR_REQUEST_MSIM"

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)


