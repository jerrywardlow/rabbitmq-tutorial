#!/usr/bin/python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "Here's your message!"
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" ('_') Sent %r:%r" % (severity, message))
connection.close()
