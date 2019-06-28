from pythonping import ping
import datetime


""" subnet = "192.162.1."
for ip in range(1,254):
    dest = subnet+ip
    pingresponse = ping(target=dest, timeout=2)
    print(pingresponse.rtt_avg_ms) """

pingresponse = ping('192.162.1.1', timeout=2)
print(pingresponse.rtt_avg_ms)
