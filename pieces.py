import pygame
import os

w=800
gap = w/8
black = ((0,0,0))
white = (255,255,255)







class rook:
	blackrook = pygame.image.load("blackrook.png") 
	whiterook = pygame.image.load("whiterook.png")

	def __init__(self, color):
		self.color = color
		if self.color == white:
			self.image = self.whiterook
		else:
			self.image = self.blackrook
		self.x = gap*.17
		self.y = gap*.15
		self.reachable = []

	def __repr__(self):
		return "R"

def checkLine(square, board):
	reachable = []
	row = square.y/gap
	col = square.x/gap
	left = col
	right = col
	up = row
	down = row
	while (left>-1):
		reachable.append(board[row][left])
		if ((board[row][left].piece is not None) and (board[row][left] is not square)):
			if board[row][left].piece.color != square.piece.color and str(board[row][left].piece) == "K":
				pass
			else:
				break
		left-=1
	while right<8:
		reachable.append(board[row][right]) 
		if ((board[row][right].piece is not None) and (board[row][right] is not square)):
			if board[row][right].piece.color != square.piece.color and str(board[row][right].piece) == "K":
				pass
			else:
				break
		right+=1
	while up > -1:
		reachable.append(board[up][col])
		if ((board[up][col].piece is not None) and (board[up][col] is not square)):
			if board[up][col].piece.color != square.piece.color and str(board[up][col].piece) == "K":
				pass
			else:
				break
		up-=1
	while down < 8:
		reachable.append(board[down][col])
		if ((board[down][col].piece is not None) and (board[down][col] is not square)):
			if board[down][col].piece.color != square.piece.color and str(board[down][col].piece) == "K":
				pass
			else:
				break
		down+=1
	return reachable


class king:
	blackking = pygame.image.load("blackking.png") 
	whiteking = pygame.image.load("whiteking.png")

	def __init__(self, color):
		self.color = color
		if self.color == white:
			self.image = self.whiteking
		else:
			self.image = self.blackking
		self.x = gap*.07
		self.y = gap*.05
		self.reachable = []
		self.inCheck = False
		self.moved = False

	def __repr__(self):
		return "K"



class pawn:
	blackpawn = pygame.image.load("blackpawn.png") 
	whitepawn = pygame.image.load("whitepawn.png")

	def __init__(self, color):
		self.color = color
		if self.color == white:
			self.image = self.whitepawn
		else:
			self.image = self.blackpawn
		self.x = gap*.2
		self.y = gap*.15
		self.reachable = []
		self.start = False

	def __repr__(self):
		return "P"

def pawnMoves(square, board):
	row = square.y/(w/8)
	col = square.x/(w/8)
	moves = []

	if square.piece.color == white:
		if board[row-1][col].piece is None:
			moves.append(board[row-1][col])
		if col-1>-1 and board[row-1][col-1].piece is not None:
			if board[row-1][col-1].piece.color == black:
				moves.append(board[row-1][col-1]) 
		if col+1<8 and board[row-1][col+1].piece is not None:
			if board[row-1][col+1].piece.color == black:
				moves.append(board[row-1][col+1])
		if not square.piece.start and board[row-1][col] in moves:
			if board[row-2][col].piece is None:
				moves.append(board[row-2][col])
				

	if square.piece.color == black:
		if board[row+1][col].piece is None:
			moves.append(board[row+1][col])
		if col-1>-1 and board[row+1][col-1].piece is not None:
				moves.append(board[row+1][col-1]) 
		if col+1<8 and board[row+1][col+1].piece is not None:
				moves.append(board[row+1][col+1])
		if not square.piece.start and board[row+1][col] in moves:
			if board[row+2][col].piece is None:
				moves.append(board[row+2][col])
				
	return moves

def kingMoves(square, board):
	row = square.y/(w/8)
	col = square.x/(w/8)
	moves = []

	for i in range(row-1,row+2):
		for j in range(col-1, col+2):
			if i< 8 and i>-1 and j<8 and j>-1:
				moves.append(board[i][j])
	if not square.piece.moved:
		if square.piece.color == white:
			if board[7][5].piece is None and board[7][6] is None:
				moves.append(board[7][6])
			if board[7][4].piece is None and board[7][3].piece is None and board[7][2].piece is None:
				moves.append(board[7][2])

		if square.piece.color == black:
			if board[0][5].piece is None and board[0][6] is None:
				moves.append(board[0][6])
			if board[0][4].piece is None and board[0][3].piece is None and board[0][2].piece is None:
				moves.append(board[0][2])

	for i in board:
		for j in i:
			if j.piece is not None:
				for k in j.piece.reachable:
					if j.piece.color != square.piece.color and k in moves:
						moves.remove(k)

	return moves

