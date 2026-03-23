def wordCount(n):
    words = n.split()
    return f"Word Count: {len(words)}"

n = input("Enter a sentence: ")
print(wordCount(n))