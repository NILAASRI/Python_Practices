def longest_word_length(s):
    return max(map(len, s.split()))

print(longest_word_length("Python is awesome"))  # Output: 7
