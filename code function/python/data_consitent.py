def count_consistent_indices(data, min_value=50, min_consistency=3):
    consistent_indices = []

    for idx, values in enumerate(zip(*data)):
        # print(values)

        ### cara modern
        if sum(value >= min_value for value in values) >= min_consistency:
            consistent_indices.append(idx)
        
        ### cara kuno
        # count = 0
        # for value in values:
        #     if value >= min_value:
        #         count += 1

        # if count >= min_consistency:
        #     consistent_indices.append(idx)

    return consistent_indices


data = [
    [10, 20, 10, 20, 11, 12, 52, 10, 20, 53, 20, 40, 10],
    [19, 10, 10, 20, 11, 12, 51, 10, 20, 52, 20, 40, 10],
    [19, 10, 51, 20, 11, 12, 54, 10, 20, 55, 20, 40, 10],
    [19, 10, 51, 20, 56, 12, 54, 10, 20, 55, 20, 40, 10],
    [19, 10, 51, 20, 54, 12, 54, 10, 20, 55, 20, 40, 10],
    [19, 10, 51, 20, 54, 12, 54, 10, 20, 55, 20, 40, 10],
]

consistent_indices = count_consistent_indices(data, min_value=50, min_consistency=3)
print(
    "index yang datanya 50 keatas dan muncul 3 kali atau lebih:",
    consistent_indices,
)
