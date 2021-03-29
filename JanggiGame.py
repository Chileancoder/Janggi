# Author: Sebastian Gajardo
# Date: 2/21/21
# Description: Janggi Korean chess game portfolio project. Consists of Janggi Piece parent class, blue general, red
# general, blue guard, red guard, blue soldier, red soldier, horse, elephant, chariot and cannon child/sub classes
# to represent the pieces of the game and a Janggi game class to represent the actual game that hold both the game board
# and hold the players, one red and one blue. Each game piece has specific movement rules and the game is won by a
# player when they put the other player in a checkmate situation where they can't make a legal move on the next turn.
# Decided to not have a player class because the game will always have two players, if it had a variable set of players
# it would be necessary. All pieces hold there specific movement rules instead of the game, since it's an individual
# piece characteristic. Used recursion to cover possible moves for pieces, made it much easier than iterating through
# because of the complex rules set for each player. Used list comprehensions to represent the whole board and each
# fortress that are passed to each piece when making a move and used sets to represent all possible moves for each
# piece because they don't allow repeats.

class JanggiPiece:
    """
    Represents the pieces used in a Janggi Korean chess game class. Will be added to player pieces list and used to
    play the game. Will interact with Janggi game class which will initialize all the piece object and set/get piece
    location and all possible legal moves for each type of game piece.
    """

    def __init__(self, owner, location, piece_type):
        """Initializes a Janggi chess piece object with desired owner, initial location and type and name for display
        purposes."""
        self._owner = owner
        self._location = location
        self._name = owner + piece_type
        self._type = piece_type

    def get_owner(self):
        """
        Returns owner of chess piece.
        """
        return self._owner

    def get_location(self):
        """
        Returns chess piece location.
        """
        return self._location

    def get_name(self):
        """
        Returns piece name, used for displaying the board.
        """
        return self._name

    def get_type(self):
        """
        Returns current Janggi Piece object type.
        """
        return self._type

    def get_row(self):
        """
        Returns current row of piece.
        """
        return self.get_location()[0]

    def get_column(self):
        """
        Returns current column of piece.
        """
        return self.get_location()[1]

    def set_location(self, new_location):
        """
        Receives new position and sets it as current location of the piece.
        """
        self._location = new_location

    def __repr__(self):
        """
        Used to print out General objects, in friendlier form.
        """
        return repr(self.get_name())


class BlueGeneral(JanggiPiece):
    """
    Represents a Blue General type piece in Janggi Korean chess, inherits from Janggi Piece parent class. Blue general
    can move one space along the lines of the blue fortress. So forward, back, left, right and diagonal along fortress
    lines.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a blue general Janggi chess piece with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None):
        """
        Receives the current Janggi game board and all opposition player positions and returns all legal moves possible
        for the blue general object as a set of tuples.
        """
        if current_spot is None:  # Initialize current spot as current piece location.
            return self.get_legal_moves(board, opposition, count, self.get_location())

        row, column = current_spot[0], current_spot[1]  # (row, column) format for ease of use.

        if current_spot not in {(row, column) for row in range(7, 10) for column in range(3, 6)}:
            return set()  # Base case if current position not in blue fortress.

        if count == 1 and board[row][column] != "" and current_spot not in opposition:
            return set()  # Base case if not initial position and current position occupied by a friendly piece.

        if count == 1:  # Base case if all checks passed, add current spot to moves.
            return {current_spot}

        moves = set()
        if current_spot in {(7, 3), (7, 5), (9, 3), (9, 5), (8, 4)}:
            # If in corners or center of blue fortress add diagonals.                                     # Down, right.
            moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1)) |
                            self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1)) |  # Down, left.
                            self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1)) |  # Up, right.
                            self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1)))  # Up, left.

        # Add up, down, left and right moves for all positions.
        moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column)) |  # Down.
                   self.get_legal_moves(board, opposition, count + 1, (row - 1, column)) |  # Up.
                   self.get_legal_moves(board, opposition, count + 1, (row, column + 1)) |  # Right.
                   self.get_legal_moves(board, opposition, count + 1, (row, column - 1)))  # Left.

        return moves  # Returns all possible moves.


class RedGeneral(JanggiPiece):
    """
    Represents a red general type piece in Janggi Korean chess, inherits from Janggi Piece parent class. Red general
    can move one space along the lines of the red fortress. So forward, back, left, right and diagonal along fortress
    lines.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a red General Janggi chess piece object with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None):
        """
        Receives the current Janggi game board and all opposition player positions and returns all legal moves possible
        for the blue general object as a set of tuples.
        """
        if current_spot is None:  # Initialize current spot as current piece location.
            return self.get_legal_moves(board, opposition, count, self.get_location())

        row, column = current_spot[0], current_spot[1]  # (row, column) format for ease of use.

        if current_spot not in {(row, column) for row in range(3) for column in range(3, 6)}:
            return set()  # Base case if current position not in red fortress.

        if count == 1 and board[row][column] != "" and current_spot not in opposition:
            return set()  # Base case if not initial position and current position occupied by a friendly piece.

        if count == 1:  # Base case if all checks passed, add current spot to moves.
            return {current_spot}

        moves = set()
        if current_spot in {(0, 3), (0, 5), (2, 3), (2, 5), (1, 4)}:
            # If in corners or center of blue fortress add diagonals. Down, right. Down, left. Up, right. Up, left.
            moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1)) |
                                self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1)) |
                                self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1)) |
                                self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1)))

        # Add up, down, left and right moves for all positions.
        moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column)) |  # Down.
                            self.get_legal_moves(board, opposition, count + 1, (row - 1, column)) |  # Up.
                            self.get_legal_moves(board, opposition, count + 1, (row, column + 1)) |  # Right.
                            self.get_legal_moves(board, opposition, count + 1, (row, column - 1)))  # Left.

        return moves  # Returns all possible moves.


