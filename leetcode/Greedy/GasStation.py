def gasStation(gas: list, cost: list) -> int:
    for start in range(len(gas)):
        remain = gas[start]
        n = 0

        for i in range(start, start+len(gas)):
            idx = i % len(gas)
            if remain - cost[idx] < 0:
                break
            remain += gas[idx] - cost[idx] 
            n += 1

            if n == len(gas):
                return start
    
    return -1
    
print(gasStation([1,2,3,4,5], [3,4,5,1,2]))