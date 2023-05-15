def get_user_input() -> int:
    while True:
        try:
            user_input = int(input("請輸入1至9的數字："))
            if 1 <= user_input <= 9:
                return user_input
            else:
                print("請輸入1至9，請重新輸入")
        except ValueError:
            print("輸入錯誤，請重新輸入一個有效的數字")

def print_multiplication_table(number, i=1):
    if i > 9:
        return
    result = number * i
    print(f"{number} x {i} = {result}")
    print_multiplication_table(number, i + 1)

def main():
    user_input = get_user_input()
    print_multiplication_table(user_input)

if __name__ == "__main__":
    main()
