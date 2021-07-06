def avg_wt_tat(data):
    for dct in data:
        dct['tat'] = dct['ct'] - dct['at']
        dct['wt'] = dct['tat'] - dct['bt']
    tot_wt = tot_tat = 0
    for dct in data:
        tot_wt += dct['wt']
        tot_tat += dct['tat']
    ln = len(data)
    return {'avg_TAT': tot_tat/ln, 'avg_WT': tot_wt/ln}


def generate_gantt(data):
    lst = []
    for dct in data:
        lst.append([dct['ct'], dct['id']])
    lst.sort()
    cht = "|"
    tm = "0"
    for i in lst:
        cht += i[0]//2*'_' + str(i[1]) + i[0]//2*'_' + '|'
        tm += " "*(i[0]+1) + str(i[0])

    print(cht)
    print(tm)


def output(data, algo):
    print(algo)
    data = avg_wt_tat(data)
    for num in data:
        print(num, "=", data[num])
    print('---'*9, '\n')
