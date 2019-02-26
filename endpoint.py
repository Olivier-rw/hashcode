class Endpoint:

    def __init__(self, d_latency):
        self.d_latency = d_latency
        self.caches = {}
        self.video_requests = {}

class Cache:
    def __init__(self, video):
        self.videos = []
