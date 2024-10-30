grid = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def adding_values(row, column, current_player):
  grid[row][column] = current_player


def checking_for_winner(row, column, current_player):
  if (grid[row][0] == grid[row][1] == grid[row][2] == current_player) or (
      grid[0][column] == grid[1][column] == grid[2][column] == current_player
  ) or (grid[0][2] == grid[1][1] == grid[2][0] == current_player) or (
      grid[0][0] == grid[1][1] == grid[2][2] == current_player):
    print("Won")
    return True
  else:
    new_grid = []
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        new_grid.append(grid[i][j])
  for row in grid:
    for cell in row:
      if cell == "_":
        return False
  print("The game is a tie.")
  return True


def print_board():
  for i in range(len(grid)):
    k = ""
    for j in range(len(grid[0])):
      k += grid[i][j]
    print(k)


current_player = "o"
while True:
  print("It is currently player %s's turn" % (current_player))
  x_coordinate = int(input("Enter a number  between 0 and 2: "))
  y_coordinate = int(input("Enter a number  between 0 and 2: "))
  if grid[x_coordinate][y_coordinate] != "_":
    print("This space is already taken. Please enter a different coordinate.")
    continue

  adding_values(x_coordinate, y_coordinate, current_player)
  print_board()
  if checking_for_winner(x_coordinate, y_coordinate, current_player):
    break
  if current_player == "x":
    current_player = "o"
  else:
    current_player = "x"
