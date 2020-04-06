"""
Title:  Can plant flowers?

You are given a flowerbed in the form of an array and number n, plants.  Each value
in array can be either 0 = empty lot or 1 = occupied lot.  Your task is to determine
if n flowers can be planted in flowerbed.  The condition is that two flowers cannot
be in adjacent lot otherwise they will compete for resources.


Example 1:

Input:
Flowerbed = [1,0,0,0,1], n = 1
Output: True


Example 2:

Input:
Flowerbed = [1,0,1,0,1], n = 1
Output:  False


Example 3:

Input:
Flowerbed = [1,0,0,0,1], n = 2
Output:  False


Time:  O(N)
Space:  O(1)
"""


def can_plant_flowers(flower_bed, n):
    if len(flower_bed) <= 0:
        raise Exception("\n Invalid flower_bed supplied.  For flower_bed, please supply a non-empty list")
    if n <= 0:
        raise Exception("\n Invalid n supplied.  For n, please supply an integer value greater than zero")
    if len(flower_bed) == 1 and flower_bed[0] == 1:
        raise Exception("\n The flower_bed is fully planted.  No lot to plant")
    if len(flower_bed) == 1 and flower_bed[0] == 0 and n == 1:
        return True

    for i in range(len(flower_bed)):
        if flower_bed[i] == 0 and i - 1 >= 0 and flower_bed[i - 1] != 1 and i + 1 <= len(flower_bed) and flower_bed[i + 1] != 1:
            flower_bed[i] = 1
            n -= 1
            if n == 0:
                return True
    return n == 0


if __name__ == "__main__":
    #flower_bed = []
    #flower_bed = [0]
    #flower_bed = [1]
    flower_bed = [1, 0, 0, 0, 1]
    #flower_bed = [1, 0, 1, 0, 1]
    #flower_bed = [1, 0, 0, 0, 1]
    print("\n flower_bed: ", flower_bed)

    #n = 0
    #n = 1
    n = 2
    print(" n: ", n)

    can_plant = can_plant_flowers(flower_bed, n)
    print("\n can_plant: ", can_plant)
