def welcome():
    print("Chào mừng bạn đến với chương trình Python!")

def sum_numbers():
    a = int(input("Nhập số thứ nhất: "))
    b = int(input("Nhập số thứ hai: "))
    print(f"Tổng của {a} và {b} là {a + b}")

if __name__ == '__main__':
    welcome()
    sum_numbers()