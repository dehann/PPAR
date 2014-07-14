import time
import sys
import json
import lcm
from ppar import msg_t

with open(sys.argv[1], 'r') as my_file:
    jsonFileContent = json.load(my_file)
    #print(my_file.read())
    my_file.close()
    print "Data loaded from " + str(sys.argv[1])
   
#json_data=open('../data/example.json')
#jsonFileContent = json.load(json_data)
#json_data.close()
#print "Data loaded from example.json"

pubchannel = ""

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
    global pubchannel
    lc.publish(pubchannel, old.encode())

def my_handler(channel, data):
    msg = msg_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("   timestamp   = %s" % str(msg.utime))
    print(" INTERFACE VER = %s" % str(msg.RE_VERSION))
    print("   random ID   = %s" % str(msg.requeID))
    print("   reqOrig     = %s" % str(msg.requeOrig))
    print("   request     = %s" % str(msg.datastr))
    print("")
    reqstr = str(msg.datastr)
    if (msg.RE_VERSION == 1):
        result = str(getFromJsonFile(reqstr))
        sendReplyMsg(msg, result)

subchannel = getFromJsonFile("[\"ppar\"][\"lcm\"][\"request-channel\"]")
pubchannel = getFromJsonFile("[\"ppar\"][\"lcm\"][\"reply-channel\"]")

lc = lcm.LCM()
subscription = lc.subscribe(subchannel, my_handler)

print "Subscribed to : " + subchannel
print "Reply channel set to : " + pubchannel

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)