class BlueGuard(JanggiPiece):
    """
    Represents a blue guard type piece in Janggi Korean chess, inherits from Janggi Piece parent class. Blue guards
    can move one space along the lines of the blue fortress. So forward, back, left, right and diagonal along fortress
    lines.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a blue guard Janggi chess piece object with desired, owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None):
        """
        Receives the current Janggi game board and all opposition player positions and returns all legal moves possible
        for the blue guard object as a set of tuples.
        """
        if current_spot is None:  # Initialize current spot as current piece location.
            return self.get_legal_moves(board, opposition, count, self.get_location())

        row, column = current_spot[0], current_spot[1]  # (row, column) format for ease of use.

        if current_spot not in {(row, column) for row in range(7, 10) for column in range(3, 6)}:
            return set()  # Base case if current position not in blue fortress.

        if count == 1 and board[row][column] != "" and current_spot not in opposition:
            return set()  # Base case if not initial position and current position occupied by a friendly piece.

        if count == 1:  # Base case if all checks passed, add current spot to moves.
            return {current_spot}

        moves = set()
        if current_spot in {(7, 3), (7, 5), (9, 3), (9, 5), (8, 4)}:
            # If in corners or center of blue fortress add diagonals.                                    # Down, right.
            moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1)) |
                            self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1)) |  # Down, left.
                            self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1)) |  # Up, right.
                            self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1)))  # Up, left.

        # Add up, down, left and right moves for all positions.
        moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column)) |  # Down.
                   self.get_legal_moves(board, opposition, count + 1, (row - 1, column)) |  # Up.
                   self.get_legal_moves(board, opposition, count + 1, (row, column + 1)) |  # Right.
                   self.get_legal_moves(board, opposition, count + 1, (row, column - 1)))  # Left.

        return moves  # Returns all possible moves.


class RedGuard(JanggiPiece):
    """
    Represents a red guard type piece in Janggi Korean chess, inherits from Janggi Piece parent class. Red guard
    can move one space along the lines of the red fortress. So forward, back, left, right and diagonal along fortress
    lines.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a red guard Janggi chess piece object with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None):
        """
        Receives the current Janggi game board and all opposition player positions and returns all legal moves possible
        for the blue general object as a set of tuples.
        """
        if current_spot is None:  # Initialize current spot as current piece location.
            return self.get_legal_moves(board, opposition, count, self.get_location())

        row, column = current_spot[0], current_spot[1]  # (row, column) format for ease of use.

        if current_spot not in {(row, column) for row in range(3) for column in range(3, 6)}:
            return set()  # Base case if current position not in red fortress.

        if count == 1 and board[row][column] != "" and current_spot not in opposition:
            return set()  # Base case if not initial position and current position occupied by a friendly piece.

        if count == 1:  # Base case if all checks passed, add current spot to moves.
            return {current_spot}

        moves = set()
        if current_spot in {(0, 3), (0, 5), (2, 3), (2, 5), (1, 4)}:
            # If in corners or center of blue fortress add diagonals.  Down, right. Down, left. Up, right.
            moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1)) |
                                self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1)) |
                                self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1)) |
                                self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1)))  # Up, left.

        # Add up, down, left and right moves for all positions.
        moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column)) |  # Down.
                            self.get_legal_moves(board, opposition, count + 1, (row - 1, column)) |  # Up.
                            self.get_legal_moves(board, opposition, count + 1, (row, column + 1)) |  # Right.
                            self.get_legal_moves(board, opposition, count + 1, (row, column - 1)))  # Left.

        return moves  # Returns all possible moves.


class Horse(JanggiPiece):
    """
    Represents a horse type piece in Janggi Korean chess, inherits from Janggi Piece. a Horse object can move one space
    either vertically or horizontally and one space diagonally from their in the same general direction as the initial
    vertical or horizontal move. They can be blocked by a piece from either team along the way.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a Horse Janggi chess piece object with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None):
        """
        Receives current Janggi game board and opposition player positions and returns all legal moves possible
        for Horse object based on given parameters as a set of tuples.
        """
        if current_spot is None:  # Initializes current_spot as present location.
            return self.get_legal_moves(board, opposition, count, self.get_location())

        row, column = current_spot[0], current_spot[1]  # Location in row, column format.

        if current_spot not in {(row, column) for row in range(10) for column in range(9)}:
            return set()  # If location not on board.

        if count == 1 and board[row][column] != "":  # If location not empty, during initial move.
            return set()

        if count == 2 and board[row][column] != "" and current_spot not in opposition:
            return set()  # If final location, is occupied by piece from same team.

        if count == 2:  # If all conditions passed return final location.
            return {current_spot}

        if count == 1:  # If initial move legal, check it's final moves.

            if row > self.get_row():  # Initial move downwards. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1)) |
                        self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1)))

            elif row < self.get_row():  # Initial move upwards. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1)) |
                        self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1)))

            elif column > self.get_column():  # Initial move to the right. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1)) |
                        self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1)))

            else:  # Initial move to the left. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1)) |
                        self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1)))

        # Recursive case, check all possible initial moves.
        moves = set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column)) |
                 self.get_legal_moves(board, opposition, count + 1, (row - 1, column)) |
                 self.get_legal_moves(board, opposition, count + 1, (row, column + 1)) |
                 self.get_legal_moves(board, opposition, count + 1, (row, column - 1)))

        return moves  # All legal moves returned.


class Elephant(JanggiPiece):
    """
    Represents an elephant type piece in Janggi Korean chess, inherits from Janggi Piece parent class. An elephant
    object can move one space either vertically or horizontally and then two spaces diagonally from their in the same
    general direction as the initial vertical or horizontal move. They can be blocked by a piece from either team
    along the way.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a Elephant Janggi chess piece with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None, direction=None):
        """
        Receives current Janggi game board and opposition player positions and returns all legal moves possible
        for Elephant object based on given parameters as a set of tuples.
        """
        if current_spot is None:  # Initializes current_spot as present location.
            return self.get_legal_moves(board, opposition, count, self.get_location(), direction)

        row, column = current_spot[0], current_spot[1]  # Location in row, column format.

        if current_spot not in {(row, column) for row in range(10) for column in range(9)}:
            return set()  # If location not on board.

        if (count == 1 or count == 2) and board[row][column] != "":
            return set()  # If location not empty, during initial and mid move.

        if count == 3 and board[row][column] != "" and current_spot not in opposition:
            return set()  # If final location, is occupied by piece from same team.

        if count == 3:  # If all conditions passed return final location.
            return {current_spot}

        if count == 1:  # If initial move legal, check it's mid moves.
            if row > self.get_row():  # Initial move downwards. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1), "++") |
                           self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1), "+-"))

            elif row < self.get_row():  # Initial move upwards. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1), "-+") |
                           self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1), "--"))

            elif column > self.get_column():  # Initial move to the right. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1), "++") |
                           self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1), "-+"))

            else:  # Initial move to the left. Recursive case.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1), "+-") |
                           self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1), "--"))

        if count == 2:  # If mid move legal, check it's final move.
            if direction == "++":  # If mid move was in ++ direction continue in that direction.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column + 1), None))

            elif direction == "+-":  # If mid move was in +- direction continue in that direction.
                return set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column - 1), None))

            elif direction == "-+":  # If mid move was in -+ direction continue in that direction.
                return set(self.get_legal_moves(board, opposition, count + 1, (row - 1, column + 1), None))

            else:  # If mid move was in -- direction continue in that direction.
                return set(self.get_legal_moves(board, opposition, count + 1, (row - 1, column - 1), None))

        # Recursive case, check all possible initial moves.
        moves = set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column), direction) |
                    self.get_legal_moves(board, opposition, count + 1, (row - 1, column), direction) |
                    self.get_legal_moves(board, opposition, count + 1, (row, column + 1), direction) |
                    self.get_legal_moves(board, opposition, count + 1, (row, column - 1), direction))

        return moves  # All legal moves returned.