class queen:
	blackqueen = pygame.image.load("blackqueen.png") 
	whitequeen = pygame.image.load("whitequeen.png")

	def __init__(self, color):
		self.color = color
		if self.color == white:
			self.image = self.whitequeen
		else:
			self.image = self.blackqueen
		self.x = gap*.05
		self.y = gap*.1
		self.reachable = []

	def __repr__(self):
		return "Q"

class knight:
	blackknight = pygame.image.load("blackknight.png") 
	whiteknight = pygame.image.load("whiteknight.png")

	def __init__(self, color):
		self.color = color
		if self.color == white:
			self.image = self.whiteknight
		else:
			self.image = self.blackknight
		self.x = gap*.1
		self.y = gap*.13
		self.reachable = []

	def __repr__(self):
		return "N"

def knightMoves(square, board):
	moves = []
	row = square.y/(w/8)
	col = square.x/(w/8)


	if row-2>-1 and col-1>-1:
		moves.append(board[row-2][col-1])
	if row-2>-1 and col+1<8:
		moves.append(board[row-2][col+1])
	if row-1>-1 and col-2>-1:
		moves.append(board[row-1][col-2])
	if row-1>-1 and col+2<8:
		moves.append(board[row-1][col+2])

	if row+2<8 and col-1>-1:
		moves.append(board[row+2][col-1])
	if row+2<8 and col+1<8:
		moves.append(board[row+2][col+1])
	if row+1<8 and col-2>-1:
		moves.append(board[row+1][col-2])
	if row+1<8 and col+2<8:
		moves.append(board[row+1][col+2])
	return moves



class bishop:
	blackbishop = pygame.image.load("blackbishop.png") 
	whitebishop = pygame.image.load("whitebishop.png")

	def __init__(self, color):
		self.color = color
		if self.color == white:
			self.image = self.whitebishop
		else:
			self.image = self.blackbishop
		self.x = gap*.1
		self.y = gap*.08
		self.reachable = []
	def __repr__(self):
		return "B"

def checkDiag(square, board):
	reachable = []
	row = square.y/gap
	col = square.x/gap
	left = col
	right = col
	up = row
	down = row
	while (left>-1) and up>-1:
		reachable.append(board[up][left])
		if ((board[up][left].piece is not None) and (board[up][left] is not square)):
			if board[up][left].piece.color != square.piece.color and str(board[up][left].piece) == "K":
				pass
			else:
				break
		left-=1
		up-=1
	left = col
	up = row
	while right<8 and down< 8:
		reachable.append(board[down][right])
		if ((board[down][right].piece is not None) and (board[down][right] is not square)):
			if board[down][right].piece.color != square.piece.color and str(board[down][right].piece) == "K":
				pass
			else:
				break
		right+=1
		down+=1
	right = col
	down = row
	while up > -1 and right <8:
		reachable.append(board[up][right])
		if ((board[up][right].piece is not None) and (board[up][right] is not square)):
			if board[up][right].piece.color != square.piece.color and str(board[up][right].piece) == "K":
				pass
			else:
				break
		up-=1
		right+=1
	up = row
	right = col
	while down < 8 and left>-1:
		reachable.append(board[down][left])
		if ((board[down][left].piece is not None) and (board[down][left] is not square)):
			if board[down][left].piece.color != square.piece.color and str(board[down][left].piece) == "K":
				pass
			else:
				break
		down+=1
		left-=1
	down = row
	left = col
	return reachable


def reachable(square, board):
	
	
	reachable = []
	if str(square.piece) == "R":
		reachable = checkLine(square,board)
	elif str(square.piece) == "Q":
		reachable = checkLine(square,board)
		reachable.extend(checkDiag(square, board))
	elif str(square.piece) == "B":
		reachable = checkDiag(square, board)
	elif str(square.piece) == "P":
		reachable = pawnMoves(square, board)
	elif str(square.piece) == "N":
		reachable = knightMoves(square, board)
	elif str(square.piece) == "K":
		reachable = kingMoves(square,board)
	else:
		reachable = [j for i in board for j in i]

	removed = []
	k = 0
	while k<len(reachable):
		if reachable[k].piece is not None:
			if reachable[k].piece is square.piece:
				removed.append(reachable[k])
		k+=1
	for i in removed:
		reachable.remove(i)

	square.piece.reachable = reachable
