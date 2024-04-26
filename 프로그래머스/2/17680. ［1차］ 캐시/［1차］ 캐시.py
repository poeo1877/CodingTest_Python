import time

def solution(cacheSize, cities):
    cache = {}
    totalTime = 0
    for city in cities:
        city = city.lower()
        if cacheSize > 0 and city in cache:
            totalTime += 1
            cache[city] = time.time()
            continue
        elif len(cache) < cacheSize:
            totalTime += 5
            cache[city] = time.time()
            continue
        elif len(cache) >= cacheSize > 0:
            totalTime += 5
            LRU = min(cache, key = lambda k: cache[k])
            del cache[LRU]
            cache[city] = time.time()
        else:
            totalTime += 5
            
    return totalTime
