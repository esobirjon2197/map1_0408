# 1-m
i = [1, 2, 3, 34, 4, 553,6]
print(i)

t = list(map(lambda el: el * 2, i))
print(t)


# 2-m
roy = [10, 20, 30, 40]
print(roy)

t = list(map(lambda el: el -5, roy))
print(t)


# 3-m
roy = ["apple", "banana", "cherry"]
print(roy)

t = list(map(lambda el: el.upper(), roy))
print(t)


# 4-m
roy = ["salom", "dunyo", "python"]
print(roy)

t = list(map(lambda el: len(el), roy))
print(t)


# 5-m
roy = [3, 6, 9, 12]
print(roy)

t = list(map(lambda el: el ** 2, roy))
print(t)


# 6-m
roy = ["Ali", "Vali", "Hasan"]
print(roy)

t = list(map(lambda el:  f"MR. {el}", roy))
print(t)


# 7-m
roy = [100, 200, 300]
print(roy)

t = list(map(lambda el: str(el), roy))
print(t)


# 8-m
roy = ["1", "2", "3", "4"]
print(roy)

t = list(map(lambda el: int(el), roy))
print(t)


# 9-m
roy = [5, 10, 15, 20]
print(roy)

t = list(map(lambda el: el / 3, roy))
print(t)


# 10-m
roy = ["hello", "world"]
print(roy)

t = list(map(lambda el: f"{el} !", roy))
print(t)

