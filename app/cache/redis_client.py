import redis

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def cache_response(key, value):
    redis_client.setex(key, 3600, value)

