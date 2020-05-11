#!/usr/bin/env python3

import pika

HOST = 'mq'

def callback(ch, method, properties, body):
    with open('mq.log', 'a') as f:
        f.write(str(body, 'utf-8'))

    print("Got: ", body)

# Connect
con = pika.BlockingConnection(pika.ConnectionParameters(HOST))
channel = con.channel()
print('Connected.')

# Create a fanout exchange
channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

# Create the queue
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='pubsub', queue=queue_name)

# Consume
channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

try:
    print('Waiting...')
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()
con.close()
