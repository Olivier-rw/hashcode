class Endpoint:

    def __init__(self, d_latency):
        self.d_latency = d_latency
        self.caches = {}
        self.video_requests = {}
        self.new_set = set(self.video_requests.values())

class Cache:
    def __init__(self, size):
        self.size = size
        self.videos = []
