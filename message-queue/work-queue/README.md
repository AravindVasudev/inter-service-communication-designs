# RabbitMQ Demo
```
   $ docker-compose up -d mq # RabbitMQ
   $ docker-compose up consumer # Consumer service. writes to consumer/mq.log
   $ dcoker-compose run producer # Producer service. Reads from stdin
```
