from endpoint import Endpoint
f = open('final_practice.txt', 'r')
first_line = f.readline().split()
t_videos, t_endpoints, t_request, t_caches, c_capacity = list(map(int, first_line))
print(t_videos, t_endpoints, t_request, t_caches, c_capacity)

v_sizes = list(map(int, f.readline().split()))
print(v_sizes)
endpoints = []
cashes_list = []
for i in range(t_endpoints):
    temp = list(map(int, f.readline().split()))
    temp_object = Endpoint(temp[0])
    for x in range(temp[1]):
        temp2 = list(map(int, f.readline().split()))
        temp_object.caches[temp2[0]] = temp2[1]

    endpoints.append(temp_object)

# for x in endpoints:
#     print(x.d_latency, len(x.caches))
#     print(x.caches)
for v in range(t_request):
    request = list(map(int, f.readline().split()))
    curr_endpoint = endpoints[request[1]]
    if request[0] in curr_endpoint.video_requests.keys():
        curr_endpoint.video_requests[request[0]] += request[2]
    else:
        curr_endpoint.video_requests[request[0]] = request[2]

# for x in endpoints:
#     print(x.video_requests)

