# Python-Chess
# See a video of this project: https://drive.google.com/file/d/1DbjGC7kk76PV6LnouRJXw8jAY3XVmnjU/view?usp=sharing
This is a basic chess program written in python, it allows all basic legal moves and some special moves.
moves that this program does not support: En passant and pawn promotion to a piece other than Queen.
# Rules that this program does check for:
  1. All pieces can only move to squares they are able to - which are highlighted red for a selected piece.
  2. A piece cannot move into a square that is occupied by a piece of the same color.
  3. A pawn is allowed to move 2 squares on its first move, after that, the pawn can only move forward 1 square.
  4. A pawn can only move diagnally when there is a piece of the opposite color to be taken.
  5. Pawn promotes to a queen when it reaches the end of the board.
  6. The King's square is highlighted red when the King is in check.
  7. The King cannot castle after moving.
# Rules that this program does not check for:
  1. Whether or not a piece can prevent checkmate by blocking an opposing piece's attack on the king.
  3. Whether or not the squares between a king and a rook are attacked before castle.
  4. Whether or not a piece's movement would put the king in check.
