#!/usr/bin/python36

import subprocess
import cgi

print("content-type: text/html")


form = cgi.FieldStorage()

cname = form.getvalue("s")

cmd = "sudo docker start {}".format(cname)

x = subprocess.getoutput(cmd)

print("location: http://192.168.0.12/cgi-bin/run.py")
print()



