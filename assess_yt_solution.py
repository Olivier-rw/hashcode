import sys

video_count = 0
endpoint_count = 0
request_descriptions = 0

cache_count = 0
cache_capacity = 0
video_sizes = []

endpoint_to_server = []#list of latencies
endpoint_caches = []# list of dictionaries, each dictionary maps cache ids to latencies
endpoint_requests = []# list of list of tuples, where each tuple is a video, #of requests pair
request_sum = 0

def understand_problem(fileName):
    global video_count, endpoint_count, request_descriptions, cache_count, cache_capacity, video_sizes, \
        endpoint_to_server, endpoint_caches, endpoint_requests, request_sum

    with open(fileName, 'r') as problem:
        data = list(map(lambda x: int(x), problem.readline().split(' ')))
        video_count = data[0]
        endpoint_count = data[1]
        request_descriptions = data[2]
        cache_count = data[3]
        cache_capacity = data[4]

        video_sizes = list(map(lambda x: int(x), problem.readline().split()))


        for i in range(endpoint_count):
            endpoint_data = list(map(lambda x: int(x), problem.readline().split(' ')))
            endpoint_to_server.append(endpoint_data[0])
            cache_dict = {}
            for j in range(endpoint_data[1]):
                cache_data = list(map(lambda x: int(x), problem.readline().split(' ')))
                cache_dict[cache_data[0]] = cache_data[1]
            endpoint_caches.append(cache_dict)

        for i in range(endpoint_count): endpoint_requests.append([])

        for i in range(request_descriptions):
            request_data = list(map(lambda x: int(x), problem.readline().split(' ')))
            video_id = request_data[0]
            endpoint_id = request_data[1]
            request_count = request_data[2]
            request_sum += request_count
            endpoint_requests[endpoint_id].append((video_id, request_count))


def score_solution(solution):
    score = 0
    for endpoint_id, request_data in enumerate(endpoint_requests):
        # get the caches for this endpoint
        # see if the solution says anything about them
        # if it does, check if the videos we want are in there
        # if so, compute the time gained.
        cache_latencies = endpoint_caches[endpoint_id]
        relevant_caches = set(cache_latencies.keys()).intersection(set(solution.keys()))

        if relevant_caches is None: continue

        for request in request_data:
            video_id = request[0]
            best_performance = sys.maxsize

            for cache in relevant_caches:
                if solution[cache].__contains__(video_id):
                    best_performance = min(best_performance, endpoint_caches[endpoint_id][cache])

            if best_performance != sys.maxsize:
                time = (endpoint_to_server[endpoint_id]-best_performance)
                score += request[1]*time*1000

    return score / request_sum


def validate_submission(fileName):
    with open(fileName, 'r') as output:
        # Read the first line, is it a number?
        cache_number = output.readline()
        try:
            cache_number = int(cache_number)
        except ValueError:
            print("Invalid first line: must be a number")

        assert cache_number <= cache_count, "Solution uses more caches than allowed"

        cache_info = output.readlines()

        # Do we have the correct number of lines?
        assert cache_number == len(cache_info), "Number of cache lines did not match stated cache count"

        solution = {}

        for info in cache_info:
            try:
                int_results = list(map(lambda x: int(x), info.split(' ')))
                memory_required = sum(list(map(lambda x: video_sizes[x], int_results[1:])))
                assert cache_capacity >= memory_required, "exceeded cache capacity in entry" + str(info)
            except ValueError:
                print("Some value in cache info is not convertible to an int")

            solution[int_results[0]] = set(int_results[1:])

        return solution

if __name__ == '__main__':
    problem_file = input("What's the name of the problem file?")
    solution_file = input("What's the name of your solution file?")

    print("learning about the problem")
    understand_problem(problem_file)
    print("validating the solution")
    result = validate_submission(solution_file)
    print("scoring")
    print(score_solution(result))