class Chariot(JanggiPiece):
    """
    Represents a Chariot type piece in Janggi Korean chess, inherits from Janggi Piece parent class. A Chariot
    can move vertically or horizontally until it encounters another piece. If the encountered piece belongs to the
    opposite player it can capture the encountered piece and count it as an approved move. If the piece belongs to the
    same player it must stop one short of that spot. Within either fortress the chariot can move diagonally along the
    the fortress lines as long as the above criteria are met.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a Chariot Janggi chess piece with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, current_spot=None, direction=None):
        """
        Receives current Janggi game board and opposition player positions and returns all legal moves possible
        for Chariot object based on given parameters as a set of tuples.
        """
        if current_spot is None:
            return self.get_legal_moves(board, opposition, self.get_location())

        row, column = current_spot[0], current_spot[1]

        if current_spot not in {(x, y) for x in range(10) for y in range(9)}:
            return set()  # If current spot not on board game board.

        if direction == "++" or direction == "+-" or direction == "-+" or direction == "--":
            # Diagonal direction base case, if current spot not within either fortress return empty set.
            if (current_spot not in {(x, y) for x in range(3) for y in range(3, 6)}) and (current_spot not in
                 {(x, y) for x in range(7, 10) for y in range(3, 6)}):
                return set()

        if self.get_location() != current_spot and board[row][column] != "" and current_spot not in opposition:
            return set()  # If not initial location and current spot a friendly piece.

        if self.get_location() != current_spot and current_spot in opposition:
            # Base case, current spot is opposition piece.
            return {current_spot}

        if self.get_location() != current_spot and board[row][column] == "":
            # If current spot is not initial position and is empty, return current spot and continue recursion.
            if direction == "+=":  # Down the board.
                return {current_spot} | self.get_legal_moves(board, opposition, (row + 1, column), direction)
            if direction == "-=":  # Up the board.
                return {current_spot} | self.get_legal_moves(board, opposition, (row - 1, column), direction)
            if direction == "=+":  # Right side.
                return {current_spot} | self.get_legal_moves(board, opposition, (row, column + 1), direction)
            if direction == "=-":  # Left side.
                return {current_spot} | self.get_legal_moves(board, opposition, (row, column - 1), direction)

            # Diagonals.
            if direction == "++":  # Up right.
                return {current_spot} | self.get_legal_moves(board, opposition, (row + 1, column + 1), direction)
            if direction == "+-":  # Up left.
                return {current_spot} | self.get_legal_moves(board, opposition, (row + 1, column - 1), direction)
            if direction == "-+":  # Down right.
                return {current_spot} | self.get_legal_moves(board, opposition, (row - 1, column + 1), direction)
            if direction == "--":  # Down left.
                return {current_spot} | self.get_legal_moves(board, opposition, (row - 1, column - 1), direction)

        moves = set()
        if current_spot in {(0, 3), (0, 5), (1, 4), (2, 3), (2, 5), (7, 3), (7, 5), (9, 3), (9, 5), (8, 4)}:
            # If in either fortress with a diagonal add diagonal moves.                        # Up right.
            moves = moves | set(self.get_legal_moves(board, opposition, (row + 1, column + 1), "++") |
                    self.get_legal_moves(board, opposition, (row + 1, column - 1), "+-") |  # Up left.
                    self.get_legal_moves(board, opposition, (row - 1, column + 1), "-+") |  # Down right.
                    self.get_legal_moves(board, opposition, (row - 1, column - 1), "--"))  # Down left.

        moves = moves | set(self.get_legal_moves(board, opposition, (row + 1, column), "+=") |  # Down the board.
                    self.get_legal_moves(board, opposition, (row - 1, column), "-=") |  # Up the board.
                    self.get_legal_moves(board, opposition, (row, column + 1), "=+") |  # Right.
                    self.get_legal_moves(board, opposition, (row, column - 1), "=-"))  # Left.

        return moves  # Return all possible moves.


class Cannon(JanggiPiece):
    """
    Represents an cannon type piece in Janggi Korean chess, inherits from Janggi Piece parent class. A Cannon piece
    can move to any space in the vertical or horizontal direction that has a non-Cannon piece separating the Cannon
    and the space as long as the space is not occupied by a friendly piece. A Cannon can't capture another Cannon or
    as mentioned before "jump" over another Cannon. Within either fortress a Cannon piece can move diagonally along the
    fortress lines if the above criteria are met (from one corner of the fortress to another diagonally while staying
    within the fortress and jumping over a non-Cannon type piece).
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a Cannon Janggi chess piece object with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, positions=None, count=0, current=None, direction=None):
        """
        Receives current Janggi game board and opposition player positions and returns all legal moves possible
        for Cannon object based on given parameters as a set of tuples.
        """
        if current is None:
            # Initialize default parameters, positions is all piece positions in game excluding cannons.

            positions = [(x, y) for (x, y) in [(row, column) for row in range(10) for column in
                        range(9) if board[row][column] != ""] if board[x][y].get_type() != "Cannon"]

            return self.get_legal_moves(board, opposition, positions, count, self.get_location(), None)

        row, column = current[0], current[1]  # Change to row, column form.

        if current not in {(row, column) for row in range(10) for column in range(9)}:
            return set()  # Base case, if position not on board.

        if current != self.get_location() and board[row][column] != "" and current not in positions:
            return set()  # Base case, if not initial position and current location is a cannon.

        if count > 1:  # Base case, if more than one player that's not a cannon between current and initial positions.
            return set()

        if count == 1 and current in opposition:
            # Base case. If one piece between current and initial positions and current is an opponent.
            return {current}

        if count == 1 and board[row][column] == "":
            # Recursive case. If one piece between current and initial positions and current is empty.
            if direction == "+=":  # Moving down board.
                return {current} | set(self.get_legal_moves(board, opposition, positions, count, (row + 1, column),
                        "+="))
            elif direction == "-=":  # Moving up board.
                return {current} | set(self.get_legal_moves(board, opposition, positions, count, (row - 1, column),
                        "-="))
            elif direction == "=+":  # Moving right.
                return {current} | set(self.get_legal_moves(board, opposition, positions, count, (row, column + 1),
                        "=+"))
            else:  # Moving left.
                return {current} | set(self.get_legal_moves(board, opposition, positions, count, (row, column - 1),
                        "=-"))

        if board[row][column] == "":  # If location is empty, continue in same direction. Recursive case.
            if direction == "+=":  # Moving down board.
                return set(self.get_legal_moves(board, opposition, positions, count, (row + 1, column), "+="))

            elif direction == "-=":  # Moving up board.
                return set(self.get_legal_moves(board, opposition, positions, count, (row - 1, column), "-="))

            elif direction == "=+":  # Moving right.
                return set(self.get_legal_moves(board, opposition, positions, count, (row, column + 1), "=+"))

            else:  # Moving left.
                return set(self.get_legal_moves(board, opposition, positions, count, (row, column - 1), "=-"))

        if current in positions:  # If piece at location is not a cannon, add one to piece count. Recursive case.
            if direction == "+=":  # Moving down board.
                return set(self.get_legal_moves(board, opposition, positions, count + 1, (row + 1, column), "+="))

            elif direction == "-=":  # Moving up board.
                return set(self.get_legal_moves(board, opposition, positions, count + 1, (row - 1, column), "-="))

            elif direction == "=+":  # Moving right.
                return set(self.get_legal_moves(board, opposition, positions, count + 1, (row, column + 1), "=+"))

            else:  # Moving left.
                return set(self.get_legal_moves(board, opposition, positions, count + 1, (row, column - 1), "=-"))

        diagonals = set()  # Create diagonals empty set.
        red_corners = {(0, 3): (2, 5), (0, 5): (2, 3), (2, 3): (0, 5), (2, 5): (0, 3)}
        if self.get_location() in red_corners and (0, 4) in positions:
            # If in any corner of the red fortress and middle of fortress occupied add legal diagonal moves.
            diagonals = diagonals | {red_corners.get(self.get_location())}

        blue_corners = {(7, 3): (9, 5), (7, 5): (9, 3), (9, 3): (7, 5), (9, 5): (7, 3)}
        if self.get_location() in blue_corners and (8, 4) in positions:
            # If in any corner of the blue fortress and middle of fortress occupied add legal diagonal moves.
            diagonals = diagonals | {blue_corners.get(self.get_location())}

        # Check up, down, left and right moves. Recursive case
        moves = diagonals | set(self.get_legal_moves(board, opposition, positions, count, (row + 1, column), "+=") |
                self.get_legal_moves(board, opposition, positions, count, (row - 1, column), "-=") |
                self.get_legal_moves(board, opposition, positions, count, (row, column + 1), "=+") |
                self.get_legal_moves(board, opposition, positions, count, (row, column - 1), "=-"))

        return moves  # Returns all moves possible.


