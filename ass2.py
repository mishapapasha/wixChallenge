road = ">>><>v<v<>>>^<v<vv^v>v^^^v><vvv<>^v<<v>^^<vv^<>>v^v>>v^>><^<<>v^^>^v>^>>^v>vv>><vv<^v><vv^v^>v^^<v><><<v^<vv><<^vv^^v^v<v><<vvv<^>><v^^<^<>>vv<<<^^v>><vv^^vv>v<>^^^^>>>>v^><^>>><><<<v>vvv<>v^^^<vv<^v>^^^^>v<>v<v^><<>>^^^<^<<>>v<v<>^^<v^^<^<^<v>vvvvv>v^>^>>v^v^vvv>v<^v^v>v<v<^^vv<<^<>v<<>v<<^v>v^<<v<><<^>^^<v^^<<>^v>v<><<<^>>^>^^^<>>vvv>^<v^v>>v<v<^<>>>>v^^<^vv<>^<<v^>>>><v>^>>^^v^>>v<^v<v<^^<v<<<^^vv<>><v<<^^vv^v^<<v^>^>v^<^^>^^v>v^<^>^>><>^>^vv>>>vv>>^^>^<>>v^><<^v<><>^<v^v>v^><^^^^>>v>^<vv>^>^vv^v^^^>^v>v>>>vv<<^<>>>^<v^>^>>>v^vv>>>v<>>>><^v^<vvvv><v>><>>vv>vv<<><^^<>^^<v<<<>><<<>v>vv>>^^^^^<v<>^>>v^<v^<v<>>vv<>vv^<<^v<v><>><>^<v>v^v>>>^v^^>><vvv^<vv<^>vv^v<<^v^<<v<vvv<v^^<>>vv^>>>v<^^^><^v^^vvv<<^vv>>>>>v>v<^<^^^><>^<><^vvv>^>v<^>^v<>^>^v^>vv<v<v<^^v<>^^v<>^<^v><>v<vv^<<>><><vv>v>vv>^v^>v>v^v^vvv^v^v<v>^<<^<>v>^<>v<v<<<<v>v^v>v<^<>>>^>>>v><vv<^vv<^v<vv<>>>>>>^>>>^><<<><v>^^><>^<v<<<>vv>^<v><>v<<<v>>vv<><^>>v^v^><>vv^v>^^^v>^^^v>^v^v>^v^<<<<<vvv><<>vv^<v<<<>vv><^<<>vvv>v^^>>><>>vv^^><vv^^^<<<>vv^^<>>^^^<><^>^<>>^<<<^v>>v<>^>^v><v^>^<v><vv^v^><vvv<<vv^v>vv<<^v<>^<>>^v>>>vv<>>^><><^<<^^v>^^<<v^v^<v^^^vvv<v^v^^<<vv<v<<^v<>>>vv><v^^^vv^<v>v^^^>^<<>^>><vv^<>^^><<>v><v>>vv>>>>v^>>^vv^v<v^<vvv>^<<^^v>v<v>>>>v>^^<<v^^>^<v<^vv<>^>^><<>vv>^v<^vvv^^>>>vv<v^<<<^<>vv><^<>vv<>^>v^v<>v^<>>v<^^>^>^<^<>v>v><v^>><v^v<v^<v>^^vv>v<v>vvv^v^v>^><v^^><>>^<v^<^<v^v<v<^"
posX = 0
posY = 0
points = {}

def positionUpdate(dir):
    global posX, posY
    if dir == '^':
        posY += 1
    elif dir == 'v':
        posY -= 1
    elif dir == '>':
        posX += 1
    elif dir == '<':
        posX -=1
        
points[str([0, 0])] = 1
for dir in road:
    positionUpdate(dir)
    ##print("posX: " + str(posX) + "\t posY " + str(posY))
    position = str([posX, posY])
    if position in  points:
        points[position] += 1
    else:
        points[position] = 1
        
print('All points: {0}'.format(len(points)))

answer = 0
for i in points:
    if points[i] > 1:
        answer += 1
print('Answer: {0}'.format(answer))
