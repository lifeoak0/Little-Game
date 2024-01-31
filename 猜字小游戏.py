import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)  # 随机生成一个1到100之间的数字
    guess = None

    while guess != number_to_guess:
        guess = int(input("猜一个1到100之间的数字: "))

        if guess < number_to_guess:
            print("太低了！再试一次。")
        elif guess > number_to_guess:
            print("太高了！再试一次。")

    print(f"恭喜你！正确答案是 {number_to_guess}.")

# 运行游戏
guess_the_number()
