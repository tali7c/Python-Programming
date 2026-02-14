# Runner-up score
n = int(input("Enter number of scores: "))
values = list(map(int, input("Enter scores: ").split()))

scores = sorted(set(values[:n]))
if len(scores) < 2:
    print("Not enough distinct scores")
else:
    print("Runner-up:", scores[-2])
