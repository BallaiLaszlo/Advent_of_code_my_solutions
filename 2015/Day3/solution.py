input_text=""
with open("input.txt","r",encoding="utf-8") as input:
    for char in input:
        input_text=input_text+char
print(input_text)

x,y =0,0
visited_houses={(x,y)}

for char in input_text:
    if char == "^":
        y+=1
    elif char == "V":
        y-=1
    elif char == ">":
        x+=1
    elif char == "<":
        x -= 1
    visited_houses.add((x,y))

print(len(visited_houses))