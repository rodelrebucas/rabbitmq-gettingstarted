## Getting started with RabbitMQ

Terms:

A **producer** is a user application that sends messages.

A **queue** is a buffer that stores messages.

A **consumer** is a user application that receives messages.

---

A. **RabbitMQ is a message broker** so it can receive and forward messages.

_Relationship_ - one producer sends message and received by one consumer.

1. Start the receiver with: `python receive.py`

2. Send message to the `hello` queue with: `python send.py`

B. **RabbitMQ as worker queues** - pass time consuming task to multiple workers.

_Relationship_ - one producer sends message and received|processed by one consumer out of the multiple consumers.

- Messages are pass using round robin.
- Prevent message loss when consumer dies by turning on message acknowledgements.
- Make the message survive on restarts and crashes with `durable` option on consumer and `deliver_mode=2` on producer

1. Run multiple workers by running `worker.py` in different terminals

2. Send task with `python new_task.py task`

C. **RabbitMQ as PubSub** - passing all messages not just a subset to multiple consumers is called publish/subscribe.

_Relationship_ - one producer sends message and received by all subscribed consumers.

1. Run consumer `python receive_logs.py`.

2. Run producer `python emit_log.py`.

---

Tutorial References are in _https://www.rabbitmq.com/getstarted.html_
