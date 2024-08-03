from engine import fight

if __name__ == "__main__":
    for i in range(1, 161, 4):
        print(F"![](examples/board_example_{i}.png)|![](examples/board_example_{i + 2 - 1}.png)|![](examples/board_example_{i + 3 - 1}.png)|![](examples/board_example_{i + 4 - 1}.png)")
        
    # fight(
    #     white="pnbqkr",
    #     black="pnbrqk"
    # )