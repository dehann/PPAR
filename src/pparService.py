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
    try:
        return eval("jsonFileContent" + reqstr)
    except:
        print "Not found in specified json file"
        pass
    return

def sendReplyMsg(old, result):
    old.utime = int(time.time() * 1000000)
    old.replyOrig = "pparService.py"
    old.datastr = result
    global lc
    lc.publish("PPAR_REPLY_MSIM", old.encode())

def my_handler(channel, data):
    msg = msg_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("   timestamp   = %s" % str(msg.utime))
    print("   random ID   = %s" % str(msg.requeID))
    print("   reqOrig     = %s" % str(msg.requeOrig))
    print("   request     = %s" % str(msg.datastr))
    print("")
    reqstr = str(msg.datastr)
    if (msg.RE_VERSION == 1):
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


