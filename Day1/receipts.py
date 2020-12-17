import time

def two_sum_problem_naive():
    start_time = time.time()
    values = []
    with open("input.txt", "r") as f:
        values = [int(i) for i in f.read().split("\n")]
    for i in range(len(values)):
        init_value = values[i]
        for j in range(i + 1, len(values)):
            if init_value + values[j] == 2020:
                print(init_value, values[j])
                print(time.time() - start_time)
                return init_value * values[j]

def two_sum_problem_smarter():
    start_time = time.time()
    available = [0 for i in range(2020)]
    with open("input_receipts.txt", "r") as f:
        for val_str in f.read().split("\n"):
            val = int(val_str)
            available[val] = 1
            if available[2020-val] == 1:
                print(time.time() - start_time)
                return val * (2020 - val)

def three_sum_problem_naive():
    values = []
    with open("input_receipts.txt", "r") as f:
        values = [int(i) for i in f.read().split("\n")]
    for i in range(len(values)):
        A = values[i]
        for j in range(i + 1, len(values)):
            B = values[j]
            for k in range(j + 1, len(values)):  
                if A + B + values[k] == 2020:
                    print(A, B, values[k])
                    return A * B * values[k]  