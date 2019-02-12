import redis


class Pubsub():
    def __init__(self):
        self.conn = redis.Redis(host="localhost", port=6379)
        self.channel = "mointor"

    def puber(self,msg):
        self.conn.publish(self.channel, msg)
        return True

    def suber(self):
        s = self.conn.pubsub()
        s.subscribe(self.channel)
        s.parse_response()
        return s
