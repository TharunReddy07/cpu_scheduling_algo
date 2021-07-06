from algorithms import *
from compare import *
from twoPointerIO import *
import sys
import copy
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

if __name__ == '__main__':
    data1 = []
    for _ in range(int(input())):
        data1.append({})
        arr = list(map(int, input().split()))
        data1[-1]['id'] = arr[0]
        data1[-1]['at'] = arr[1]
        data1[-1]['bt1'] = arr[2]
        data1[-1]['io'] = arr[3]
        data1[-1]['bt2'] = arr[4]

    data2 = copy.deepcopy(data1)
    ans = new_algo(data2)
    for i in ans:
        print(i)
    output(ans, "Two pointer")

    '''
    data4 = copy.deepcopy(data1)
    ans = first_come_first_serve(data4)
    output(ans, "First come first serve")

    ans = shortest_job_first(data4)
    output(ans, "SJF non-preemptive")

    ans = shortest_remaining_time(data4)
    output(ans, "SJF preemptive")

    ans = round_robin(data4, 4)
    output(ans, "Round Robin") '''
