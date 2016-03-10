 from puzzle import Puzzle


class MNPuzzle(Puzzle):
    """
    An nxm puzzle, like the 15-puzzle, which may be solved, unsolved,
    or even unsolvable.
    """

    def __init__(self, from_grid, to_grid):
        """
        MNPuzzle in state from_grid, working towards
        state to_grid

        @param MNPuzzle self: this MNPuzzle
        @param tuple[tuple[str]] from_grid: current configuration
        @param tuple[tuple[str]] to_grid: solution configuration
        @rtype: None
        """
        # represent grid symbols with letters or numerals
        # represent the empty space with a "*"
        assert len(from_grid) > 0
        assert all([len(r) == len(from_grid[0]) for r in from_grid])
        assert all([len(r) == len(to_grid[0]) for r in to_grid])
        self.n, self.m = len(from_grid), len(from_grid[0])
        self.from_grid, self.to_grid = from_grid, to_grid

    def __str__(self):
        """
        Return a string representation of MNpuzzle
        
        @type MNPuzzle
        @rtype str
        
        >>> self = (("1", "2", "3"), ("4", "5", "*"))
        >>> self.__str__()
        '(("1", "2", "3"), ("4", "5", "*"))'
        """
        return '({})'.format(from_grid)
#Once I know what this is suppose to look like a little more I should look str over

    def __eq__(self, other):
        """
        Return if other is equivalent to self
        
        @type MNpuzzle
        @type #ANYTHING?
        @rtype bool
        
        >>> MNPuzzle.self = (("1", "2", "3"), ("4", "5", "*"))
        >>> other = 'HELLO'
        >>> MNPuzzle.__eq__(other)
        False
        
        >>> MNPuzzle.self = (("1", "2", "3"), ("4", "5", "*"))
        >>> other = (("1", "2", "3"), ("4", "5", "*"))
        >>> MNPuzzle.__eq__(other)
        True
        """
        return self == other
#probably more complicated

    # TODO
    # __repr__ is up to you

    # TODO
    def is_solved(self):
        """
        Return True iff MNPuzzle is solved
        
        @type self: MNPuzzle
        @rtype: bool
        
        >>> from_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> to_grid = (("1", "2", "3"), ("4", "5", "*"))
        >>> MNPPuzzle(from_grid, to_grid)
        >>> MNPuzzle.is_solved()
        True
        
        >>> MNPuzzle((("2", "*", "1"),("3", "4", "5")),(("1", "2", "3"),
        ("4", "5", "*")))
        >>> MNPuzzle.is_solved()
        False
        """
        return from_grid == to_grid
#Extension helper functions
    
    def swap_left(self):
     """
     Swap the character that is on the right of "*" with "*"
     
     >>> MNPuzzle((("2", "*", "1"),("3", "4", "5")),(("1", "2", "3"),
        ("4", "5", "*")))
     >>> MNPuzzle.swap_left()
     >>> Print(MNPuzzle)
     (("2","1", "*"),("3", "4", "5")),(("1", "2", "3"),("4", "5", "*"))
    """
     
    
    
    # legal extensions are configurations that can be reached by swapping one
    # symbol to the left, right, above, or below "*" with "*"

    # TODO
    # override is_solved
    # a configuration is solved when from_grid is the same as to_grid


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    target_grid = (("1", "2", "3"), ("4", "5", "*"))
    start_grid = (("*", "2", "3"), ("1", "4", "5"))
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    start = time()
    solution = breadth_first_solve(MNPuzzle(start_grid, target_grid))
    end = time()
    print("BFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))
    start = time()
    solution = depth_first_solve((MNPuzzle(start_grid, target_grid)))
    end = time()
    print("DFS solved: \n\n{} \n\nin {} seconds".format(
        solution, end - start))