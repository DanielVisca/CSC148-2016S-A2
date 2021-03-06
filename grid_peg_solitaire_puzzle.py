from puzzle import Puzzle


class GridPegSolitairePuzzle(Puzzle):
    """
    Snapshot of peg solitaire on a rectangular grid. May be solved,
    unsolved, or even unsolvable.
    """

    def __init__(self, marker, marker_set):
        """
        Create a new GridPegSolitairePuzzle self with
        marker indicating pegs, spaces, and unused
        and marker_set indicating allowed markers.

        @type marker: list[list[str]]
        @type marker_set: set[str]
                          "#" for unused, "*" for peg, "." for empty
        """
        assert isinstance(marker, list)
        assert len(marker) > 0
        assert all([len(x) == len(marker[0]) for x in marker[1:]])
        assert all([all(x in marker_set for x in row) for row in marker])
        assert all([x == "*" or x == "." or x == "#" for x in marker_set])
        self._marker, self._marker_set = marker, marker_set

    # TODO
    # implement __eq__, __str__ methods
    def __eq__(self, other):
        """
        @type self: GridPegSolitairePuzzle
        @type: object
        @rtype: bool
        
        Return True if other is equal to sekf, otherwise return False
        
        >>>  self = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"], \
        ["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"], \
        ["*", "*", "*", "*", "*"]]
        >>>  other = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"], \
        ["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"], \
        ["*", "*", "*", "*", "*"]]
        >>> GridPegSolitairePuzzle.__eq__(self, other)
        True
        
        >>>  self = [["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"], \
        ["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"], \
        ["*", "*", "*", "*", "*"]]
        >>>  other = [["*", ".", "*", "*", "*"],["*", "*", "*", "*", "*"], \
        ["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"], \
        ["*", "*", "*", "*", "*"]]
        >>> GridPegSolitairePuzzle.__eq__(self, other)
        False
        """
        return self == other
#maybe check types as well?
    
    def __str__(self):
        """
        @type self: GridPegSolitairePuzzle
        @rtype: str
        
        Return a string representation of self
        
        >>> GridPegSolitairePuzzle([["*", "*", "*", "*", "*"],["*", "*", "*", \
        "*", "*"], \
        ["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"], \
        ["*", "*", "*", "*", "*"]], {['.','*']})
        >>> GridPegSolitairePuzzle.__str__()
        '[["*", "*", "*", "*", "*"],["*", "*", "*", "*", "*"], \
        ["*", "*", "*", "*", "*"],["*", "*", ".", "*", "*"], \
        ["*", "*", "*", "*", "*"]], {['.','*']}'
        """
        return '{},{}'.format(self._marker, self._marker_set)
    
    # __repr__ is up to you

    # TODO
    # override extensions
    # legal extensions consist of all configurations that can be reached by
    # making a single jump from this configuration
    def extensions(self):
        """
        """
        pass
    # TODO
    # override is_solved
    # A configuration is solved when there is exactly one "*" left
    def is_solved(self):
        """
        """
        pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    from puzzle_tools import depth_first_solve

    grid = [["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", "*", "*", "*"],
            ["*", "*", ".", "*", "*"],
            ["*", "*", "*", "*", "*"]]
    gpsp = GridPegSolitairePuzzle(grid, {"*", ".", "#"})
    import time

    start = time.time()
    solution = depth_first_solve(gpsp)
    end = time.time()
    print("Solved 5x5 peg solitaire in {} seconds.".format(end - start))
    print("Using depth-first: \n{}".format(solution))