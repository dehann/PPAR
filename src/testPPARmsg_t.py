import lcm
import time

from ppar import msg_t

lc = lcm.LCM()

msg = msg_t()
msg.utime = int(time.time() * 1000000)
msg.RE_VERSION = 1
msg.requeID = 1
msg.requeOrig = "testPPARmsg_t.py"

msg.datastr = "['constants']['earth']['gravity']"
#msg.datastr = "['plots'][1]['signals'][0]['channel']"
#msg.datastr = "['sensors']['microstrain']['dt']"
#msg.datastr = "['other']"

lc.publish("PPAR_REQUEST_EXAMPLE", msg.encode())
