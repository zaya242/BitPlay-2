# program to find two numbers that are odd occuring
def printTwoOdd(arr, size):
    # xorof2 will hold xor of the 2 odd occuring numbers
    xorof2 = arr[0]

    # these will hold 2 odd occuring numbers
    x = 0
    y = 0

    # this will hold the right most set box from xorof2
    setbit = 0

    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]

        setbit = xorof2 & ~(xorof2 - 1)

        # if number is having set bit at location we need then XOR it with x else y
        for i in range(size):
            if (arr[i] & setbit):
                x =x ^ arr[i]
            else:
                y = y ^ arr[i]

        print("The two ODD elements are", x, "and", y)

# create an empty array
arr = []

# rake array size and elemnts as inputs
arr_size = int(input("Enter the size of the array : "))
for i in range(0,arr_size):
    z = int(input("Enter element : "))
    arr.append(z)

printTwoOdd(arr, arr_size)    

