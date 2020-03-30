def find_missing_number(arr):
    n = len(arr)

    xor_value_of_supplied_numbers = 0
    for i in range(n):
        xor_value_of_supplied_numbers ^= arr[i]
    print("\n xor_value_of_supplied_numbers: ", xor_value_of_supplied_numbers, "\t bin(xor_value_of_supplied_numbers): ", bin(xor_value_of_supplied_numbers))

    number_of_expected_numbers = n + 1
    start_index = 1

    xor_value_of_expected_numbers = 0
    for i in range(start_index, start_index + number_of_expected_numbers):
        xor_value_of_expected_numbers ^= i
    print("\n xor_value_of_expected_numbers: ", xor_value_of_expected_numbers, "\t bin(xor_value_of_expected_numbers): ", bin(xor_value_of_expected_numbers))

    return xor_value_of_supplied_numbers ^ xor_value_of_expected_numbers


if __name__ == "__main__":
    arr = 6, 1, 4, 2, 3
    missing_number = find_missing_number(arr)
    print("\n missing_number: ", missing_number, "\t bin(missing_number): ", bin(missing_number))

