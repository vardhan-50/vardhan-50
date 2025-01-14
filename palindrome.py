#first method
word=input()
is_palindrome=True
for i in range(len(word)//2):
    if word[i]!= word[-(i+1)]:
        is_palindrome=False
        break
if is_palindrome:
    print("the given word is a palindrome")
else:
    print("the given word is not a palindrome")

#second method
word=input()
reverse_string=word[ : :-1]
if reverse_string==word:
    print("the given is word is palindrome")
else:
    print("the given is not palindrome")

#third method
word=input()
reverse=""
for i in word:
    reverse=i+reverse
if reverse==word:
    print("the given word is a palindrome")
else:
    print("the given word is not a palindrome")
