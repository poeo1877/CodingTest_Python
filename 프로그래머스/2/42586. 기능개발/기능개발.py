from collections import OrderedDict
import math

def solution(progresses, speeds):
    deployment_plan = []
    for progress, speed in zip(progresses, speeds):
        date = math.ceil((100 - progress) / speed)
        if deployment_plan and deployment_plan[-1][0] >= date:
            deployment_plan[-1][1] += 1
        else:
            deployment_plan.append([date, 1])
    
    answer = [deployment[1] for deployment in deployment_plan]
    return answer


