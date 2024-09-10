dimension = (7, 5)
paths = [ ["right", (0,0)], ["down", (0, dimension[1])], ["left", (dimension[0], dimension[1])], ["up", (dimension[0], 0 )]]
print(any(map(lambda path: (0,0) in path,
              filter(lambda path: path != path[0], paths))))

print(list(enumerate(paths[1])))