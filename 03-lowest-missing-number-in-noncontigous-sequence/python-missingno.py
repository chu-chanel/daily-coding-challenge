input_array = [0, 1, 2, 3] #4
#input_array = [-1, 34, 0, 2, 5, 1] #3
#input_array = [-1, 0, -21, -4, -1] #1
#input_array = [-1, 0, -21, 22, -1] #1


def find_missing(input_array):
    full_range = list(range(1, max(input_array) + 2))
    leftover_range = [leftovers for leftovers in full_range
                      if leftovers not in input_array]
    missing_int = leftover_range[0]
    print(missing_int)
    return missing_int


if __name__ == "__main__":
    find_missing(input_array)
