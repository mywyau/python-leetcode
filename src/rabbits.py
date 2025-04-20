from collections import Counter
import math

def num_rabbits(answers):
    count = Counter(answers)
    total = 0

    for answer, freq in count.items():
        group_size = answer + 1
        groups = math.ceil(freq / group_size)
        total += groups * group_size

    return total
