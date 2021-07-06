import copy
from compare import *


def new_algo(data2):
    data3 = copy.deepcopy(data2)
    ready = []
    waiting = []
    terminated = []
    split = []

    threshold = 50
    time, iteration = 0, 1

    # all processes can be in waiting queue
    while data2 or ready or waiting:
        i = 0  # checking whether a process arrived ################
        while i < len(data2):
            if data2[i]['at'] <= time:
                if data2[i]['bt1'] != 0:
                    data2[i]['bt'] = data2[i]['bt1']
                else:
                    if data2[i]['io'] != 0:
                        data2[i]['ioStart'] = time
                        waiting.append(data2[i])
                        data2.remove(data2[i])
                        continue
                    else:
                        data2[i]['bt'] = data2[i]['bt2']
                ready.append(data2[i])
                data2.remove(data2[i])
            else:
                i += 1

        # (data = ready = empty) and (waiting != empty)
        if not ready and not data2:
            min_time = float('inf')
            for i in waiting:
                if i['ioStart'] + i['io'] < min_time:
                    min_time = i['ioStart'] + i['io']
            time = max(min_time, time)

        i = 0  # checking whether a process completed its IO #######
        while i < len(waiting):
            if waiting[i]['ioStart'] + waiting[i]['io'] <= time:
                waiting[i]['bt'] = waiting[i]['bt2']
                waiting[i]['io'] = 0
                ready.append(waiting[i])
                waiting.remove(waiting[i])
            else:
                i += 1

        print('iteration', iteration)
        ready = sorted(ready, key=lambda item: item['bt'])

        if iteration % 2 == 0:
            # execute middle #----------------------------------------->
            middle = (len(ready)//2)
            cpu = ready[middle]
            ready.remove(ready[middle])
            time += cpu['bt']
            print('P' + str(cpu['id']), cpu['bt'], '--')

            iteration += 1
            if cpu['id'] not in split:
                cpu['bt1'] = 0
                if cpu['io'] != 0:
                    cpu['ioStart'] = time
                    waiting.append(cpu)
                else:
                    cpu['ct'] = time
                    terminated.append(cpu)
            else:
                split.remove(cpu['id'])

        else:
            # execute first process #---------------------------------->
            cpu = ready[0]
            ready = ready[1:]
            time += cpu['bt']
            print('P' + str(cpu['id']), cpu['bt'])
            print(time)

            if cpu['id'] not in split:
                cpu['bt1'] = 0
                if cpu['io'] != 0:
                    cpu['ioStart'] = time
                    waiting.append(cpu)
                else:
                    cpu['ct'] = time
                    terminated.append(cpu)
            else:
                split.remove(cpu['id'])

            i = 0  # checking whether a process arrived ##################
            while i < len(data2):
                if data2[i]['at'] <= time:
                    if data2[i]['bt1'] != 0:
                        data2[i]['bt'] = data2[i]['bt1']
                    else:
                        data2[i]['bt'] = data2[i]['bt2']
                    ready.append(data2[i])
                    data2.remove(data2[i])
                else:
                    i += 1

            # (data = ready = empty) and (waiting != empty)
            if not ready and not data2:
                min_time = float('inf')
                for i in waiting:
                    if i['ioStart'] + i['io'] < min_time:
                        min_time = i['ioStart'] + i['io']
                time = max(min_time, time)

            i = 0  # checking whether a process completed its IO #########
            while i < len(waiting):
                if waiting[i]['ioStart'] + waiting[i]['io'] <= time:
                    waiting[i]['bt'] = waiting[i]['bt2']
                    waiting[i]['io'] = 0
                    ready.append(waiting[i])
                    waiting.remove(waiting[i])
                else:
                    i += 1
            ready = sorted(ready, key=lambda item: item['bt'])

            # deciding whether to execute last process or not in READY queue
            if ready and ready[-1]['bt'] > threshold:
                # split #----------------------------------------------->
                print(ready[-1]['bt'], 'split')
                new_process = ready[-1].copy()

                split.append(new_process['id'])
                new_process['bt'] = ready[-1]['bt'] // 4
                if ready[-1]['bt'] % 4 != 0:
                    new_process['bt'] += 1

                ready[-1]['bt'] -= new_process['bt']
                ready.append(new_process)
                iteration += 1

            elif ready:
                # execute last process #-------------------------------->
                cpu = ready[-1]
                ready.remove(cpu)
                time += cpu['bt']
                print('P' + str(cpu['id']), cpu['bt'])
                print(time)

                if cpu['id'] not in split:
                    cpu['bt1'] = 0
                    if cpu['io'] != 0:
                        cpu['ioStart'] = time
                        waiting.append(cpu)
                    else:
                        cpu['ct'] = time
                        terminated.append(cpu)
                else:
                    split.remove(cpu['id'])
                iteration += 1

    # adding bt1 and bt2
    i = 0
    while i < len(data3):
        data3[i]['bt'] = data3[i]['bt1'] + data3[i]['bt2']
        j = 0
        while j < len(terminated):
            if data3[i]['id'] == terminated[j]['id']:
                data3[i]['ct'] = terminated[j]['ct']
                break
            j += 1
        i += 1

    return data3
