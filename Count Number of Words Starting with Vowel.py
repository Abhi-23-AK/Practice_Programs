sentence = input("Enter sentence: ").lower()
words = sentence.split()

count = sum(1 for w in words if w[0] in "aeiou")
print("Words starting with vowel:", count)