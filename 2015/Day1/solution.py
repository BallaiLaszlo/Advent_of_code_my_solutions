input_text=""
res=0
with open("input.txt","r",encoding="utf-8") as input:
    for char in input:
        input_text=input_text+char
counter=0
for char in input_text:
        counter+=1
        if char == "(" or res<0:
            res=res+1
        elif char==")":
            res=res-1
        if res<0:
            break


print(res) #part1
print(counter)#part2
