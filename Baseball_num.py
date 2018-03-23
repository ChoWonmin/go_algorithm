
time = input()
solve_list = []

def solve(question, s, b):
    answer = [s, b]

    print(answer)
    if(["0","0"]==answer):
        for num in solve_list:
            for q_num in question:
                if(q_num in num):
                    print(num , q_num)
                    solve_list.remove(num)
                    break

    elif(["0","1"]==answer):
        for num in solve_list:
            for q_num in question:
                if(q_num not in num):
                    solve_list.remove(num)
                    break

    elif(["0","2"]==answer):
        for num in solve_list:
            for q_num in question:
                if(q_num not in num):
                    solve_list.remove(num)
                    break

    elif(["0","3"]==answer):
        print(answer)
    elif(["1","0"]==answer):
        print(answer)
    elif(["1","1"]==answer):
        print(answer)
    elif(["1","2"]==answer):
        print(answer)
    elif(["2","0"]==answer):
        print(answer)
    elif(["2","1"] == answer):
        print(answer)
    elif(["3","0"] == answer):
        print(answer)


for i in range(123, 988):
    num = str(i)

    tmp = {num[0], num[1], num[2]}

    if("0" in num):
        continue
    length = tmp.__len__()



    if(length > 2):
        solve_list.append(num)

for i in range(0, time):
    line = raw_input().split(" ")

    print(solve_list.__len__())
    solve(line[0], line[1], line[2])
    print(solve_list.__len__())
