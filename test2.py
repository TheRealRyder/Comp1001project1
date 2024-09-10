ORANGE = '\U0001F7E7'
BLUE = '\U0001F7E6'
GREEN = '\U0001F7E9'
PURPLE = '\U0001F7EA'
WHITE = '\U00002B1C'
SQUARES = [ORANGE, GREEN, BLUE, PURPLE]
# ---------- DEFINE YOUR CONSTANTS AFTER THIS LINE  ----------

# ---------- DEFINE YOUR CONSTANTS BEFORE THIS LINE ----------
#CHANGED THE WAY OF CHEKCING WITHIN THE PATHS, NOW NEED TO STOP OVERLAP FOR PATHS WITH TOO BIG OF A BOUNDARY 
def visualise_paths(paths, dimension):
    
    '''Take a list with four paths and the dimension, print out the visualised
       version of it. Shaanan, Yige, Han and Rose's path are printed out in 
       orange, green, blue and purple respectively. Unvisited coordinates are 
       printed in white.'''

    row_dim, col_dim = dimension
    backyard = [[WHITE for _ in range(col_dim)] for _ in range(row_dim)]

    # create the backyard represented by coloured squares
    for mower_i, mower_path in enumerate(paths):
        for x, y in mower_path:
            backyard[x][y] = SQUARES[mower_i]

    # print out the backyard
    for row in backyard:
        line = ''
        for col in row:
            line += col
        print(line)

# ------------- WRITE YOUR SOLUTION AFTER THIS LINE ---------------
# This was copy and pasted from my work in VSCode, evidence of work 
# is in my github repository https://github.com/TheRealRyder/Comp1001project1
def quad_clockwise_spiral_paths(dimension, time_step):
    """accepts tuple of ints "dimension" and int "time_step" and produces 
    4 spiral paths at a given time each starting from the boundaries 
    of the given dimensions returning a list of the 4 lists each 
    containing tuples"""
    # Initialize paths with directions and 3 other containers, in order
    # of the 4 mowers, to help computing the mowers movement along the grid
    row_size, col_size = dimension
    
    paths = [["right", (0, 0)], ["bottom", (0, col_size - 1)], ["left", 
                    (row_size - 1, col_size - 1)], ["top", (row_size - 1, 0)]]
    
    boundary = {"right": col_size - 2, "bottom": row_size - 2,
                    "left": 1, "top": 1}

    current_paths = [[0, 0], [0, col_size - 1], [row_size - 1, col_size - 1], 
                     [row_size - 1, 0]]
    
    visited = set()
    
    stopped = [False, False, False, False]
    # Loop by the amount of the given time
    for i in range(time_step):
        # For each time step append a new tuple in each path of paths
        # using the index of path to find and modify its other variables
        for index, path in enumerate(paths[:]):
            # For each path check for its current direction, if True check if 
            # the most recent tuple is within its limits and modify future 
            # tuple or direction accordingly if our of limits stop current and 
            # any future tuples from being added
            
            if path[0] == "right":
                if stopped[index] is True:
                    continue
                elif current_paths[index][1]  < boundary["right"] and (current_paths[index][0], current_paths[index][1] + 1) not in visited:
                    
                    current_paths[index][1] += 1      
                elif (current_paths[index][0] + 1, current_paths[index][1]) in visited: 
                    stopped[index] = True
                    continue
                else:
                    path[0] = "bottom"
                    boundary["right"] -= 1
                    
            if path[0] == "bottom":
                if stopped[index] is True:
                    continue
                elif current_paths[index][0]  < boundary["bottom"] and (current_paths[index][0] + 1, current_paths[index][1]) not in visited:
                    
                    current_paths[index][0] += 1
                elif (current_paths[index][0], current_paths[index][1]-1) in visited:
                    stopped[index] = True
                    continue
                else:
                    path[0] = "left"
                    
                    boundary["bottom"] -= 1
                        
                    
            if path[0] == "left":
                
                if stopped[index] is True:
                    continue
                elif current_paths[index][1] > boundary["left"] and (current_paths[index][0], current_paths[index][1] - 1 ) not in visited:
                    
                    
                    current_paths[index][1] -= 1
                elif (current_paths[index][0]-1, current_paths[index][1]) in visited:
                    
                    stopped[index] = True
                    continue
                else:
                    path[0] = "top"
                    boundary["left"] += 1
                    
            if path[0] == "top":
                
                if stopped[index] is True:
                    
                    continue
                elif current_paths[index][0] > boundary["top"] and (current_paths[index][0] - 1, current_paths[index][1]  ) not in visited:
                    
                    current_paths[index][0] -= 1
                elif (current_paths[index][0], current_paths[index][1] + 1) in visited:
                    
                    stopped[index] = True
                    continue
                else:
                    
                    path[0] = "right"
                    boundary["top"] += 1
                    # added increase as current tuple did non move
                    current_paths[index][1] += 1
                    
            path.append((current_paths[index][0], current_paths[index][1]))
            visited.add((current_paths[index][0], current_paths[index][1]))
    # Finally, remove added directions in each paths before returning 
    for path in paths:
        del path[0]
    return paths

dimension = (10,5) 
paths_t12 = quad_clockwise_spiral_paths(dimension, 30)
print(paths_t12)
visualise_paths(paths_t12, dimension)        