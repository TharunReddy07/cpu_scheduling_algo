import copy


def new_algo(data2):
    data3 = copy.deepcopy(data2)
    ready = []
    waiting = []
    terminated = []

    threshold = 50
    time, iteration = 0, 1

    i = 0
    while i < len(data2):
        if data2[i]['at'] <= time:
            ready.append(data2[i])
            data2.remove(data2[i])
        else:
            i += 1

    while data2 or ready:
        print('iteration', iteration)
        ready = sorted(ready, key=lambda item: item['bt'])

        if iteration % 2 == 0:
            # execute middle
            middle = (len(ready)//2)
            cpu = ready[middle]
            ready.remove(ready[middle])
            time += cpu['bt']
            print('P' + str(cpu['id']), cpu['bt'], '--')

            iteration += 1
            cpu['ct'] = time
            terminated.append(cpu)
            i = 0
            while i < len(data2):
                if data2[i]['at'] <= time:
                    ready.append(data2[i])
                    data2.remove(data2[i])
                else:
                    i += 1

    i = 0
    while i < len(terminated):
        j = 0
        while j < len(data3):
            if terminated[i]['id'] == data3[j]['id']:
                if 'ct' in data3[j]:
                    data3[j]['ct'] = max(terminated[i]['ct'], data3[j]['ct'])
                else:
                    data3[j]['ct'] = terminated[i]['ct']
                break
            j += 1
        i += 1

    return data3
