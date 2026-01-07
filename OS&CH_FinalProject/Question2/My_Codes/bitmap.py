MYDISK_SIZE = 16
### total number of blocks available on the disk right now

bitmap = [0] * MYDISK_SIZE
### bitmap list where 0 means free and 1 means allocated

def bitmap_allocate(block_count):
### function allocates consecutive blocks using bitmap allocation
    free_counter = 0
    ### keeps track of how many free blocks are found in a row

    for i in range(MYDISK_SIZE):
    ### scan the disk from start to end

        if bitmap[i] == 0:
        ### if the current block is free
            free_counter += 1
            ### increasing the count of consecutive free blocks

            if free_counter == block_count:
            ### if we found enough space for the file
                for j in range(i - block_count + 1, i + 1):
                ### looping over the blocks that will be allocated

                    bitmap[j] = 1
                    ### mark each block as allocated

                return i - block_count + 1
                ### return the starting index of the allocated space
        else:
        ### if the block is already allocated
            free_counter = 0
            ### reset the counter and keep searching
    return -1
    ### allocation failed because no suitable space was found

def bitmap_free(start_index, size):
### this function is freeing previously allocated bitmap blocks

    for i in range(start_index, start_index + size):
    ###loop through the allocated block range

        bitmap[i] = 0
        ### marking each block as free again

def print_bitmap():
### print the current state of the bitmap
    print("Bitmap:", bitmap)
    ### display bitmap on the screen

start = bitmap_allocate(4)
### allocate space for a file of size 4 blocks
print_bitmap()
### bitmap after allocation
bitmap_free(start, 4)
### free the allocated blocks
print_bitmap()
### bitmap after freeing blocks/last step