import time

import pika

import config


def on_message(channel, method_frame, header_frame, body):
    print(f"Consumer : received {body.decode()}")


def main():
	while True:
		try:
			params = pika.ConnectionParameters('rabbit', config.RABBITMQ_PORT)
			connection = pika.BlockingConnection(params)
			channel = connection.channel()
			channel.queue_declare(queue=config.QUEUE_NAME)

			channel.basic_consume(on_message, queue=config.QUEUE_NAME)
			channel.start_consuming()
		except pika.exceptions.ConnectionClosed:
			print('Consumer : something went wrong, restarting...')
			time.sleep(1)




if __name__ == '__main__':
	main()
