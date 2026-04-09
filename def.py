def area(width, height, units="sq ft"):
    result= width * height
    print(f"{result} {units}")

area (2,5)
area(2,5, units="sq m")


def remainder(dividend, divisor):
    return dividend %  divisor

r = remainder(divisor=4, dividend=17)
print(r)


def find_max_and_index(numbers):
    max_value = max(numbers)
    index= numbers.index(max_value)
    return max_value, index

nums = [1,6,2,9,3,27,4,11,0]
max_val, idx= find_max_and_index(nums)
print(max_val,idx)


count=0

def increment_count():
    global count
    count+=1
print(count)
for _ in range(5):
    increment_count()
print(count)


def make_zeros(numbers):
   for i in range(len(numbers)):
       numbers[i]=0


lst = [1,2,3,4,5]
print(lst)
make_zeros(lst)
print(lst)


