  
'''
A* Pathfinding
-calculating score
where X = Y + Z
Y = cost of movement from starting point
Z = estimated score from ending point
'''


# !/usr/bin/python

def find(l, elem):
    for row, i in enumerate(l):
        try:
            column = i.index(elem)
        except ValueError:
            continue
        return [row, column]
    return -1


def displayPathtoPrincess(n, grid):
    try:
        princess_location = find(grid, "p")
        player_location = find(grid, "m")
        while player_location != princess_location:
            scoreboard = []
            coordinates = []
            x, y = player_location
            down, up, right, left = [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]
            movement = ['DOWN', 'UP', 'RIGHT', 'LEFT']

            for move in [down, up, right, left]:
                score_to_goal = abs(princess_location[0]-move[0]) + abs(princess_location[1]-move[1])                
                scoreboard.append(score_to_goal)
                coordinates.append(move)

            best_move = min(scoreboard)
            next_move = scoreboard.index(best_move)
            player_location = coordinates[next_move]
            print(movement[next_move])
    except:
        pass


m = int(input())
grid = []

for i in range(0, m):
    grid.append(list(input()))

displayPathtoPrincess(m, grid)
