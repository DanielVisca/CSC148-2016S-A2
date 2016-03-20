from puzzle import Puzzle


class WordLadderPuzzle(Puzzle):
    """
    A word-ladder puzzle that may be solved, unsolved, or even unsolvable.
    """

    def __init__(self, from_word, to_word, ws):
        """
        Create a new word-ladder puzzle with the aim of stepping
        from from_word to to_word using words in ws, changing one
        character at each step.

        @type from_word: str
        @type to_word: str
        @type ws: set[str]
        @rtype: None
        """
        (self._from_word, self._to_word, self._word_set) = (from_word,
                                                            to_word, ws)
        # set of characters to use for 1-character changes
        self._chars = "abcdefghijklmnopqrstuvwxyz"

        # TODO
        # implement __eq__ and __str__
        def __eq__(self, other):
            """
            @type self: WordLadderPuzzle
            @type: object
            @rtype: bool
            
            Return True if other is equal to self, otherwise return False
            
            >>> WordLadderPuzzle('ohno','popo','dunno')
            >>> other = WordLadderPuzzle('notthisone','nottrue','words')
            >>> WordLadderPuzzle.__eq__(other)
            False
            
            >>> WordLadderPuzzle('ohno','popo','dunno')
            >>> other = WordLadderPuzzle('ohno','popo','dunno')
            >>> WordLadderPuzzle.__eq__(other)
            True
            """
        # __repr__ is up to you

        # TODO
        # override extensions
        # legal extensions are WordPadderPuzzles that have a from_word that can
        # be reached from this one by changing a single letter to one of those
        # in self._chars     
#needs to be tested
        def extension(self, new_word):
            """
            @type self: WordLadderPuzzle
            @type: str
            @rtype: NoneType
            
            Change from_word to new_word if it only has a 1 character difference
            
            >>> WordLadderPuzzle._from_word = 'tired'
            >>> new_word = 'fired'
            >>> WordLadderPuzzle.extension(new_word)
#This example isnt done right
            >>> Print(from_word)
            fired
            
            >>> WordLadderPuzzle._from_word = 'tired'
            >>> new_word = 'lazy'
            >>> WordLadderPuzzle.extension(new_word)
#This example isnt done right
            >>> Print(from_word)
            tired
            """
            #Checking if it is a string of equal length
            if type(new_word) == str and len(new_word) == len(from_word):
                                                              
                #making sure there is no more than one different letter .                                   
                letters_dif = 0
                for i in range(len(from_word)):
                    if from_word[i] != new_word[i] and new_word[i] in \
                       self._chars:
                        letters_diff += 1
                if letters_d
                    from_word = new_word
                    
            
        # be reached from this one by changing a single letter to one of those
        # in self._chars

        # TODO
        # override is_solved
        # this WordLadderPuzzle is solved when _from_word is the same as
        # _to_word
        def is_solved(self):
            """
            @type self: WordLadderPuzzle
            @rtype: bool
            
            Return whether from_word is equal to to_word
            
            >>> WordPuzzleLadder._from_word = 'swagtastic'
            >>> WordPuzzleLadder._to_word = 'notswagtastic'
            False
            >>> WordPuzzleLadder._from_word = 'swagtastic'
            >>> WordPuzzleLadder._to_word = 'swagtastic'
            True
            """
#Should I check the type as well?
            return _from_word == _to_word
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    from puzzle_tools import breadth_first_solve, depth_first_solve
    from time import time
    with open("words", "r") as words:
        word_set = set(words.read().split())
    w = WordLadderPuzzle("same", "cost", word_set)
    start = time()
    sol = breadth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using breadth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))
    start = time()
    sol = depth_first_solve(w)
    end = time()
    print("Solving word ladder from same->cost")
    print("...using depth-first-search")
    print("Solutions: {} took {} seconds.".format(sol, end - start))