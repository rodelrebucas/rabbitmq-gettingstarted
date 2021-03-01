import pika, sys


# Connect to a broker (localhost).
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()

# Exchange - the one responsible for receiving message from the producer and pushing
# that message to the queue.
# Fanout - the exchange type  when we want to broadcast the message
# to the queues the channel knows.
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

# Severity as routing_key as first parameter
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'

# create log message from the command line as 2nd parameter
message = " ".join(sys.argv[2:]) or "Hello World!"

# Publish to the named exchange not to a default exchange.
# routing_key value is ignored when using fanout exchange.
channel.basic_publish(exchange="direct_logs", routing_key=severity, body=message)


# Notify that message was sent
print(f"{message} was sent to. routing_key {severity}")

# Close the connection and network buffers.
connection.close()
