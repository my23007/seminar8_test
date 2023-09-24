def first_div_16(n1, n2):
    for num in range(n1, n2):
        if num % 16 == 0:
            return num
    return 0
def halve_to_2(number):
    if number <= 0:
        return -1
    
    while number >= 2:
        number /= 2
    
    return number
def string_expansion(input_string):
    result = ""
    for i, char in enumerate(input_string):
        result += char * (2 * i + 2)
    return result
def item_count_from_index(input_list, index):
    if index < 0 or index >= len(input_list):
        return ""

    target_item = input_list[index]
    count = input_list.count(target_item)
    return count
def length_times_largest(input_list):
    largest_int = None

    for item in input_list:
        if isinstance(item, int):
            if largest_int is None or item > largest_int:
                largest_int = item

    if largest_int is not None:
        return len(input_list) * largest_int
    else:
        return ""