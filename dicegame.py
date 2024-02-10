import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, steps):
    player += steps
    if player > 100:
        player = 100 - (player - 100)  # Bounce back if overshoots
    return player

def main():
    players = {"Player 1": 0, "Player 2": 0}
    while True:
        for player in players:
            input(f"{player},按 Enter 掷骰子...")
            steps = roll_dice()
            print(f"{player}掷出了 {steps} 点.")
            players[player] = move_player(players[player], steps)
            print(f"{player}现在在第 {players[player]} 个方格.")
            if players[player] == 100:
                print(f"恭喜！{player}获胜了！")
                return

if __name__ == "__main__":
    main()

