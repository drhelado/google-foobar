import math

class cell:
    def __init__(self, x = 0, y = 0, dist = 0):
        self.x = x
        self.y =y
        self.dist = dist

def pos_to_coords(pos):
    x = int(math.floor(pos/8))
    y = int(pos % 8)
    return (x, y)

def is_inside(x, y, n):
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    return False

def solution(src, dest):
    #Your code here
    _src, _dest = [0, 0], [0, 0]

    _src[0], _src[1] = pos_to_coords(src)
    _dest[0], _dest[1] = pos_to_coords(dest)

    src = _src
    dest = _dest


    n = 8

    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]

    queue = []

    queue.append(cell(src[0], src[1], 0))

    visited = [[False for i in range(n)] for j in range(n)]

    visited[src[0]][src[1]] = True

    while queue:
        t = queue[0]
        queue.pop(0)

        if t.x == dest[0] and t.y == dest[1]:
            return t.dist

        for i in range(n):
            x = t.x + dx[i]
            y = t.y + dy[i]

            if is_inside(x, y, n):
                # and not visited[x][y]:
                visited[x][y] = True
                queue.append(cell(x, y, t.dist + 1))

_solution = solution(0, 1)
print(_solution)
