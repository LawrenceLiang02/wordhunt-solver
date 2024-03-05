import os
import json

# Load dictionary files
dictionary_path = "dictionary"
dictionary_files = os.listdir(dictionary_path)
word_set = set()

for file_name in dictionary_files:
    with open(os.path.join(dictionary_path, file_name), 'r') as file:
        words = json.load(file)
        for word_obj in words:
            word_set.add(word_obj['word'].lower())

# Define directions
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

# Define board
board = [
    ['n', 'i', 'i', 'h'],
    ['t', 'e', 'c', 'h'],
    ['d', 'l', 's', 'g'],
    ['a', 'l', 'o', 's']
]

def is_valid(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def dfs(x, y, visited, current_word, found_words):
    if not is_valid(x, y) or visited[x][y]:
        return

    current_word += board[x][y]
    if len(current_word) >= 3 and current_word.lower() in word_set:
        found_words.add(current_word.lower())

    visited[x][y] = True
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        dfs(new_x, new_y, visited, current_word, found_words)
    visited[x][y] = False

def find_words():
    visited = [[False] * 4 for _ in range(4)]
    found_words = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, visited, "", found_words)
    return sorted(found_words, key=len, reverse=True)

found_words = find_words()
print("Found words (longest first):")
for word in found_words:
    print(word)
