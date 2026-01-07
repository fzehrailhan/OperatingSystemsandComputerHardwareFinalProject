MEMORY_SIZE = 99  ### total memory
free_list = [[0, MEMORY_SIZE]]  ### free list stores free blocks as [start_index, length]
next_fit_pointer = 0  ### pointer for Next Fit allocation

def allocate_best_fit(size):  ### allocate memory using Best Fit strategy
    best_index = -1
    best_size = float('inf')  ### smallest sufficient block found so far

    for i, (start, length) in enumerate(free_list):  ### check each free block
        if length >= size and length < best_size:
            best_size = length
            best_index = i
    if best_index == -1:  ### no suitable block found
        return -1

    start, length = free_list[best_index]
    allocated_start = start  ### remember where allocation starts
    if length == size:  ### perfect fit, remove block
        free_list.pop(best_index)
    else:  ### split the block and keep leftover
        free_list[best_index] = [start + size, length - size]
    return allocated_start

def allocate_worst_fit(size):  ### allocate memory using Worst Fit strategy
    worst_index = -1
    worst_size = -1  ### largest block found so far

    for i, (start, length) in enumerate(free_list):  ### check each free block
        if length >= size and length > worst_size:
            worst_size = length
            worst_index = i
    if worst_index == -1:  ### no suitable block found
        return -1

    start, length = free_list[worst_index]
    allocated_start = start  ### remember starting point
    if length == size:  ### perfect fit, remove block
        free_list.pop(worst_index)
    else:  ### split the block
        free_list[worst_index] = [start + size, length - size]
    return allocated_start

def allocate_next_fit(size):  ### allocate memory using Next Fit strategy
    global next_fit_pointer
    n = len(free_list)
    if n == 0:  ### nothing to allocate
        return -1

    for i in range(n):  ### circular scan starting from last allocation
        index = (next_fit_pointer + i) % n
        start, length = free_list[index]
        if length >= size:
            allocated_start = start  ### remember start
            if length == size:  ### perfect fit, remove block
                free_list.pop(index)
                if free_list:
                    next_fit_pointer = index % len(free_list)
                else:
                    next_fit_pointer = 0
            else:  ### split the block
                free_list[index] = [start + size, length - size]
                next_fit_pointer = index
            return allocated_start
    return -1  ### allocation failed

def free_block(start, size):  ### free a memory block and merge neighboring free blocks
    free_list.append([start, size])
    free_list.sort()  ### sort blocks by start index

    merged = []
    for block in free_list:
        if not merged:
            merged.append(block)
        else:
            last_start, last_length = merged[-1]
            curr_start, curr_length = block
            if last_start + last_length == curr_start:  ### merge adjacent blocks
                merged[-1][1] += curr_length
            else:
                merged.append(block)
    free_list.clear()
    free_list.extend(merged)

def print_memory():  ### print current free memory blocks
    print("Free memory:", free_list)

a = allocate_best_fit(7)
print("Best Fit allocated 7 units at", a)
print_memory()
b = allocate_worst_fit(20)
print("Worst Fit allocated 20 units at", b)
print_memory()
c = allocate_next_fit(9)
print("Next Fit allocated 9 units at", c)
print_memory()
free_block(b, 20)
print("Freed 20 units allocated by Worst Fit")
print_memory()
