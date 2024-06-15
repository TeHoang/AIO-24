def max_k(num_list: list, k: int) -> list:
    return [max(num_list[i:i+k]) for i in range(len(num_list)-k+1)]


print(max_k([3, 4, 5, 1, -44, 5, 10, 12, 33, 1], 3))

# [5, 5, 5, 5, 10, 12, 33, 33]
