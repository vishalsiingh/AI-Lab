# Problem Statement:
# Given a grid-based maze where 0 represents walls and 1 represents walkable paths, 
# find the shortest path from a start cell to an end cell.

# Tasks:
# Use BFS to find the shortest path.
# Use DFS to explore all possible paths and report one valid path (not necessarily the shortest).
# Compare the number of nodes explored by BFS and DFS.


# import queue

# def createMaze():
# maze = []
# maze.append(["#","#", "#7, "#", "#7, "0", §"])
# maze.append(["#"," w, wom mou ugw won onguy)
# maze.append(["#"," v, "fn, nn, nwgw wn ngu])
# maze.append(["#"," *, "fn, nn ww wn nfe])
# maze.append (["#"," ", "#", "#", "#v, vv, "§"'])
# maze.append (["#"," *, " ", " ", vhv, © 0, v40])
# maze.append (["#","#", "#", "#", "§v, "xX", "§])
# return maze

# def createMaze2():
# maze = []
# maze.append (["#","#", "#§", "#v, "fv, von, "gv, viv, w#1)|
# maze.append(["#",6" ., " ., Ll w, " ., " ., Ll ", ” ., "“#"1)
# maze.append(["#"," v, "fn, "gv, wow ugn nfgn ww wgn])
# maze.append (["#"," ", "ign, LBL LAL nie, "ae "§"1)
# maze.append(["#"," ", "#", " v, "&", vv ", "#7, vv, "E§"])
# maze.append(["#"," ., nw, n ", gr, " » nw, ” -, #1)
# maze.append(["#"," ", nie, ” ", nije, " .. Ll LN nie, "§n1)
# maze.append(["#"," .. " », Ll w, " », "w ", " ., " ., "$"])
# maze.append (["#","#", "#", "#v, v§v, vgn, ngr, vx, wgn])
# return maze

# def printMaze (maze, path=""):
# for x, pos in enumerate (maze[0]):

# if pos == "0":
# start = x

# i = start
# nums = queue.Queue()
# nums .put ("")
# add = ""
# maze = ()
# while not findEnd(maze, add):
# add = nums.get()
# #print (add)
# for j in ["L", "R", "U"", "D"]:
# put = add + j
# if valid(maze, put):
# nuns.put(put)

import queue
q=queue.Queue()
q.put("0")
q.put("1")

for _ in range(15):
    x=q.get()
    print(x)
    q.put(x+ "0")
    q.put(x+ "1")
    
