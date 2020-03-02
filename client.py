from kafka import KafkaConsumer
import threading



class consumer1(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        consumer1 = KafkaConsumer('LPR_test',
                          group_id='my-group',
                          bootstrap_servers=['localhost:9092'])
        for msg in consumer1:
            with open("image1.png","wb") as f:
                f.write(msg.value)

class consumer2(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        consumer2 = KafkaConsumer('LPR_test',
                          group_id='my-group',
                          bootstrap_servers=['localhost:9092'])
        for msg in consumer2:
            with open("image2.png","wb") as f:
                f.write(msg.value)

if __name__ == '__main__':

    t1 = consumer1()
    t2 = consumer2()
    t1.start()
    t2.start()
