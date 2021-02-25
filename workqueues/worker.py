import pika, os, sys, time



def main():
    # Connect to a broker (localhost).
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()

    # Create the queue where the message should be delivered.
    # Idempotent declaration - doesn't matter how many times
    # we execute 'queue_declare' it will return the same result.
    # We make sure queue exists before receiving messages.
    # So we need to declare it again.
    channel.queue_declare(queue="hello")


    # Use this callback to handle incoming messages
    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")
        print(f" [x] Received decoded body {body.decode()}")
        print(f" [x] Done in {body.count(b'')}")

        # Fake long task
        time.sleep(body.count(b''))
        print("Done")

        # Turn on message acknowledgements
        # All unacknowledge messages will be re-delivered
        ch.basic_ack(delivery_tag = method.delivery_tag)

    # Subscribe the callback to `hello` queue
    channel.basic_consume(queue="hello", on_message_callback=callback)

    # Listen for incoming messages
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)