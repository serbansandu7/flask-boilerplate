import redis


class RedisEntity:
    def __init__(self, host_name, port_number):
        self.host_name = host_name
        self.port_number = port_number
        self.connection = self.createConnection()

    def createConnection(self) -> redis.client.Redis:
        try:
            client = redis.Redis(
                host=self.host_name,
                port=self.port_number,
                db=0,
                socket_timeout=5,
            )
            ping = client.ping()
            if ping is True:
                return client
        except redis.AuthenticationError:
            print("AuthenticationError")

    def setKey(self, key, value, expire_time):
        self.connection.set(key, value, ex=expire_time)

    def getKey(self, key):
        return self.connection.get(key)