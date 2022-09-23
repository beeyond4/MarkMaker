def marker(data, k1, k2, k3):
    marked ={}
    for i in data:
        mark = '2'
        if data[i] <= k1:
            mark='3'
            if data[i] <= k2:
                mark='4'
                if data[i] <= k3:
                    mark='5'
        marked[i] = mark
    return marked


n = open('run_of_60_mark.txt', 'w')
with open('run_of_60_m.txt') as cls:
    children = [list(line.strip('\n').split(' ')) for line in cls]
m6, m7, f6, f7 = {}, {}, {}, {}
Max_male = ['', '', 100]
Max_female = list(Max_male)

for i in children:
    name, cls, time, sex = i[0], i[1], float(i[2]), i[3]
    if sex == 'm':
        if time < Max_male[2]:
            Max_male = list([name, cls, time])
        if cls == '6': m6[name] = time
        else: m7[name] = time
    else:
        if time < Max_female[2]:
            Max_female = list([name, cls, time])
        if cls == '6': f6[name] = time
        else: f7[name] = time

pupils = marker(m6, 11.1, 10.4, 9.9)
male7 = marker(m7, 11.0, 10.2, 9.4)
female6 = marker(f6, 11.2, 10.6, 10.3)
female7 = marker(f7, 11.4, 10.6, 9.8)
pupils.update(male7)
pupils.update(female6)
pupils.update(female7)

for i in sorted(pupils):
    n.write(i + ' ' + pupils[i] + '\n')

print('TOP1 male:  ', Max_male[0] + ' ' + Max_male[1] + ' class ' + str(Max_male[2]))
print('TOP1 female:', Max_female[0] + ' ' + Max_female[1] + ' class ' + str(Max_female[2]))
