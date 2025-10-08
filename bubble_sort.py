# Joshcar Funes
# 10/1/2025

# defines "bubblesort" as a function
def bubblesort(arr):
    n = len(arr)

    # This goes through every array
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traveling through the array from 0 all the way to 1
            # Additionally will swap elements if an element is greater than the one to it's right
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

# This line of code tests the above to ensure that it works
if __name__ =="__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]

    bubblesort(arr)

    print("Sorted array:")
    for i in range(len(arr)):
        print("%d" % arr[i], end=",")
# heh, guess this code felt the fury! source was https://www.geeksforgeeks.org/dsa/bubble-sort-algorithm/
