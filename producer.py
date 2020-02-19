from kafka import KafkaProducer
import json
import cv2

img = cv2.imread('image.jpeg',0)
producer = KafkaProducer(bootstrap_servers='localhost:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))
future = producer.send('LPR', {'foo': str(img)})
result = future.get(timeout=60)
print(result)