class RedSoldier(JanggiPiece):
    """
    Represents an red soldier type piece in Janggi Korean chess, inherits from Janggi Piece parent class. A Red Soldier
    piece can move forward towards the blue edge of the board or horizontally one space, unless space is occupied by a
    friendly piece. Within the blue fortress it can move diagonally one space along the fortress lines. Once at the
    blue edge of the board it can only move horizontally.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a red soldier Janggi chess piece object with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None):
        """
        Receives current Janggi game board and opposition player positions and returns all legal moves possible
        for Blue Soldier object based on given parameters as a set of tuples.
        """
        if current_spot is None:  # Initialize current spot as initial location of piece.
            return self.get_legal_moves(board, opposition, count, self.get_location())

        row, column = current_spot[0], current_spot[1]

        if current_spot not in [(row, column) for row in range(10) for column in range(9)]:
            return set()  # Base case if current spot not on board.

        if count == 1 and board[row][column] != "" and current_spot not in opposition:
            # If current spot has a friendly piece in it.
            return set()

        if count == 1:  # If all checks passed return current spot in set form.
            return {current_spot}

        moves = set()
        if self.get_location() == (7, 3):  # Bottom right corner of blue fortress.
            moves = {(8, 4)}
        if self.get_location() == (7, 5):  # Bottom left corner.
            moves = {(8, 4)}
        if self.get_location() == (8, 4):  # Center of blue fortress.
            moves = {(9, 3), (9, 5)}

        moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row + 1, column)) |  # Move forward.
                            self.get_legal_moves(board, opposition, count + 1, (row, column + 1)) |  # Move right.
                            self.get_legal_moves(board, opposition, count + 1, (row, column - 1)))  # Move left.

        return moves  # Returns all possible moves.


class BlueSoldier(JanggiPiece):
    """
    Represents a blue soldier type piece in Janggi Korean chess, inherits from Janggi Piece parent class. A Blue Soldier
    piece can move forward towards the red edge of the board or horizontally one space, unless space is occupied by a
    friendly piece. Within the red fortress it can move diagonally one space along the fortress lines. Once at the
    red edge of the board it can only move horizontally.
    """

    def __init__(self, owner, location, piece_type):
        """
        Initializes a blue soldier Janggi chess piece object with desired owner, location and piece type.
        """
        super().__init__(owner, location, piece_type)

    def get_legal_moves(self, board, opposition, count=0, current_spot=None):
        """
        Receives current Janggi game board and opposition player positions and returns all legal moves possible
        for Blue Soldier object based on given parameters as a set of tuples.
        """
        if current_spot is None:  # Initialize current spot as initial location of piece.
            return self.get_legal_moves(board, opposition, count, self.get_location())

        row, column = current_spot[0], current_spot[1]

        if current_spot not in [(row, column) for row in range(10) for column in range(9)]:
            return set()  # Base case if current spot not on board.

        if count == 1 and board[row][column] != "" and current_spot not in opposition:
            # If current spot has a friendly piece in it.
            return set()

        if count == 1:  # If all checks passed return current spot in set form.
            return {current_spot}

        moves = set()
        if self.get_location() == (2, 3):  # Bottom left corner of red fortress.
            moves = {(1, 4)}
        if self.get_location() == (2, 5):  # Bottom right corner.
            moves = {(1, 4)}
        if self.get_location() == (1, 4):  # Center of red fortress.
            moves = {(0, 3), (0, 5)}

        moves = moves | set(self.get_legal_moves(board, opposition, count + 1, (row - 1, column)) |  # Move up.
                            self.get_legal_moves(board, opposition, count + 1, (row, column + 1)) |  # Move right.
                            self.get_legal_moves(board, opposition, count + 1, (row, column - 1)))  # Move left.

        return moves  # Returns all possible moves.


class JanggiGame:
    """
    Represents a Janggi Korean chess game, composed of two players red and blue. Who each have 1 general, 2 guards,
    2 elephants, 2 horses, 2 chariots, 2 cannons and 5 soldiers to try and get the opposing player into checkmate. Will
    interact with all of the Janggi Piece subclasses to initialize them, set locations, get locations and get owner,
    get type and get legal moves for each individual piece on the Janggi game board. Will hold the game board as a list
    of lists and two lists one for red pieces and one for blue pieces to represent player pieces in game.
    """

    def __init__(self):
        """
        Initializes a Janggi game object with an initialized board, players turn as blue, red and blue piece collections
        created as an empty list, then red and blue pieces created and set in initial positions and current game state
        as UNFINISHED.
        """
        self._blue_pieces = []                      # Represents list of non captured pieces in game for blue player.
        self._red_pieces = []                       # Represents list of non captured pieces in game for red player.
        self._game_state = "UNFINISHED"
        self._current_turn = "blue"                 # Blue player starts the game.
        self._board = self.create_board()

    def create_pieces(self):
        """
        Creates player pieces, initializes their starting position and appends them into their respective
        player pieces list.
        """
        # Initial positions in row, column format.

        blue_initial = [(8, 4), [(9, 3), (9, 5)], [(9, 2), (9, 7)], [(9, 1), (9, 6)], [(9, 0), (9, 8)], [(7, 1),
                        (7, 7)], [(6, 0), (6, 2), (6, 4), (6, 6), (6, 8)]]

        red_initial = [(1, 4), [(0, 3), (0, 5)], [(0, 2), (0, 7)], [(0, 1), (0, 6)], [(0, 0), (0, 8)], [(2, 1), (2, 7)],
                       [(3, 0), (3, 2), (3, 4), (3, 6), (3, 8)]]

        self._blue_pieces += [BlueGeneral("blue", blue_initial[0], "General")]  # Creates the generals.
        self._red_pieces += [RedGeneral("red", red_initial[0], "General")]

        for number in range(2):  # Creates two Guards, Horses, Elephants, Chariots and Cannons per player.

            self._blue_pieces += [BlueGuard("blue", blue_initial[1][number], "Guard"),
                                  Horse("blue", blue_initial[2][number], "Horse"),
                                  Elephant("blue", blue_initial[3][number], "Elephant"),
                                  Chariot("blue", blue_initial[4][number], "Chariot"),
                                  Cannon("blue", blue_initial[5][number], "Cannon")]

            self._red_pieces += [RedGuard("red", red_initial[1][number], "Guard"),
                                 Horse("red", red_initial[2][number], "Horse"),
                                 Elephant("red", red_initial[3][number], "Elephant"),
                                 Chariot("red", red_initial[4][number], "Chariot"),
                                 Cannon("red", red_initial[5][number], "Cannon")]

        for number in range(5):  # Creates five soldiers per player.

            self._blue_pieces += [BlueSoldier("blue", blue_initial[6][number], "Soldier")]
            self._red_pieces += [RedSoldier("red", red_initial[6][number], "Soldier")]

    def add_pieces(self):
        """
        Adds each players piece to their starting positions on the Janggi game board at the beginning of the game.
        """
        board = self.get_board()

        for piece in self.get_blue_pieces():  # Adds blue pieces.
            position = piece.get_location()
            board[position[0]][position[1]] = piece

        for piece in self.get_red_pieces():  # Adds red pieces.
            position = piece.get_location()
            board[position[0]][position[1]] = piece

    def create_board(self):
        """
        Creates Janggi game board and then calls create_pieces method to create game board pieces and sets pieces in
        initial positions by calling add_pieces method.
        """
        self._board = [["" for _ in range(9)] for _ in range(10)]  # _ means, not keeping track of values.

        self.create_pieces()  # Janggi game board pieces created.
        self.add_pieces()  # Pieces added to board.

        return self._board

    def get_board(self):
        """
        Returns the current game board.
        """
        return self._board

    def get_current_turn(self):
        """
        Returns player whose turn it is.
        """
        return self._current_turn

    def get_game_state(self):
        """
        Returns the current state of the game.
        """
        return self._game_state

    def get_blue_pieces(self):
        """
        Returns blue player pieces currently in game.
        """
        return self._blue_pieces

    def get_red_pieces(self):
        """
        Returns red player pieces currently in game.
        """
        return self._red_pieces

    def get_opposition_positions(self, player):
        """
        Receives a player and returns all of the opposition player piece positions as a set of (row, column) tuples.
        """

        if player == "blue":  # If blue is player send red piece positions.
            return {piece.get_location() for piece in self.get_red_pieces()}
        else:  # Vice versa.
            return {piece.get_location() for piece in self.get_blue_pieces()}

    def get_opposition(self):
        """"
        Returns opposition player from current turn player.
        """
        if self.get_current_turn() == "blue":
            return "red"
        else:
            return "blue"

    def get_piece_from_position(self, position):
        """
        Receives a position on the board and returns the piece in that position.
        """
        return self.get_board()[position[0]][position[1]]  # Returns Janggi piece at that position.

    def change_turn(self):
        """
        Changes turn to other player, based on what the current player is.
        """
        if self.get_current_turn() == "blue":
            self._current_turn = "red"
        else:
            self._current_turn = "blue"

    def set_game_state(self, player):
        """
        Receives player whose turn it is and sets game state to that player winning.
        """
        if player == "blue":
            self._game_state = "BLUE_WON"
        else:
            self._game_state = "RED_WON"

    def make_move(self, move_from, move_to):
        """
        Receives position to move from and position to move to and then  if the square being moved from does not
        contain a piece belonging to the player whose turn it is, or if the indicated move is not legal, or if the game
        has already been won, then it returns False. Otherwise it makes the indicated move, removes any
        captured piece, updates the game state if necessary, updates whose turn it is, and returns True. Does this by
        first translating the algebraic input positions to (row, column) format then checking if game is still
        "UNFINISHED", if the position to move from is empty, if piece at move from position does not belong to current
        turn player, if move to position is a legal move for that janggi piece object and if that move leaves the
        current player in check. If any of those are False returns False and move is not made.If move to position if
        the same as move from position and the player is not currently in check then it counts as skipping your turn and
        returns True. If all of the previous checks are passed then makes the move and checks if opposition player is in
        check, if he is checks if he is in checkmate as well. If he's in checkmate the game state changes to the current
        player winning if not it changes turn and returns True. Calls update board, is in check, is check mate and
        leaves in check.
        """
        board = self.get_board()
        # Translating from alphanumeric to row/column.
        translate = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8}
        to_position = (int(move_to[1:]) - 1, translate[move_to[0]])  # Move to in (row, column) format.
        from_position = (int(move_from[1:]) - 1, translate[move_from[0]])  # Move from in (row, column) format.

        if self.get_game_state() != "UNFINISHED":  # If game has already been won by either player.
            return False

        if board[from_position[0]][from_position[1]] == "":  # If move_from position is empty.
            return False

        piece = self.get_piece_from_position(from_position)  # Game piece at move_from.
        player = piece.get_owner()

        if player != self.get_current_turn():  # If piece does not belong to player whose turn it is.
            return False

        if move_from == move_to and not self.is_in_check(player):
            # Player skipped turn intentionally, if general not in check.
            self.change_turn()  # Update turn and return true.
            return True

        if to_position not in piece.get_legal_moves(board, self.get_opposition_positions(player)):
            return False  # If position not in legal moves for that piece.

        if self.leaves_in_check(from_position, to_position):  # If move leaves player making move in check.
            return False

        self.update_board(from_position, to_position)  # Otherwise make indicated move, remove any captured pieces.

        if self.is_in_check(self.get_opposition()):  # If opposition player in check after current player made move.

            if self.is_check_mate(self.get_opposition()):  # If in opposition player in check, check checkmate.
                # If opposition player in checkmate, change state to current player as winner and return True.
                self.set_game_state(player)
                return True

        self.change_turn()  # Update turn and return True if all conditions met.
        return True

    def update_board(self, move_from, move_to):
        """
        Receives move_from and move_to positions and updates board when a legal move is given. Does this by replacing
        the move_fom position with and empty string ("") to represent an empty spot on the board. Then if the move_to
        position has an opposition player it grabs that player and replaces it with an empty string ("") , sets the
        current location of that opposition player as None and then removes it from the appropriate player in game
        piece collection and then places the moving piece to the vacated space. If move_to position doesn't have an
        opposition piece in it it simply puts the it simply places the current player moving piece in the new spot and
        then sets the new location for that piece as the new spot.
        """
        board = self.get_board()
        piece = board[move_from[0]][move_from[1]]  # Grab piece being moved.
        board[move_from[0]][move_from[1]] = ""  # Replace spot with empty.

        if board[move_to[0]][move_to[1]] != "":  # If space occupied by opposition player.
            opponent = board[move_to[0]][move_to[1]]  # Grab opponent piece in space.
            board[move_to[0]][move_to[1]] = ""  # Replace spot with empty.
            opponent.set_location(None)  # Opponent piece  out  of game.

            if opponent in self.get_red_pieces():
                self.get_red_pieces().remove(opponent)  # Remove piece from game if it belongs to red.
            else:
                self.get_blue_pieces().remove(opponent)  # Remove piece from game if it belongs to blue.

        board[move_to[0]][move_to[1]] = piece  # Add moving piece to spot.
        piece.set_location(move_to)  # Set new location for piece.

    def leaves_in_check(self, move_from, move_to):
        """
        Receives move_to and move_from positions and simulates move on board to check if it will leave the general in
        check. If so returns True, if not returns False. Does this by making the move on current game board, including
        removing any captured pieces as if the move was actually being made and then calling the is_in_check method
        to see if the opposition player is left in check it sets the boolean value to true, if not sets it to false.
        Then reverses the move that was just made by putting all pieces back to where they were prior to the check.
        """
        board = self.get_board()
        piece = board[move_from[0]][move_from[1]]  # Grab piece being moved.
        board[move_from[0]][move_from[1]] = ""  # Replace spot with empty.
        opponent = None
        is_in_check = False

        if board[move_to[0]][move_to[1]] != "":  # If space occupied by opposition player piece.
            opponent = board[move_to[0]][move_to[1]]  # Grab opponent piece in space.
            board[move_to[0]][move_to[1]] = ""  # Replace spot with empty.
            opponent.set_location(None)  # Opponent piece out of game.

            if opponent in self.get_red_pieces():
                self.get_red_pieces().remove(opponent)  # Remove piece from game if it belongs to red.
            else:
                self.get_blue_pieces().remove(opponent)  # Remove piece from game if it belongs to blue.

        board[move_to[0]][move_to[1]] = piece  # Add moving piece to spot.
        piece.set_location(move_to)  # Set new location for just moved piece.

        if self.is_in_check(piece.get_owner()):  # If general of moved pieces side is left in check set to True.
            is_in_check = True

        board[move_from[0]][move_from[1]] = piece  # Return moved piece to original move_from location.
        piece.set_location(move_from)  # Set moved piece location back to original move_from location.

        if opponent is not None:  # If piece was captured.
            board[move_to[0]][move_to[1]] = opponent  # Return opponent to original move_to location on board.
            opponent.set_location(move_to)  # Set location of opponent piece back to original move_to position.

            if opponent.get_owner() == "blue":
                # If opponent belongs to blue player, put back in non captured blue pieces.
                self.get_blue_pieces().append(opponent)
            else:  # If opponent belongs to red player, put back in non captured red pieces.
                self.get_red_pieces().append(opponent)

        else:
            board[move_to[0]][move_to[1]] = ""  # Replace moved_to spot with empty if no player was captured.

        return is_in_check

    def is_in_check(self, player):
        """
        Receives the player "red" or "blue" and returns True if the player is in check but returns False otherwise.
        Checks this by iterating through blue or red pieces depending on what player was input and grabbing the general
        type piece and getting it's location on the board. Then sees if that location is in opposite players available
        moves.
        """
        board = self.get_board()
        all_positions = set()
        position = None  # Initialize general position to None.

        if player == "blue":  # If checking blue player.
            for piece in self.get_blue_pieces():
                if piece.get_type() == "General":
                    position = piece.get_location()  # General location in (row, column) tuple.

            for piece in self.get_red_pieces():  # Get all possible legal moves for red.
                all_positions = all_positions | piece.get_legal_moves(board, self.get_opposition_positions("red"))

            if position in all_positions:
                return True  # If general position in all possible legal moves for opposing player return True.

        else:  # If checking red player.
            for piece in self.get_red_pieces():
                if piece.get_type() == "General":
                    position = piece.get_location()  # General location in (row, column) tuple.

            for piece in self.get_blue_pieces():  # Get all possible legal moves for blue.
                all_positions = all_positions | piece.get_legal_moves(board, self.get_opposition_positions("blue"))

            if position in all_positions:
                return True  # If general position in all possible legal moves for opposing player return True.

        return False

    def is_check_mate(self, player):
        """
        Receives opposition player from current turn and checks if he is in check mate. Does this by iterating through
        opposition player pieces and checking if any legal moves available to them would avoid a check state
        by calling on the leaves_in_check method which returns true if move leaves general in check and False
        otherwise.
        """

        if player == "red":  # If opposition is red check red pieces.
            for piece in self.get_red_pieces():
                moves = piece.get_legal_moves(self.get_board(), self.get_opposition_positions("red"))
                # All possible moves for current piece.

                for move_to in moves:  # Check all legal moves for all red pieces in game.
                    if not self.leaves_in_check(piece.get_location(), move_to):
                        return False  # If any available move for any piece gets red general out of check return False.

        else:  # If opposition is blue, check blue pieces.
            for piece in self.get_blue_pieces():
                moves = piece.get_legal_moves(self.get_board(), self.get_opposition_positions("blue"))
                # All possible moves for current piece.

                for move_to in moves:  # Check all legal moves for all blue pieces in game.
                    if not self.leaves_in_check(piece.get_location(), move_to):
                        return False  # If any available move for any piece gets blue general out of check return False.

        return True

    def print_board(self):
        """
        Prints out the current Janggi's game board with letters on the top of the board and numbers on the left side
        of the board for ease of reading.
        """
        board = self.get_board()
        a_i = "abcdefghi"
        top = ""
        for letter in a_i:  # Prints out top row with letters on top for orientation.
            if letter == "a":
                top += "   "
            top += " ______" + letter + "______ "
        print(top)

        for row in range(10):  # Prints out rest of board with numbers on the left side for orientation.
            if row == 9:
                line = str(row + 1) + " "
            else:
                line = str(row + 1) + "  "
            for column in range(9):
                if board[row][column] != "":
                    difference = 13 - len(board[row][column].get_name())
                    extra_spaces = " " * difference
                    line += "|" + board[row][column].get_name() + extra_spaces + "|"
                else:
                    line += "|_____________|"
            print(line)
        print()


def main():
    """
    Main function for testing.
    """
    # Basic tests from readme.
    game = JanggiGame()
    print(game.make_move('c1', 'e3'))  # should be False because it's not Red's turn.
    print(game.make_move("a7", "b7"))  # should return True.
    print(game.is_in_check('blue'))  # should return False.
    print(game.make_move('a4', 'a5'))  # should return True.
    print(game.get_game_state())  # should return UNFINISHED.
    print(game.make_move('b7', 'b6'))  # should return True.
    print(game.make_move('b3', 'b6'))  # should return False because it's an invalid move.
    print(game.make_move('a1', 'a4'))  # should return True.
    print(game.make_move('c7', 'd7'))  # should return True.
    print(game.make_move('a4', 'a4'))  # this will pass the Red's turn and return True.

    # Playing out a game.
    j = JanggiGame()
    print(j.get_board())
    j.print_board()  # Initial board print out, all pieces in correct positions.
    print(j.get_blue_pieces())
    print(j.get_red_pieces())
    j.make_move("a7", "a6")  # True, blue soldier forward move.
    j.print_board()
    j.make_move("c4", "c5")  # True, Red soldier move forward.
    j.print_board()
    print(j.make_move("a6", "b5"))  # False, blue soldiers can't move diagonal unless in red fortress.
    j.make_move("a6", "a5")  # True, blue soldier move forward.
    j.print_board()
    print(j.make_move("i4", "h5"))  # False, red soldier can't move diagonal, unless in blue fortress.
    j.make_move("c1", "d3")  # True, horse moving down right.
    j.print_board()
    print(j.get_current_turn())  # Blue turn.
    j.make_move("e7", "e6")  # True, blue soldier vertical move.
    j.print_board()
    j.make_move("d3", "e5")  # True, red Horse down, right move.
    j.print_board()
    print(j.make_move("a4", "b3"))  # False, Not reds turn.
    j.make_move("g10", "e7")  # True, blue elephant legal move.
    j.print_board()
    print(j.make_move("e5", "d7"))  # False, Red horse blocked by blue soldier.
    print(j.get_current_turn())  # Reds turn.
    j.print_board()
    j.make_move("e5", "c4")  # True, Red horse, left and up diagonal.
    j.print_board()
    print(j.is_in_check("blue"))  # False, not in check.
    print(j.is_in_check("red"))  # False, not in check.
    j.make_move("e7", "h5")  # True, blue elephant legal right and up diagonal.
    j.print_board()
    print(j.make_move("d1", "c1"))  # False, red guard can't go outside red fortress.
    j.make_move("e2", "d3")  # True, red general down left diagonal within fortress.
    j.print_board()
    print(j.get_current_turn())  # Blue.
    print(j.make_move("e9", "g9"))  # False, Blue general can't move more than 1 space at a time.
    print(j.make_move("f10", "g10"))  # False, blue guard can't go outside blue fortress.
    print(j.make_move("b10", "c8"))  # False, blue elephant moves 1 + 2 not 1 + 1.
    j.make_move("c10", "d8")  # True, blue horse up and right diagonal.
    j.print_board()
    j.make_move("f1", "e2")  # True red guard diagonal following fortress lines.
    j.print_board()
    print(j.make_move("a10", "a5"))  # False, blue chariot can't move to spot occupied by friendly.
    j.make_move("a10", "a6")  # True, blue chariot forward move.
    j.print_board()
    print(j.make_move("h3", "f3"))  # False, can't move to a space without jumping at least one non cannon piece.
    j.make_move("h3", "h7")  # True, red cannon jumps blue elephant.
    j.print_board()
    print(j.make_move("h8", "h6"))  # False, Blue cannon can't jump over other cannon.
    j.make_move("a6", "d6")  # True, blue chariot puts red general in check.
    j.print_board()
    print(j.is_in_check("red"))  # True, red general in check by blue chariot.
    print(j.is_check_mate("red"))  # False, red general can get out  of check easily.
    print(j.get_current_turn())  # Red.
    print(j.make_move("a4", "a5"))  # False, red can't make a move that leaves red general in check.
    j.make_move("b1", "d4")  # True, red elephant blocking blue chariot, getting general out of check.
    j.print_board()
    print(j.get_current_turn())  # Blue.
    j.make_move("f10", "f9")  # True, blue guard forward move within fortress.
    j.print_board()
    j.make_move("h7", "f7")  # True, red cannon left move, jump over blue soldier.
    j.print_board()
    j.make_move("h5", "f2")  # True, blue elephant left and up diagonal to red fortress.
    j.print_board()
    j.make_move("f7", "f10")  # True, blue cannon jump over blue guard into fortress.
    j.print_board()
    j.make_move("h10", "g8")  # True, blue horse up and left diagonal.
    j.print_board()
    print(j.make_move("f10", "c7"))  # False, cannon can't diagonal outside of fortress.
    j.make_move("f10", "d8")  # True, red cannon diagonal capture blue horse within fortress, jumping over blue general.
    j.print_board()
    print(j.get_blue_pieces())  # Blue horse captured so taken out of blue player pieces in game.
    print(j.get_current_turn())
    j.make_move("a5", "a4")  # True, blue soldier captures red soldier.
    j.print_board()
    j.make_move("a1", "a4")  # True, red chariot captures blue soldier.
    j.print_board()
    j.make_move("e9", "d8")  # True, blue general captures red cannon.
    j.print_board()
    j.make_move("e2", "f2")  # True, red guard captures blue elephant.
    j.print_board()
    j.make_move("i7", "i6")  # True, blue soldier forward move.
    j.print_board()
    j.make_move("c5", "c6")  # True, red soldier forward move.
    j.print_board()
    j.make_move("d6", "c6")  # True, blue chariot captures red soldier.
    j.print_board()
    j.make_move("a4", "b4")  # True, red chariot horizontal move.
    j.print_board()
    j.make_move("b10", "d7")  # True,  blue elephant right and up diagonal.
    j.print_board()
    j.make_move("b4", "b8")  # True, red chariot captures blue cannon and checks blue general.
    j.print_board()
    j.make_move("d8", "e9")  # True, blue general getting out of check.
    j.print_board()
    j.make_move("b3", "b9")  # True, red cannon jumps over red chariot.
    j.print_board()
    j.make_move("h8", "b8")  # True, blue cannon jumps blue horse and captures red chariot.
    j.print_board()
    j.make_move("b9", "f9")  # True, red cannon jumps general and captures blue guard within blue fortress.
    j.print_board()
    j.make_move("e9", "f9")  # True, blue general captures red cannon horizontal move.
    j.print_board()
    j.make_move("h1", "g3")   # True, red horse, left down diagonal.
    j.print_board()
    j.make_move("c6", "c4")  # True, blue chariot captures red horse, forward move.
    j.print_board()
    j.make_move("i4", "i5")  # True, red soldier forward move.
    j.print_board()
    j.make_move("i6", "i5")  # True, blue soldier captures red soldier with vertical move.
    j.print_board()
    j.make_move("g4", "g5")  # True, red soldier move vertically.
    j.print_board()
    j.make_move("c4", "c3")  # True, blue chariot vertical move, red general in check.
    j.print_board()
    j.make_move("d3", "e2")  # True, general moves diagonal within fortress to get out of check.
    j.print_board()
    j.make_move("c3", "g3")  # True, blue chariot captures red horse with horizontal move.
    j.print_board()
    j.make_move("f2", "f3")     # True, true red guard vertical move within palace.
    j.print_board()
    j.make_move("d7", "b4")  # True, blue elephant left up diagonal put red general in check.
    j.print_board()
    j.make_move("e2", "e1")  # True, red general moves out of check.
    j.print_board()
    j.make_move("g3", "g5")  # True, blue chariot captures red soldier, vertical move.
    j.print_board()
    j.make_move("d4", "f1")  # True, elephant back right diagonal.
    j.print_board()
    j.make_move("b8", "b1")  # True, blue cannon jump over blue elephant and check red general.
    j.print_board()
    print(j.make_move("e1", "f2"))  # False, no diagonal line.
    j.make_move("d1", "d2")  # True, red guard moves so cannon has no piece to jump, general out of check.
    j.print_board()
    j.make_move("g5", "g3")  # True, blue chariot vertical move.
    j.print_board()
    j.make_move("f1", "d4")  # True,  red elephant down and right diagonal.
    j.print_board()
    j.make_move("b1", "g1")  # True, blue cannon captures red elephant, jumps over red general
    j.print_board()
    j.make_move("i1", "h1")  # True, red chariot horizontal move.
    j.print_board()
    j.make_move("i10", "h10")  # True blue chariot horizontal move.
    j.print_board()
    j.make_move("h1", "h10")  # True, red chariot captures blue chariot, vertical move.
    j.print_board()
    j.make_move("g8", "h10")  # True, blue horse captures red chariot, back and left diagonal.
    j.print_board()
    j.make_move("e4", "f4")  # True,  Red soldier right horizontal move.
    j.print_board()
    j.make_move("g3", "g2")  # True, blue chariot vertical move.
    j.print_board()
    j.make_move("d2", "d3")  # True, red guard diagonal blocks blue elephant.
    j.print_board()
    j.make_move("g2", "g4")  # True, blue chariot vertical move.
    j.print_board()
    j.make_move("e1", "e2")  # True, general vertical move within fortress.
    j.print_board()
    j.make_move("g4", "f4")  # True, chariot captures red soldier, horizontal move.
    j.print_board()
    j.make_move("d4", "a6")  # True, blue elephant down and left diagonal.
    j.print_board()
    j.make_move("e6", "e5")  # True, blue soldier vertical move.
    j.print_board()
    j.make_move("a6", "c9")  # True, red elephant right down diagonal.
    j.print_board()
    j.make_move("e5", "e4")  # True, blue soldier vertical move.
    j.print_board()
    j.make_move("c9", "e6")  # True, red elephant up right diagonal.
    j.print_board()
    j.make_move("b4", "e6")  # True, blue elephant captures red elephant right down diagonal.
    j.print_board()
    j.make_move("d3", "d2")  # True, red guard backward move within fortress.
    j.print_board()
    j.make_move("h10", "g8")  # True, horse up and left diagonal.
    j.print_board()
    j.make_move("e2", "e1")  # True, general backwards move.
    j.print_board()
    j.make_move("f4", "f3")  # True, blue chariot captures red guard with vertical move.
    j.print_board()
    j.make_move("d2", "e2")  # True, red guard backwards move within fortress.
    j.print_board()
    j.make_move("e4", "e3")    # True, blue soldier forward move.
    j.print_board()
    j.make_move("e1", "e1")  # True, red passes turn since not in check.
    j.print_board()
    j.make_move("e6", "h4")  # True, blue elephant right up diagonal.
    j.print_board()
    j.make_move("e1", "e1")  # True, red passes since not in check.
    j.print_board()
    j.make_move("f3", "e2")  # True, bleu chariot up left diagonal within fortress lines, captures red guard.
    j.print_board()
    print(j.is_check_mate("red"))  # red, is in check mate, has no available moves.
    print(j.get_game_state())  # Blue has won, since red is check mate no need to capture the red general.
    print(j.make_move("e1", "e2"))  # False, blue has already won game red can't continue to move.
    print(j.make_move("e2", "e2"))  # False, blue has already won game can't continue to play, game is over.


if __name__ == "__main__":
    main()
