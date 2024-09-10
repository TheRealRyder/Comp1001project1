def quad_clockwise_spiral_paths(dimension, time_step):
    row_size, col_size = dimension
    
    paths = [["right", (0,0)],["bottom", (0, col_size-1)],["left", (row_size-1, col_size-1)],["top", (row_size-1, 0)]]
    
    boundary = {"right":col_size - 2, "bottom": row_size -2, "left": 1,"top": 1}

    current_paths = [[0,0],[0, col_size-1], [row_size-1, col_size-1], [row_size-1, 0]]
    
    stopped = [False, False, False, False]
    
    for i in range(time_step):
        for index, path in enumerate(paths[:]):
        
            
            if path[0] == "right":
                if stopped[index] == True:
                    continue
                elif current_paths[index][1]  != boundary["right"]:
                    
                    current_paths[index][1] += 1      
                elif any((current_paths[index][0]+1,current_paths[index][1]) in p[1:] for p in paths) :
                    stopped[index] = True
                    continue
                else:
                    path[0] = "bottom"
                    boundary["right"] -= 1
                    
            if path[0] == "bottom":
                if stopped[index] == True:
                    continue
                elif current_paths[index][0]  != boundary["bottom"]:
                    
                    current_paths[index][0] += 1
                elif any((current_paths[index][0], current_paths[index][1]-1) in p[1:] for p in paths) :
                    stopped[index] = True
                    continue
                else:
                    path[0] = "left"
                    
                    boundary["bottom"] -= 1
                        
                    
            if path[0] == "left":
                
                if stopped[index] == True:
                    continue
                elif current_paths[index][1] != boundary["left"]:
                    
                    
                    current_paths[index][1] -= 1
                elif any((current_paths[index][0]-1, current_paths[index][1]) in p[1:] for p in paths) :
                    
                    stopped[index] = True
                    continue
                else:
                    path[0] = "top"
                    boundary["left"] += 1
                    
            if path[0] == "top":
                
                if stopped[index] == True:
                    
                    continue
                elif current_paths[index][0] != boundary["top"]:
                    
                    current_paths[index][0] -= 1
                elif any((current_paths[index][0], current_paths[index][1]+1) in p[1:] for p in paths) :
                    
                    stopped[index] = True
                    continue
                else:
                    
                    path[0] = "right"
                    boundary["top"] += 1
                    
                    current_paths[index][1] += 1
            path.append((current_paths[index][0], current_paths[index][1]))
    for path in paths:
        del path[0]
    return paths
dimension = (7, 5)
paths_t0 = quad_clockwise_spiral_paths(dimension, 0)
paths_t3 = quad_clockwise_spiral_paths(dimension, 3)
paths_t12 = quad_clockwise_spiral_paths(dimension, 12)   
'''print(paths_t0)
print(paths_t3)'''
print(paths_t12)
