class Node:
    def __init__(self, char) -> None:
        self.char = char
        self.is_end = False

        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = Node("")

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = Node(char)
                node.children[char] = new_node
                node = new_node

        node.is_end = True


f = open("word_list.txt", "r")

t = Trie()
for line in f:
    t.insert(line.strip())


def grid_parser(game_spawn: str, n=4) -> list(list[str]):
    return_arr = []
    tmp_arr = []
    for i in range(n * n):
        if i % n == n - 1:
            tmp_arr.append(game_spawn[i])
            return_arr.append(tmp_arr)
            tmp_arr = []
        else:
            tmp_arr.append(game_spawn[i])
    return return_arr


def get_solves() -> None:
    prompt = input("prompt: ")
    rows = int(input("rows: "))
    grid = grid_parser(prompt, rows)
    words = []
    visited = [[0] * rows for _ in range(rows)]  # Initialize as distinct lists

    def dfs(x, y, prefix, node):
        # out of range
        if x < 0 or x >= rows or y < 0 or y >= rows:
            return
        if visited[x][y] == 1:
            return
        prefix += grid[x][y]
        if not node.children.get(grid[x][y]):
            return
        node = node.children[grid[x][y]]

        if node.is_end and prefix not in words:
            words.append(prefix)

        visited[x][y] = 1  # Update visited status for the current cell

        dfs(x + 1, y, prefix, node)
        dfs(x - 1, y, prefix, node)
        dfs(x, y + 1, prefix, node)
        dfs(x, y - 1, prefix, node)
        dfs(x + 1, y + 1, prefix, node)
        dfs(x - 1, y - 1, prefix, node)
        dfs(x + 1, y - 1, prefix, node)
        dfs(x - 1, y + 1, prefix, node)

        visited[x][y] = 0  # Reset visited status for backtracking

    for i in range(rows):
        for j in range(rows):
            dfs(i, j, "", t.root)
            visited = [
                [0] * rows for _ in range(rows)
            ]  # Reset visited for each starting position

    words.sort(key=len)
    for i in words:
        print(i)


get_solves()
