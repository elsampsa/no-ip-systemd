#!/usr/bin/python3

"""As per: https://www.noip.com/integrate/request

This is a single-shot program.  Let systemd to restart it over-and-over again.   Define the connection interval in the file noip.service
"""
import urllib3
import base64
http = urllib3.PoolManager()

username   = "user"                # PUT HERE YOUR USERNAME
password   = "passwd"              # PUT HERE YOUR PASSWORD
hostname   = "yourdomain.ddns.net" # PUT HERE YOUR DOMAIN
user_agent = "My Python No-IP agent/1.0 youremail@iki.fi" # PUT HERE YOUR USER AGENT DATA

bs = "%s:%s" % (username, password)
b64 = base64.b64encode(bs.encode("utf-8")) # utf-8 => bytes => base64
auth = "Basic " + b64.decode("ascii") # final string in ascii

headers = {
    "User-Agent"     : user_agent,
    "Authorization"  : auth
    }

st = "https://dynupdate.no-ip.com/nic/update?hostname={HOSTNAME}".format(
    HOSTNAME = hostname)

# print(st)
# print(headers)

r = http.request('GET', st, headers = headers)

print("status:", r.status)
print("data  :", r.data)
