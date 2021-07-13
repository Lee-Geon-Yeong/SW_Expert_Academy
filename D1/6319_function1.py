Word = input()
print(Word)
if list(Word) == list(reversed((Word))) : 
    print("입력하신 단어는 회문(Palindrome)입니다.")

