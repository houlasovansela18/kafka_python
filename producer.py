from kafka import KafkaProducer

class producer:

    def __init__(self):
        self.image_path = "image.jpeg"

    def run(self):
        with open(self.image_path,"rb") as f:
            data = f.read()
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        future = producer.send('LPR_test',data)
        result = future.get(timeout=60)
        print(result)

if __name__ == '__main__':

    p = producer()
    p.run()
