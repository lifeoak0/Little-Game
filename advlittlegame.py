import time

def intro():
    print("欢迎来到神秘岛！")
    time.sleep(2)
    print("你是一名探险家，冒险家，你听说在这个岛上有宝藏，你决定前往探险！")
    time.sleep(2)
    print("你发现了两条路。")
    time.sleep(2)
    print("你会选择左边的路(输入 '左')还是右边的路(输入 '右')?")

def choose_path():
    path = input("左 or 右: ").lower()
    if path == "左":
        print("你选择了左边的路。")
        time.sleep(2)
        left_path()
    elif path == "右":
        print("你选择了右边的路。")
        time.sleep(2)
        right_path()
    else:
        print("无效的输入，请输入 '左' 或 '右'。")
        choose_path()

def left_path():
    print("你沿着左边的路走着，发现了一座古老的废墟。")
    time.sleep(2)
    print("你进入废墟寻找宝藏。")
    time.sleep(2)
    print("突然，你听到了一声巨响，看到了一只巨大的蜘蛛！")
    time.sleep(2)
    print("你会选择与蜘蛛战斗(输入 '战斗')还是逃跑(输入 '逃跑')?")
    action = input("战斗 or 逃跑: ").lower()
    if action == "战斗":
        print("你选择与蜘蛛战斗。")
        time.sleep(2)
        print("你勇敢地与蜘蛛搏斗，最终击败了它！")
        time.sleep(2)
        print("你在废墟里找到了宝藏！")
    elif action == "逃跑":
        print("你选择逃跑，回到了起点。")
        choose_path()
    else:
        print("无效的输入，请输入 '战斗' 或 '逃跑'。")
        left_path()

def right_path():
    print("你选择了右边的路。")
    time.sleep(2)
    print("你沿着小径前行，发现了一个山洞。")
    time.sleep(2)
    print("你进入山洞寻找宝藏。")
    time.sleep(2)
    print("山洞里突然出现了一只巨大的熊！")
    time.sleep(2)
    print("你会选择与熊战斗(输入 '战斗')还是逃跑(输入 '逃跑')?")
    action = input("战斗 or 逃跑: ").lower()
    if action == "战斗":
        print("你选择与熊战斗。")
        time.sleep(2)
        print("你勇敢地与熊搏斗，最终击败了它！")
        time.sleep(2)
        print("你在山洞里找到了宝藏！")
    elif action == "逃跑":
        print("你选择逃跑，回到了起点。")
        choose_path()
    else:
        print("无效的输入，请输入 '战斗' 或 '逃跑'。")
        right_path()

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()

