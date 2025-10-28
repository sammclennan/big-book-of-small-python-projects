# Hungry Robots game

import random
import sys

WIDTH = 40
HEIGHT = 20
WALL_DENSITY = 0.5
NUM_ROBOTS = 4
DEAD_ROBOTS = 2

WALL = '░'
PLAYER = '@'
ROBOT = 'R'
DEAD_ROBOT = 'X'

# Get random coords
def get_coords(used_coords, min_distance=None, ref_coords=None):
    while True:
        coords = [random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2)]

        # Prevent overlapping coords
        if coords not in used_coords:
            if min_distance and ref_coords:
                if (
                    abs(ref_coords[0] - coords[0]) < min_distance and abs(ref_coords[1] - coords[1]) < min_distance
                ):
                    continue

            used_coords.append(coords)
            return coords


# Get move from player
def get_move(movement_keys):
    while True:
        for i, key in enumerate(movement_keys, start=1):
            print(f"({key if movement_keys[key] else ' '})", end='')
            if i % 3 == 0: print() 

        print('Enter move or QUIT:')
        player_move = input('> ').upper()

        if player_move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif (player_move == 'T' and teleports > 0) or (player_move in (movement_keys) and movement_keys[player_move]):
            return player_move


# Get possible movements
def possible_moves(coords, obstacles=WALL):
    moves = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 0), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    valid_moves = {}

    for move in moves:
        dy, dx = move
        if playing_field[coords[0] + dy][coords[1] + dx] not in obstacles:
            valid_moves[move] = True
        else:
            valid_moves[move] = False

    return valid_moves


# Create 2D array for playing field
playing_field = [[WALL] * WIDTH]
for i in range(1, HEIGHT - 1):
    playing_field.append([WALL])
    playing_field[i].extend(random.choices([WALL, ' '], weights=[WALL_DENSITY/2, 1 - WALL_DENSITY/2], k=WIDTH - 2))
    playing_field[i].append(WALL)
playing_field.append([WALL] * WIDTH)

# Keep track of existing coordinates
used_coords = []

# Get player coords
player_coords = get_coords(used_coords)
robot_coords = [{'coords': get_coords(used_coords, 4, player_coords), 'alive': True} for i in range(NUM_ROBOTS)]
dead_robot_coords = [get_coords(used_coords) for i in range(DEAD_ROBOTS)]

teleports = 2

while True:
    # Draw sprites on playing field
    playing_field[player_coords[0]][player_coords[1]] = PLAYER
    for robot in robot_coords:
        playing_field[robot['coords'][0]][robot['coords'][1]] = ROBOT if robot['alive'] else DEAD_ROBOT
    for coords in dead_robot_coords:
        playing_field[coords[0]][coords[1]] = DEAD_ROBOT

    # Print playing field
    for row in playing_field:
        print(''.join(row))
    print(f'(T)eleports remaining: {teleports}')

    # Check for win or lose condition
    live_robot_count = 0
    for i in range(len(robot_coords)):
        if robot_coords[i]['alive']:
            if robot_coords[i]['coords'] == player_coords:
                print("Oh no! You got caught by a robot!")
                sys.exit()        
            live_robot_count += 1
    
    if live_robot_count == 0:
        print('Congratulations! You beat all the robots!')
        sys.exit()

    # Get possible movements as movement keys
    movement_keys = dict(zip('QWEASDZXC', possible_moves(player_coords, obstacles=(WALL, DEAD_ROBOT)).values()))

    # Clear previous coordinates
    playing_field[player_coords[0]][player_coords[1]] = ' '
    for i in range(len(robot_coords)):
        playing_field[robot_coords[i]['coords'][0]][robot_coords[i]['coords'][1]] = ' '

    # Get coordinates currently in use
    used_coords = []
    for i in range(len(robot_coords)):
        used_coords.append(robot_coords[i]['coords'])
    for coords in dead_robot_coords:
        used_coords.append(coords)

    # Get move from player
    player_move = get_move(movement_keys)

    # Adjust player coordinates
    if player_move == 'T':
        teleports -= 1
        player_coords = get_coords(used_coords)
        continue

    if player_move in ('Q', 'W', 'E'):
        player_coords[0] -= 1
    if player_move in ('Z', 'X', 'C'):
        player_coords[0] += 1
    if player_move in ('Q', 'A', 'Z'):
        player_coords[1] -= 1
    if player_move in ('E', 'D', 'C'):
        player_coords[1] += 1    

# Have robots chase player           
    for i in range(len(robot_coords)):
        if robot_coords[i]['alive']:
            robot_moves = possible_moves(robot_coords[i]['coords'])

            # Get change in robot x coords
            move_y = 1 if robot_coords[i]['coords'][0] < player_coords[0] else -1 if robot_coords[i]['coords'][0] > player_coords[0] else 0
            
            # Get change in robot y coords
            move_x = 1 if robot_coords[i]['coords'][1] < player_coords[1] else -1 if robot_coords[i]['coords'][1] > player_coords[1] else 0

            # Adjust robot coordinates
            if robot_moves.get((move_y, move_x), False):
                robot_coords[i]['coords'][0] += move_y
                robot_coords[i]['coords'][1] += move_x
            elif move_x == -1 and robot_moves[(0, -1)]:
                robot_coords[i]['coords'][1] -= 1
            elif move_x == 1 and robot_moves[(0, 1)]:
                robot_coords[i]['coords'][1] += 1
            elif move_y == -1 and robot_moves[(-1, 0)]:
                robot_coords[i]['coords'][0] -= 1
            elif move_y == 1 and robot_moves[(1, 0)]:
                robot_coords[i]['coords'][0] += 1

    # Check for robot collision
    for i in range(len(robot_coords)):
        if robot_coords[i]['coords'] in dead_robot_coords:
            robot_coords[i]['alive'] = False
        for j in range(i + 1, len(robot_coords)):
            if robot_coords[i]['coords'] == robot_coords[j]['coords']:
                robot_coords[i]['alive'] = False
                robot_coords[j]['alive'] = False


