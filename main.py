def median(nums: list):
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2 
    else:
        return sorted_nums[mid]


def statistics(nums: list):    

    sum_of_nums = sum(nums)
    count = len(nums)

    print("Input: ", sorted(nums))

    average = sum_of_nums / count
    print("Average: ", average)

    max_num = max(nums)
    print("Max: ", max_num)

    min_num = min(nums)
    print("Min: ", min_num)

    dupelicate = [i for i in set(nums) if nums.count(i) > 1]
    print("Dupelicate: ", dupelicate)

    print("Median: ", median(nums))


nums = list(
    map(
        int,
        input("Enter numbers separated by space: ").split()
    )
)

# input() takes the user's input as a string.
# split() separates that string into individual strings using whitespace.
# map() applies the int() function to each string, converting them into integers.
# Finally, list() converts the mapped result into an actual list.

statistics(nums)