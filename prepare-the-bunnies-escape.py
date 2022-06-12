
def answer(map):
    rows, cols = len(map), len(map[0])

    def bfs(r, c):
        matrix = [[None for i in range(cols)] for i in range(rows)]
        matrix[r][c] = 1

        queue = [(r, c)]
        directions = [[1,0], [-1,0], [0,-1], [0,1]]
        while queue:
            r, c = queue.pop(0)

            for d in directions:
                dr, dc = r + d[0], c + d[1]

                if not (rows > dr >= 0) or not (cols > dc >= 0) or matrix[dr][dc] is not None:
                    continue

                matrix[dr][dc] = matrix[r][c] + 1

                if map[dr][dc] != 1:
                    queue.append((dr, dc))

        return matrix

    top_down = bfs(0, 0)
    bottom_up = bfs(rows - 1, cols - 1)

    # matrix = []

    # output = 2 ** 32 - 1
    output = float('inf')

    for r in range(rows):
        for c in range(cols):
            if top_down[r][c] and bottom_up[r][c]:
                output = min(top_down[r][c] + bottom_up[r][c] - 1, output)

    return output


maze = [[0, 0, 0, 0, 0, 0],[1, 1, 1, 1, 1, 0],[1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0]] #Answer 21
#maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]] #Answer 7
#maze = [[0,1,0,0,0],[0,0,0,1,0],[1,1,1,1,0]] #Answer 7
# maze = [[0,1,1,1],[0,1,0,0],[1,0,1,0],[1,1,0,0]] #Answer 7
# maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]] #Answer 11
# maze = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
print(answer(maze))
