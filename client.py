from kafka import KafkaConsumer
import threading



class consumer1(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        k = 0
        consumer1 = KafkaConsumer('test5',
                          group_id='my-group',
                          bootstrap_servers=['localhost:9092'])
        for msg in consumer1:
            k+=1
            with open("detection_frame/demo1/image"+str(k)+".png","wb") as f:
                f.write(msg.value)

class consumer2(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        k = 0
        consumer2 = KafkaConsumer('test5',
                          group_id='my-group',
                          bootstrap_servers=['localhost:9092'])
        for msg in consumer2:
            k+=1
            with open("detection_frame/demo2/image"+str(k)+".png","wb") as f:
                f.write(msg.value)

class consumer3(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        k = 0
        consumer3 = KafkaConsumer('test5',
                          group_id='my-group',
                          bootstrap_servers=['localhost:9092'])
        for msg in consumer3:
            k+=1
            with open("detection_frame/demo3/image"+str(k)+".png","wb") as f:
                f.write(msg.value)

class consumer4(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        k = 0
        consumer4 = KafkaConsumer('test5',
                          group_id='my-group',
                          bootstrap_servers=['localhost:9092'])
        for msg in consumer4:
            k+=1
            with open("detection_frame/demo4/image"+str(k)+".png","wb") as f:
                f.write(msg.value)

class consumer5(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        k = 0
        consumer5 = KafkaConsumer('test5',
                          group_id='my-group',
                          bootstrap_servers=['localhost:9092'])
        for msg in consumer5:
            k+=1
            with open("detection_frame/demo5/image"+str(k)+".png","wb") as f:
                f.write(msg.value)

if __name__ == '__main__':

    t1 = consumer1()
    t2 = consumer2()
    t3 = consumer3()
    t4 = consumer4()
    t5 = consumer5()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
