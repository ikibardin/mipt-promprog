import random
import time

import pika

import config


def main():
	while True:
		try:
			params = pika.ConnectionParameters('rabbit', config.RABBITMQ_PORT)
			connection = pika.BlockingConnection(params)
			channel = connection.channel()
			channel.queue_declare(queue=config.QUEUE_NAME)

			while True:
				random_value = random.random()
				channel.basic_publish(exchange='', routing_key=config.QUEUE_NAME, body=str(random_value))
				sleep_duration = random.randint(1, 4)
				
				print(f'Producer : sending  {random_value} and sleeping for {sleep_duration} seconds')
				time.sleep(sleep_duration)
		except pika.exceptions.ConnectionClosed:
			print('Producer : something went wrong, restarting...')
			time.sleep(1)

if __name__ == '__main__':
	main()
