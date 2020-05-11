#!/usr/bin/env python3

import pika

HOST = 'mq'

# Connect
con = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = con.channel()
print('Connected.')

# Create a queue
channel.queue_declare(queue='foo')

try:
    while True:
        str = input("Type something (ctrl+c to quit): ")
        channel.basic_publish(exchange='',
                              routing_key='foo',
                              body=str)
except KeyboardInterrupt:
    channel.close()
    print('Done.')
