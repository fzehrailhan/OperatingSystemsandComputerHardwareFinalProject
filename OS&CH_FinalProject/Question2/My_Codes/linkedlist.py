TOTAL_BLOCKS = 8 ### total number of disk blocks on the disk
class DiskBlock: ### this class represents a single disk block

    def __init__(self): ### constructor initializes the block as free

        self.allocated = 0
        ### 0 means the block is free, 1 means it is allocated/taken
        self.next = -1
        ### stores the index of the next block in the linked list

disk = [DiskBlock() for _ in range(TOTAL_BLOCKS)]
### create the disk as a list of empty disk blocks

def allocate_linked(block_count):
### allocates disk blocks using linked-list allocation
    first_block = -1
    ### stores the index of the first block of the file
    previous_block = -1
    ### keeps track of the previously allocated block

    for i in range(TOTAL_BLOCKS):
    ### scan the disk block by block

        if block_count == 0:
        ### stops if all required blocks are allocated
            break

        if disk[i].allocated == 0:
        ### use the block only if it is freee

            disk[i].allocated = 1 ### mark the block as allocated

            disk[i].next = -1   ### initialize next pointer

            if first_block == -1: ### sets the first block if not set yet
                first_block = i

            if previous_block != -1: ### link previous block to the current block
                disk[previous_block].next = i

            previous_block = i ### update the previous block index
            block_count -= 1 ### decrease remaining block count

    if block_count > 0: ### allocation fails if not enough free blocks exist
        return -1

    return first_block ### returning the starting block index of the file

def free_linked(start_block):
### frees all blocks of a file by following the linked list

    current = start_block  ### start from the first allocated block

    while current != -1:    ### continue until the end of the linked list

        next_block = disk[current].next ### save the next block index
        disk[current].allocated = 0 ### mark the current block as free

        disk[current].next = -1  ###resets the next pointer
        current = next_block ### move to the next block

def print_disk_state():
### Prints the allocation status of the disk
    state = [block.allocated for block in disk]
    ### Convert block objects into a list of 1s and 0s
    print("Disk:", state)
    ### Display the disk state

start1 = allocate_linked(3)
print_disk_state() ### show disk after first allocation

start2 = allocate_linked(1)
print_disk_state()### show disk after second allocation
free_linked(start2)### free the second file
print_disk_state()### shows disk after freeing blocks
