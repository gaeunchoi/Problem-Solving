from collections import deque
def solution(cacheSize, cities):
    cache = deque()
    cache_set = set()
    time = 0
    
    for city in cities:
        city = city.lower()

        if city in cache:
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            time += 5
            if cacheSize > 0:
                if len(cache) == cacheSize:
                    old = cache.popleft()
                    cache_set.remove(old)
                cache.append(city)
                cache_set.add(city)

    return time