#  You are a renowned thief who has recently switched from stealing precious metals to stealing cakes
#  because of the insane profit margins. You end up hitting the jackpot, 
# breaking into the world's largest privately owned stock of cakes—the vault of the Queen of England.

# While Queen Elizabeth has a limited number of types of cake, she has an unlimited supply of each type.

# Each type of cake has a weight and a value, stored in a tuple with two indices:

#     An integer representing the weight of the cake in kilograms
#     An integer representing the monetary value of the cake in British shillings

# For example:

#   # Weighs 7 kilograms and has a value of 160 shillings
# (7, 160)

# # Weighs 3 kilograms and has a value of 90 shillings
# (3, 90)


def max_duffel_bag_value(cake_tuples, weight_capacity):
    
    # We make a list to hold the maximum possible value at every
    # duffel bag weight capacity from 0 to weight_capacity
    # starting each index with value 0
    max_values_at_capacities = [0] * (weight_capacity + 1)

    for current_capacity in range(weight_capacity + 1):
        # Set a variable to hold the max monetary value so far
        # for current_capacity
        current_max_value = 0

        for cake_weight, cake_value in cake_tuples:
            # If a cake weighs 0 and has a positive value the value of
            # our duffel bag is infinite!
            if cake_weight == 0 and cake_value != 0:
                return float('inf')

            # If the current cake weighs as much or less than the
            # current weight capacity it's possible taking the cake
            # would get a better value
            if cake_weight <= current_capacity:

                # So we check: should we use the cake or not?
                # If we use the cake, the most kilograms we can include in
                # addition to the cake we're adding is the current capacity
                # minus the cake's weight. We find the max value at that
                # integer capacity in our list max_values_at_capacities
                max_value_using_cake = (
                    cake_value
                    + max_values_at_capacities[current_capacity - cake_weight]
                )

                # Now we see if it's worth taking the cake. how does the
                # value with the cake compare to the current_max_value?
                current_max_value = max(max_value_using_cake,
                                        current_max_value)

        # Add each capacity's max value to our list so we can use them
        # when calculating all the remaining capacities
        max_values_at_capacities[current_capacity] = current_max_value
    return max_values_at_capacities[weight_capacity]

# Time/ Space complexity
# O(n∗k) time, and O(k) space, 
# where n is number of types of cake and k is the capacity of the duffel bag

if __name__ == '__main__':
    # Use the main function here to test out the implementation
    

    cake_tuples = [(7, 160), (3, 90), (2, 15)]
    capacity    = 20

    print(f"The maximum value is: {max_duffel_bag_value(cake_tuples, capacity)}")
# Returns 555 (6 of the middle type of cake and 1 of the last type of cake)
           