# https://www.geeksforgeeks.org/python-sum-of-number-digits-in-list/

test_list = [12, 67, 98, 34]

result = []

for item in test_list:
    digit_sum = 0
    while item != 0:
        digit_num = item % 10
        digit_sum += digit_num
        item //= 10
    result.append(digit_sum)

print("The sum of number digit in list {}".format(result))
