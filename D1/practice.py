input_data=input()
row=int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1
steps=[(-2, 1), (-1, -2)]

result=0
for step in steps:
    print(step[0])
