# RabbitMQ Demo
```
   $ docker-compose up -d mq # RabbitMQ
   $ docker-compose up consumer-1 # Consumer service 1. writes to consumer/mq.log
   $ docker-compose up consumer-2 # Consumer service 2. writes to consumer/mq.log
   $ dcoker-compose run producer # Producer service. Reads from stdin
```
