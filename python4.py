#this programs gives the pair by nested loop by taking one element in the outer loop and adds with the element inside the inner loop and find the sum and returns the pair
def sum_pairs(arr):
    target=int(input("enter the target number to get sum pairs: "))
    for i in range(1,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                print(arr[i],arr[j])
sum_pairs([1,2,3,4,5,6,7,8,9])