from kafka import KafkaProducer

with open("image.jpeg","rb") as f:
    data = f.read()
producer = KafkaProducer(bootstrap_servers='localhost:9092')
future = producer.send('LPR',data)
result = future.get(timeout=60)
print(result)
