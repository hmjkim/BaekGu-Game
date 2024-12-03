import warnings
warnings.filterwarnings("ignore")


def stage():
    """
    Create a list representing stages of a hangman game as visual.

    :postcondition: return a list containing art strings 
    :return: list of art strings representing hangman stages.
    
    >>> stages = stage()
    >>> print(stages[0])
    <BLANKLINE>
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    <BLANKLINE>
    """
    stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''', '''
      +
      |
      |
      |
      |
      |
=========
''']
    return stages
