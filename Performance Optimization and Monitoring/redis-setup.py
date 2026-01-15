import redis

r = redis.Redis(host='localhost', port=6379, db=0) #to connect to redis server

try:
    if r.ping():
        print('Connected to Redis!')
except redis.ConnectionError:
    print('Redis connection failed!')


r.set('framework', 'FastAPI') #randomly trying it is an key value pair 

value = r.get('framework') #retrieves values
print(f"Stored value for framework: {value.decode()}") #convert bytes to readable string