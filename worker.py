#!/usr/bin/python
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch, method, proeprties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")

channel.basic_consume(callback,
                      queue='hello',
                       no_ack=True)

print(' [*] Waiting for messages, ditch with Ctrl-C')
channel.start_consuming()
