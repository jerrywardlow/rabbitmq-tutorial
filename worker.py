#!/usr/bin/python
import time
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, proeprties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='hello')

print(' [*] Waiting for messages, ditch with Ctrl-C')
channel.start_consuming()
