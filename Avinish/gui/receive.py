import pika
import time
import gaze_dnn
import multiprocessing
from threading import Thread
import sys
# t = Thread(target=drowsiness.track() )
# t.daemon = True
# t.start()
# t.join()


class alert(Thread):
    def run(self):
        self.connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()

        self.channel.queue_declare(queue='hello')
        self.channel.queue_declare(queue='website')


        def callback(ch, method, properties, body):
            print(" [x] Received {} {}".format(body,time.time()), flush=True)


        self.channel.basic_consume(
            queue='website', on_message_callback=callback, auto_ack=True)


        self.channel.basic_consume(
            queue='drowsiness', on_message_callback=callback, auto_ack=True)


        print(' [*] Waiting for messages. To exit press CTRL+C', flush=True)
        self.channel.start_consuming()
    def stop(self):
        self.channel.stop_consuming()
        self.connection.close()



