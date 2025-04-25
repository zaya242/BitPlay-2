# program to find the element not making a pair

# function to calculate the number that is odd occuring

def OddOccuring(arr):
     
     # initialise result
     res = 0

     # transverse the array
     for element in arr:
          # XOR with the result
          res = res ^ element

     return res   

# initialise our array
arr = []

# take array size as input
n = int(input("Enter the size of the array : "))

# take array elements as input
while(n):
     num = int(input("Enter number : "))
     arr.append(num)
     n-=1

print("\n\nOdd occuring number is : ", OddOccuring(arr))
     