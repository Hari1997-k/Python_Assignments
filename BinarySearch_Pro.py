def binary_search(arr, ele):
    start = 0
    end = len(arr) - 1
    while start <= end:

        mid = (start + end) // 2
        if (arr[mid] == ele):
            return mid
        elif (arr[mid] > ele):
            end = mid - 1
        else:
            start = mid + 1

    return -1


print("Enter The Size Of The Array : ", end="\n")
size = int(input())
arr = []
print("Enter ", size, "Elements  In Ascending Order: ")
for i in range(size):
    ele = int(input())
    arr.append(ele)
print("Enter The Element To Do Binary Search : ", end="\n")
ele = int(input())
res = binary_search(arr, ele)
if (res == -1):
    print("The Element Is " , ele, "  Not Founded In The Array ")
else:
    print("The Element " , ele, " Is present At Index - ", res)
