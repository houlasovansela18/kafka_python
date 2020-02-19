from kafka import KafkaConsumer

consumer = KafkaConsumer('LPR')
for msg in consumer:
    print (msg.value)
