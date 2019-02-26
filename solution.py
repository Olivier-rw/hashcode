from endpoint import Endpoint, Cache

f = open('final_practice.txt', 'r')
first_line = f.readline().split()
t_videos, t_endpoints, t_request, t_caches, c_capacity = list(map(int, first_line))
print(t_videos, t_endpoints, t_request, t_caches, c_capacity)

v_sizes = list(map(int, f.readline().split()))
print(v_sizes)
endpoints = []
cashes_list = []

for i in range(t_caches):
    cashes_list.append(Cache(c_capacity))

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

for x in endpoints:
    highest_requests = list(x.video_requests.values())
    for i in x.video_requests:
        if len(highest_requests) != 0:
            if x.video_requests[i] == max(highest_requests):
                if v_sizes[i] <= c_capacity:
                    tempppp = list(x.caches.keys())
                    print(tempppp)
                    if len(x.caches) != 0 and (i not in set(cashes_list[tempppp[0]].videos)):

                        cashes_list[tempppp[0]].size -= v_sizes[i]
                        cashes_list[tempppp[0]].videos.append(i)

count = 0
for x in cashes_list:
    if x.size != c_capacity:
        count += 1

    print(x.videos)

output = open("output.txt", "a")
output.write(str(count) + '\n')

for x in range(len(cashes_list)):
    output.write(str(x) + ' ' + ' '.join(str(i) for i in cashes_list[x].videos) + '\n')
    



