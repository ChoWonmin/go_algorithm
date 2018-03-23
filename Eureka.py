repeat = input()
num = []

def calc_triangular_numbers(t):
    type(t)
    return t*(t+1)/2

def get_answer(num):
    for i in range(1,num):
        x = calc_triangular_numbers(i)
        for j in range(1, num - x):
            y = calc_triangular_numbers(j)
            for k in range(1, num - x - y + 1):
                z = calc_triangular_numbers(k)
                if x+y+z == num :
                    return 1
    return 0

for i in range(repeat):
    num.append(input())

for i in range(repeat):
    print(get_answer(num[i]))

