words = ["practice", "makes", "perfect", "perfect", "perfect", "coding", "perfect", "perfect", "kjhkjhkh", "makes", "perfect","sdfsdf", "coding"]
word1 = "makes"
word2 = "coding"

def func(my_list, word1, word2):
    result_dest = len(my_list)
    index_1 = 0
    index_2 = 0
    for index_tmp, word_tmp in enumerate(my_list):
        if word_tmp == word1:
            index_1 = index_tmp
        if word_tmp == word2:
            index_2 = index_tmp
        if index_1 != 0 and index_2 != 0:

            if abs(index_2-index_1) < result_dest:
               result_dest = abs(index_2-index_1)

    return result_dest

print(f"Dist: {func(words, word1, word2)}")


#{"practice" : [0],"makes" : [1,4], "perfect": [2] , "coding" [3,6]}

