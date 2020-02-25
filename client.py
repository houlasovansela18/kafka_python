from kafka import KafkaConsumer

consumer = KafkaConsumer('LPR')
for msg in consumer:
    with open("image.png","wb") as f:
        f.write(msg.value)
