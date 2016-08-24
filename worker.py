#!/usr/bin/python
import time

def callback(ch, method, proeprties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
