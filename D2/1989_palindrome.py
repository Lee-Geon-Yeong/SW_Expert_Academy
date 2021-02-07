T=int(input())
for i in range(1, T+1):
    word=input()
    answer=1
    first = 0
    last = len(word)-1
    for j in range(len(word)//2):
        if word[first] != word[last]:
            answer=0
        first+=1
        last-=1
    print(f"#{i} {answer}")