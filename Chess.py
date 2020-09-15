import pygame
import pieces
import time
import math

pygame.init()
global over 
	
beige = (243,194,145)
brown = (155,83,6)
w = 800
win = pygame.display.set_mode((w,w))

black = ((0,0,0))
white = (255,255,255)
yellow = (255,255,153)
red = (255,0,0)
pink = (250,117,148)

def makeBoard():

	color = brown
	for i in range(8):
		if color == brown:
				color = beige
		else:
				color = brown
		for j in range(8):
			board[i].append(square(j*w/8, i*w/8, color, None))
			if color == brown:
				color = beige
			else:
				color = brown
	for i in board[1]:
		p = pieces.pawn(black)
		i.setPiece(p)
	for i in board[6]:
		p = pieces.pawn(white)
		i.setPiece(p)

	board[0][0].setPiece(pieces.rook(black))
	board[0][7].setPiece(pieces.rook(black))
	board[0][1].setPiece(pieces.knight(black))
	board[0][6].setPiece(pieces.knight(black))
	board[0][2].setPiece(pieces.bishop(black))
	board[0][5].setPiece(pieces.bishop(black))
	board[0][3].setPiece(pieces.queen(black))
	board[0][4].setPiece(pieces.king(black))
	board[7][0].setPiece(pieces.rook(white))
	board[7][7].setPiece(pieces.rook(white))
	board[7][1].setPiece(pieces.knight(white))
	board[7][6].setPiece(pieces.knight(white))
	board[7][2].setPiece(pieces.bishop(white))
	board[7][5].setPiece(pieces.bishop(white))
	board[7][3].setPiece(pieces.queen(white))
	board[7][4].setPiece(pieces.king(white))


def move(square, endSquare):
	endSquare.setPiece(square.piece)
	square.piece = None
	square.reset()



def draw(over):

	for row in board:
		for col in row:
			pygame.draw.rect(win, col.color, (col.x, col.y, col.width, col.width))
			if col.piece is not None:
				win.blit(col.piece.image, (col.piecex, col.piecey))
	for row in board:
		for col in row:
			if col.piece is not None:
				win.blit(col.piece.image, (col.piecex, col.piecey))
	pygame.display.update()


def getClicked(pos, rows, width):
	gap = width//rows
	y, x = pos

	row = y//gap
	col = x//gap

	return row, col

class square:

	def __init__(self, x, y, color, piece):
		self.x = x
		self.y = y
		self.tcolor = color
		self.color = color
		self.piece = None
		self.width = w/8
		self.piecex = 0
		self.piecey = 0

	def setPiece(self, piece):
		self.piece = piece
		self.piecex = self.x+piece.x
		self.piecey = self.y+piece.y


	def setColor(self,color):
		self.color = color

	def reset(self):
		self.color = self.tcolor













def canReach(square, endSquare):
	reachable = square.piece.reachable
	for i in reachable:
		if i is endSquare:
			if endSquare.piece is None:
				return True
			elif endSquare.piece.color != square.piece.color:
				return True
			else:
				return False
		else:
		 	pass
	return False


def isValid(square, endSquare, whiteTurn, board):
	if square.piece.color == white and whiteTurn or square.piece.color == black and not whiteTurn:
		if canReach(square, endSquare):


	

				
			if str(square.piece) == "P":
				
				
				if endSquare.y/(w/8)==7 or endSquare.y/(w/8)==0:
					return 2
				else:
					return 1

			elif str(square.piece) == "K" and not square.piece.moved:

				 if endSquare is board[7][6] or endSquare is board[0][6]:
				 	return 3
				 elif endSquare is board[7][2] or endSquare is board[0][2]:
				 	return 4
				 else:
				 	return 1

				
			else:
				return 1
	return 0






def checkmate(king, board, checking):
	if not king.inCheck:
		return False
	else:
		for i in king.reachable:
			if i.piece is None or i.piece.color != king.color:
				return False
		for i in board:
			for j in i:
				if j.piece is not None:
					if j.piece.color == king.color:
						if checking in j.piece.reachable:
							return False
	return True






