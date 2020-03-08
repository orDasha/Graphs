sequence = [1, 2, 7, 19]

# Сравните:
idx = 0
for item in sequence:
    print(item)
    idx += 1

# и
for idx, item in enumerate(sequence):
    print(idx)