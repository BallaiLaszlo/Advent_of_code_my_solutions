from array import array

text=""
length=[]
width=[]
height=[]
with open("input.txt","r",encoding="utf-8") as input:
        text=input.read()

for line in text.splitlines():
    length.append(int(line.split("x")[0]))
    width.append(int(line.split("x")[1]))
    height.append(int(line.split("x")[2]))

total_paper=0
total_ribbon=0
for i in range(len(length)):
    total_paper+=2*int(length[i])*int(width[i])+2*int(width[i])*int(height[i])+2*int(height[i])*int(length[i])+min(length[i] * width[i], width[i] * height[i], height[i] * length[i])
    smallest = int(min(length[i], width[i], height[i]))
    largest = int(max(length[i], width[i], height[i]))
    second_smallest = int((length[i] + width[i] + height[i]) - smallest - largest) # The remaining side
    total_ribbon+=length[i]*width[i]*height[i]+(smallest+smallest+second_smallest+second_smallest)

print(total_paper)#part1
print(total_ribbon)