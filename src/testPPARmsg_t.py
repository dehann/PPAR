import lcm
import time

from ppar import msg_t

lc = lcm.LCM()

msg = msg_t()
msg.utime = int(time.time() * 1000000)
msg.reqRndID = 1
msg.reqOrig = "testPPARmsg_t.py"
msg.str = "[\"plots\"][1][\"signals\"][0][\"channel\"]"

lc.publish("PPAR_REQUEST_MSIM", msg.encode())
