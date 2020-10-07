import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):

    # Shuffle the input in place
    # for index, element in enumerate(the_list):
    #     floor = the_list[0]
    #     ceiling = the_list[len(the_list) - 1]
    #     the_list[index] = get_random(floor, ceiling)

    if len(the_list) <= 1:
        return the_list

    # Walk through from beginning to end
    for index in range(0, len(the_list) - 1):

        # Choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_choice_index = get_random(index,len(the_list) - 1)

        # Place our random choice in the spot by swapping
        if random_choice_index != index:
            the_list[index], the_list[random_choice_index] = the_list[random_choice_index], the_list[index]
                
    
# O(n) time and 
# O(1) space. 

sample_list = [1, 2, 3, 4, 5]
print( 'Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print( sample_list)