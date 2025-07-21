

sentences = "python python the best language"
result = reduce(lambda a, x: a + x.count('python'),
                   sentences,
                   0)

print(result)