from array import *

def prepare(numbers,low,high):
    pivot = numbers[high]
    item = low - 1

    for i in range(low,high):
        if numbers[i] <= pivot:
            item += 1
            numbers[item],numbers[i] = numbers[i],numbers[item]

    numbers[item + 1],numbers[high] = numbers[high],numbers[item + 1]

    return item+1

def Quick_sort(numbers,low,high):
    if low < high:
        pivot = prepare(numbers,low,high)
        Quick_sort(numbers,low,pivot-1)
        Quick_sort(numbers,pivot+1,high)

a = array('i',[])
c = int(input("Enter array size: "))
print(f"The size of array = {c}")

for i in range(c):
    x = int(input("Enter the elements of array: "))
    a.append(x)

print("The unsorted array Elements =",a)

total_a = len(a)

Quick_sort(a,0,total_a)
print(f"The sorted array Elemets = {a}")