def main():
	global board 
	global previous
	global whiteTurn
	global taken
	whiteTurn = True
	taken = None
	board = [[],[],[],[],[],[],[],[]]
	makeBoard()
	square = None
	run = True
	selected = False
	pressed = False
	over = False
	promoted = False
	whiteKing = board[7][4].piece
	blackKing = board[0][4].piece
	checking = None
	while run:

		for i in board:
			for j in i:
				if j.piece is not None:

					if j.piece is blackKing or j.piece is whiteKing:
						j.piece.inCheck = False
					pieces.reachable(j,board)

					for k in j.piece.reachable:
						if k.piece is whiteKing and j.piece.color == black:
							whiteKing.inCheck = True
							checking = j
							k.setColor(red)
						elif k.piece is blackKing and j.piece.color == white:
							blackKing.inCheck = True
							checking = j
							k.setColor(red)
						

					


		win.fill((0,0,0,0))
		draw(over)

		for event in pygame.event.get():


			if event.type == pygame.QUIT:
				run = False


			if event.type == pygame.KEYDOWN:

				#reset
				if event.key == pygame.K_c:
					board = [[],[],[],[],[],[],[],[]]
					makeBoard()
					whiteTurn = True
					selected, pressed, over = (False, False, False)

				#undo previous move
				if event.key == pygame.K_z:
					if previous != (None,None):

						whiteTurn = not whiteTurn
						endSquare, square = previous
						if not promoted:
							endSquare.setPiece(square.piece)
							if str(endSquare.piece) == "P":
								for i in board[1]:
									if str(i.piece) == "P":
										i.piece.start = False
								for i in board[6]:
									if str(i.piece) == "P":
										i.piece.start = False

						else:
							endSquare.setPiece(pieces.pawn(square.piece.color))

						square.piece = None
						square.reset()
						if taken is not None:
							square.setPiece(taken)
						previous = (None,None)
						selected = False
						for i in board:
							for j in i:
								j.reset()
						

				
			if event.type == pygame.MOUSEBUTTONDOWN and not over:
				

				pos = pygame.mouse.get_pos()
				col, row = getClicked(pos, 8, w)
				pygame.time.delay(50)


				if not selected:
					if board[row][col].piece is not None:
						square = board[row][col]
						square.setColor(yellow)
						if square.piece is not None:
							for i in square.piece.reachable:
								if i.piece is None:
									i.setColor(red)
								else:
									if i.piece.color != square.piece.color:
										i.setColor(red)
						selected = True
				else:
					endSquare = board[row][col]














					
					if isValid(square, endSquare, whiteTurn, board) == 1:

						if str(square.piece) == "P":
							square.piece.start = True
						whiteTurn = not whiteTurn
						taken = endSquare.piece
						move(square, endSquare)
						previous = (square, endSquare)
						for i in board:
								for j in i:
									j.reset()
						selected = False

					elif isValid(square, endSquare, whiteTurn, board) == 2:

						taken = endSquare.piece
						endSquare.setPiece(pieces.queen(square.piece.color))
						square.piece = None
						whiteTurn = not whiteTurn
						for i in board:
								for j in i:
									j.reset()
						selected = False
						previous = (square, endSquare)
						promoted = True
					elif isValid(square, endSquare, whiteTurn, board) == 3:
						taken = endSquare.piece
						move(square, endSquare)
						if endSquare.piece.color == white:
							board[7][5].setPiece(pieces.rook(white))
							board[7][7].piece = None
							endSquare.piece.moved = True
						else:
							board[0][5].setPiece(pieces.rook(black))
							board[0][7].piece = None
							endSquare.piece.moved = True
						whiteTurn = not whiteTurn
						for i in board:
								for j in i:
									j.reset()
						selected = False
					elif isValid(square, endSquare, whiteTurn, board) == 4:
						taken = endSquare.piece
						move(square, endSquare)
						if endSquare.piece.color == white:
							board[7][3].setPiece(pieces.rook(white))
							board[7][0].piece = None
							endSquare.piece.moved = True
						else:
							board[0][3].setPiece(pieces.rook(black))
							board[0][0].piece = None
							endSquare.piece.moved = True
						whiteTurn = not whiteTurn
						for i in board:
								for j in i:
									j.reset()
						selected = False



















						
					else:
						if endSquare.piece is not None:
							for i in board:
								for j in i:
									j.reset()
							endSquare.setColor(yellow)
							square = board[row][col]
							for i in square.piece.reachable:
								if i.piece is None:
									i.setColor(red)
								else:
									if i.piece.color != square.piece.color:
										i.setColor(red)
							

						else:
							square.reset()
							for i in board:
								for j in i:
									j.reset()
							selected = False


		if checkmate(blackKing, board, checking):
			over = True

		if checkmate(whiteKing, board, checking):
			over = True



				
				




				
		


main()
pygame.quit()
