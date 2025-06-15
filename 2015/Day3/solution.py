from operator import indexOf

input_text=""
with open("input.txt","r",encoding="utf-8") as input:
    for char in input:
        input_text=input_text+char
#print(input_text)

def count_houses_with_presents(moves):
    x, y = 0, 0
    visited = {(x, y)}
    for move in moves:
        if move == '^':
            y += 1
        elif move == 'v':
            y -= 1
        elif move == '>':
            x += 1
        elif move == '<':
            x -= 1
        visited.add((x, y))
    return len(visited)
#part1
print(count_houses_with_presents(input_text))

def count_houses_with_presents_super_santa(moves):
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    visited = {(santa_x, santa_y)}
    for i, move in enumerate(moves):
        if i % 2 == 0:  # Santa's turn
            if move == '^':
                santa_y += 1
            elif move == 'v':
                santa_y -= 1
            elif move == '>':
                santa_x += 1
            elif move == '<':
                santa_x -= 1
            visited.add((santa_x, santa_y))
        else:  # Robo-Santa's turn
            if move == '^':
                robo_y += 1
            elif move == 'v':
                robo_y -= 1
            elif move == '>':
                robo_x += 1
            elif move == '<':
                robo_x -= 1
            visited.add((robo_x, robo_y))
    return len(visited)


print(count_houses_with_presents_super_santa(input_text))
