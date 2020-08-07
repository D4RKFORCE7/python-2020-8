a = int(input('How large do you want your map? 3,5 or 7?:'))
if a == 3:
  board = ['_', '_', '_',
          '_', '_', '_',
          '_', '_', '_',]
elif a == 5:
  board = ['_', '_', '_', '_', '_'
          '_', '_', '_', '_', '_'
          '_', '_', '_', '_', '_']
elif a == 7:
  board = ['_', '_', '_', '_', '_', '_', '_' 
          '_', '_', '_', '_', '_', '_', '_',
          '_', '_', '_', '_', '_', '_', '_']
else:
  print('Stop, get some help.')

def tic_tac_toe3():
  print(' _'*3)
  print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|')
  print('|' + board[3] + '|' + board[4] + '|' + board[5] + '|')
  print('|' + board[6] + '|' + board[7] + '|' + board[8] + '|')

def tic_tac_toe5():
  print(' _'*5)
  print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|' + board[3] + '|'+ board[4] + '|')
  print('|' + board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8] + '|'+ board[9] + '|')
  print('|' + board[10] + '|' + board[11] + '|' + board[12] + '|' + board[13] + '|'+ board[14] + '|')
  print('|' + board[15] + '|' + board[16] + '|' + board[17] + '|' + board[18] + '|'+ board[19] + '|')
  print('|' + board[20] + '|' + board[21] + '|' + board[22] + '|' + board[23] + '|'+ board[24] + '|')

def tic_tac_toe7():
  print(' _'*7)
  print('|' + board[0] + '|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|' + board[5] + '|' + board[6] + '|')
  print('|' + board[7] + '|' + board[8] + '|' + board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12] + '|' + board[13] + '|')
  print('|' + board[14] + '|' + board[15] + '|' + board[16] + '|' + board[17] + '|' + board[18] + '|' + board[19] + '|' + board[20] + '|')
  print('|' + board[21] + '|' + board[22] + '|' + board[23] + '|' + board[24] + '|' + board[25] + '|' + board[26] + '|' + board[27] + '|')
  print('|' + board[28] + '|' + board[29] + '|' + board[30] + '|' + board[31] + '|' + board[32] + '|' + board[33] + '|' + board[34] + '|')
  print('|' + board[35] + '|' + board[36] + '|' + board[37] + '|' + board[38] + '|' + board[39] + '|' + board[40] + '|' + board[41] + '|')  
  print('|' + board[42] + '|' + board[43] + '|' + board[44] + '|' + board[45] + '|' + board[46] + '|' + board[47] + '|' + board[48] + '|')

if a == 3:
  tic_tac_toe3()
elif a == 5:
  tic_tac_toe5()
elif a == 5:
  tic_tac_toe7()


while True:
  o = int(input('Player 1, make your move:'))

  b = 1

  if a == 3:
    b = 1
    for i in range(9):
        if o == b:
          board[b - 1] = 'O'
          tic_tac_toe3()
        b = b + 1

  if a == 5:
    b = 1
    for i in range(25):
        if o == b:
          board[b - 1] = 'O'
          tic_tac_toe5()
        b = b + 1
        

    
  
  if a == 7:
    b = 1
    for i in range(49):

        if o == b:
          board[b - 1] = 'O'
          tic_tac_toe7()
        b = b + 1

  if board[0] == board[1] == board[2] != '_':
    print('Game Over')
    break
  elif board[3] == board[4] == board[5] != '_':
    print('Game Over')
    break
  elif board[6] == board[7] == board[8] != '_':
    print('Game Over')
    break
  elif board[0] == board[3] == board[6] != '_':
    print('Game Over')
    break
  elif board[1] == board[4] == board[7] != '_':
    print('Game Over')
    break
  elif board[0] == board[4] == board[8] != '_':
    print('Game Over')
    break
  elif board[2] == board[5] == board[8] != '_':
    print('Game Over')
    break
  elif board[2] == board[4] == board[6] != '_':
    print('Game Over')
    break
  
            
  x = int(input('Player 2, make your move:'))
  u = 1
  if a == 3:
    for i in range(9):
      if x == u:
        board[u - 1] = 'x'
        tic_tac_toe3()
      u = u + 1
      
  if a == 5:
    for i in range(25):
      if x == u:
        board[u - 1] = 'x'
        tic_tac_toe5()
      u = u + 1

  if a == 7:
    for i in range(49):
      if x == u:
        board[u - 1] = 'x'
        tic_tac_toe7()
      u = u + 1
  
  if board[0] == board[1] == board[2] != '_':
    print('Game Over')
    break
  elif board[3] == board[4] == board[5] != '_':
    print('Game Over')
    break
  elif board[6] == board[7] == board[8] != '_':
    print('Game Over')
    break
  elif board[0] == board[3] == board[6] != '_':
    print('Game Over')
    break
  elif board[1] == board[4] == board[7] != '_':
    print('Game Over')
    break
  elif board[0] == board[4] == board[8] != '_':
    print('Game Over')
    break
  elif board[2] == board[5] == board[8] != '_':
    print('Game Over')
    break
  elif board[2] == board[4] == board[6] != '_':
    print('Game Over')
    break
  
            
            