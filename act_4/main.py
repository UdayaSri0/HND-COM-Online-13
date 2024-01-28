def swap(a, b):
    return b, a

def sort_three_numbers(left, mid, right):
    if mid < left:
        left, mid = swap(left, mid)
    if right < left:
        left, right = swap(left, right)
    if right < mid:
        mid, right = swap(mid, right)
    
    return left, mid, right

# Example usage with predefined numbers:
left = 1
mid = 10
right = 2

sorted_numbers = sort_three_numbers(left, mid, right)
print(sorted_numbers)

