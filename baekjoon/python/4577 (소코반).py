import sys


def complete(socoban, target_pos):
    return all(socoban[pos[1]][pos[0]] == 'B' for pos in target_pos)


move = {"U": (0, -1), 
        "D": (0, 1), 
        "L": (-1, 0),
        "R": (1, 0)
        }

game_cnt = 0

while True:
    game_cnt += 1
    R, C = map(int, sys.stdin.readline().split())
    if R == 0 and C == 0:
        break
    
    map_data, target_pos = [], []
    character_pos = None
    target_flag = False
    game_end_flag = False
    
    for i in range(R):
        row = []
        data = sys.stdin.readline().rstrip()
        for j in range(C):
            row.append(data[j])
            if data[j] == "w":
                character_pos = (j, i)
            elif data[j] == "W":
                character_pos = (j, i)
                target_flag = True
            elif data[j] in ["+", "W", "B"]:
                target_pos.append((j, i))
        map_data.append(row)
                    
    movement_data = sys.stdin.readline().rstrip()
                
    for movement in movement_data:     
        x, y = character_pos
        dx, dy = move[movement]
        temp_x, temp_y = x + dx, y + dy
        
        if temp_y < 0 or temp_y >= R or temp_x < 0 or temp_x >= C or map_data[temp_y][temp_x] == "#":
            continue
        
        elif map_data[temp_y][temp_x] == "b":
            next_x, next_y = temp_x + dx, temp_y + dy
            if next_y < 0 or next_y >= R or next_x < 0 or next_x >= C:
                continue
            
            elif target_flag and map_data[next_y][next_x] == ".":
                character_pos = (temp_x, temp_y)
                target_flag = False
                map_data[y][x] = "+"
                map_data[temp_y][temp_x] = "w"
                map_data[next_y][next_x] = "b"
                
            elif map_data[next_y][next_x] == ".":
                character_pos = (temp_x, temp_y)
                map_data[y][x] = "."
                map_data[temp_y][temp_x] = "w"
                map_data[next_y][next_x] = "b"
                    
            elif target_flag and map_data[next_y][next_x] == "+":
                character_pos = (temp_x, temp_y)
                target_flag = False
                map_data[y][x] = "+"
                map_data[temp_y][temp_x] = "w"
                map_data[next_y][next_x] = "B"
            
            elif map_data[next_y][next_x] == "+":
                character_pos = (temp_x, temp_y)
                map_data[y][x] = "."
                map_data[temp_y][temp_x] = "w"
                map_data[next_y][next_x] = "B"
                
        elif map_data[temp_y][temp_x] == "B":
            next_x, next_y = temp_x + dx, temp_y + dy
            if next_y < 0 or next_y >= R or next_x < 0 or next_x >= C:
                continue
            
            elif target_flag and map_data[next_y][next_x] == ".":
                character_pos = (temp_x, temp_y)
                map_data[y][x] = "+"
                map_data[temp_y][temp_x] = "W"
                map_data[next_y][next_x] = "b"
                
            elif map_data[next_y][next_x] == ".":
                character_pos = (temp_x, temp_y)
                target_flag = True
                map_data[y][x] = "."
                map_data[temp_y][temp_x] = "W"
                map_data[next_y][next_x] = "b"
                    
            elif target_flag and map_data[next_y][next_x] == "+":
                character_pos = (temp_x, temp_y)
                map_data[y][x] = "+"
                map_data[temp_y][temp_x] = "W"
                map_data[next_y][next_x] = "B"
                
            elif map_data[next_y][next_x] == "+":
                character_pos = (temp_x, temp_y)
                target_flag = True
                map_data[y][x] = "."
                map_data[temp_y][temp_x] = "W"
                map_data[next_y][next_x] = "B"
                
        elif target_flag and map_data[temp_y][temp_x] == "+":
            character_pos = (temp_x, temp_y)
            map_data[y][x] = "+"
            map_data[temp_y][temp_x] = "W"
            
        elif map_data[temp_y][temp_x] == "+":
            character_pos = (temp_x, temp_y)
            target_flag = True
            map_data[y][x] = "."
            map_data[temp_y][temp_x] = "W"
        
        elif target_flag and map_data[temp_y][temp_x] == ".":
            character_pos = (temp_x, temp_y)
            target_flag = False
            map_data[y][x] = "+"
            map_data[temp_y][temp_x] = "w"
        
        elif map_data[temp_y][temp_x] == ".":
            character_pos = (temp_x, temp_y)
            map_data[y][x] = "."
            map_data[temp_y][temp_x] = "w"
        
        if complete(map_data, target_pos):
            print(f'Game {game_cnt}: complete')
            for row in map_data:
                print(''.join(row))
            game_end_flag = True
            break
    
    if game_end_flag:
        continue
    
    elif complete(map_data, target_pos):
        print(f'Game {game_cnt}: complete')
        for row in map_data:
            print(''.join(row))

    else:
        print(f'Game {game_cnt}: incomplete')
        for row in map_data:
            print(''.join(row))