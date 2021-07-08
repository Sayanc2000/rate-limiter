import redis

client = redis.Redis(host="redis-server")


def limiter(key, limit):
    req = client.incr(key)
    if req == 1:
        client.expire(key, 60)
        ttl = 60
    else:
        ttl = client.ttl(key)
    if req > limit:
        return {
            "call": False,
            "ttl": ttl
        }
    else:
        return {
            "call": True,
            "ttl": ttl
        }
