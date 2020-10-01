"""
Counting sort is a sorting algorithm that sorts the elements of an array 
by counting the number of occurrences of each unique element in the array. 
The count is stored in an auxiliary array and the sorting is done 
by mapping the count as an index of the auxiliary array.

"""
#  Write a function that takes:

#     a list of unsorted_scores
#     the highest_possible_score in the game

# and returns a sorted list of scores in less than O(nlg⁡n)O(n\lg{n})O(nlgn) time.

# For example:



def sort_scores(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score+1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []

    # For each item in score_counts
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for time in range(count):
            # Add it to the sorted list
            sorted_scores.append(score)

    return sorted_scores

# O(n) time  complexity
# O(n)  space complexity

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
