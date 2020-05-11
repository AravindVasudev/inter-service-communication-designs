#!/usr/bin/env python3

import pika

HOST = 'mq'

# Connect
con = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = con.channel()
print('Connected.')

# Create a fanout exchange
channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

try:
    while True:
        msg = input("Type something (ctrl+c to quit): ")
        channel.basic_publish(exchange='pubsub',
                              routing_key='',
                              body=msg)
except KeyboardInterrupt:
    channel.close()
    print('Done.')
