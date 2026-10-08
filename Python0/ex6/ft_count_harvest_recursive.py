

def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))

    def helper(day_i, day_f):
        if day_i > day_f:
            print("Harvest time!")
        else:
            print("Day", day_i)
            helper(day_i + 1, day_f)
    helper(1, day)
