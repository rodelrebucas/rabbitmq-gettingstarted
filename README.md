## Getting started with RabbitMQ

#### A. Receiving and sending messages.

**RabbitMQ is a message broker**, so it can receive and forward messages.

1. Start the receiver with: `python receive.py`

2. Send message to the `hello` queue with: `python send.py`

**RabbitMQ as worker queues** , pass time consuming task to multiple workers.

- Messages are pass using round robin.
- Prevent message loss when consumer dies by turning on message acknowledgements.
- Make the message survive on restarts and crashes with `durable` option on consumer and `deliver_mode=2` on producer

1. Run multilple workers by running `worker.py` in different terminals
2. Send task with `python new_task.py task`

---

Tutorial References are in _https://www.rabbitmq.com/getstarted.html_
