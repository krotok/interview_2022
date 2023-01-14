#Given an array of strings
# `words` and two different strings that already exist in the array
# `word1` and
# `word2`, return
# *the shortest distance between these two words in the list*
#.

#**Example 1:**

# ```
# Input: words = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
# Output: 3
#
# ```
#
# #**Example 2:**
#
# ```
# Input: words = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
# Output: 1
# ```
#
# **Constraints:**

# - `words[i]`#consists of lowercase English letters.
# - `word1`# and `word2` are in`words`.
# - `word1 != word2`

# words = ["practice", "makes", "perfect", "coding", "makes"]
# word1 = "coding"
# word2 = "practice"

words = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"


def func(my_list, word1, word2):
    result_dest = 0
    for word in my_list:
        if word1 in my_list:
            word1_count = my_list.count(word1)
            if word1_count < 2 :
                indx1 = my_list.index(word1)
                indx2 = my_list.index(word2)
                return abs(indx2 - indx1)
            else:
                indices = [i for i, x in enumerate(my_list) if x == word2]
                print(indices)

                # result_tmp = abs(my_list.index(word2) - my_list.index(word1))
                # if result_dest == 0:
                #     result_dest = result_tmp
                # else:
                #     if result_tmp < result_dest:
                #         result_dest = result_tmp

    return result_dest



print(f"Dist: {func(words, word1, word2 )}")