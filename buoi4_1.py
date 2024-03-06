things = ['pen','ruler','wallet','phone']
def do_something(input_list):
    output=""
    if not input_list:
        print(f"File rong {output}")
        return True
    
    if len(input_list) == 1:
        print(input_list[0])
        return True
    
    output = ", ".join(input_list[:-1])
    output += f" and {input_list[-1]}"
    # for i in range(len(input_list)):
    #     if i == len(input_list) - 1:
    #         x = input_list[-1]
    #         print(x)
    #         output += f" and {input_list[i]}"
    #     else:
    #         output += f"{input_list[i]},"
    # output = ", ".join(input_list)
    # print(output)
    # x = input_list[-1]
    # y = output[0:-1]
    # print(y)
    # output = output[0:-1] + f" and {x}"
    # for i in input_list[:-1]:
    #     output += f"{i},"
    #     #print(output)
    # output += f"and {input_list[-1]}"
    print(output)
do_something(things)
#do_something(['pen','1'])
