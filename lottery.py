number = int(input())
tick_series = str(input())
num = int(tick_series[0:6])
series = tick_series[7:].upper()
win_count = min(num, number)
out = random.sample(range(1, num + 1), win_count)
for x in range(win_count):
    print(f"Победитель номер {win_count - x} - \"{out[x]:06d} {series}\"")
