'''
Jumble Challenge Solver

Given a word list and a word as user input, return matching “sub-anagrams”.

Example Run:

python3 jumble_solver.py word_list.txt dog
god
go
do

Word list used: http://www.mieliestronk.com/corncob_lowercase.txt 

Real Runtime:
time python3 jumble_solver.py word_list.txt elastodynamics
...
...
real    0m0.816s
user    0m0.729s
sys     0m0.062s

Worst Case Runtime Complexity:

Let 
    N = number of words in word_list
    K = length of longest word in list
    n = length of user input word
    k = n/2

Runtime of ingest_word_list will be O(NK) which is equivalent to O(N).

    Creating the word counter does require iterating through every character
    in the word list.
    However given that the largest word in the english dictionary is
    45 characters, we can treat K = 45 and this effectively becomes
    a constant operation.

Runtime of solve_jumble is O(n*C(n,k)*N),
        where C(n,k) = n choose k = n!/(k!*(n-k)!).

    We need to iterate through the full range of the input word's length
    to ensure we capture all potential "sub-anagrams" of the input word.
    For each length from 1...n we need to find all potential combinations,
    taking n!/(k!*(n-k)!) time.
    The most combinations will be found when k = n/2. Finally we need to
    print all of the matching anagrams, which worst case is the entire
    word list of size N.

'''
import sys
from collections import Counter, defaultdict
from itertools import combinations, permutations

# Anagram Lookup map with a collections.Counter as key
# and set of matching anagrams as values.
COUNTER_TO_ANAGRAMS = defaultdict(set)


def ingest_word_list(file_path: str):
    '''
    Given path to word list file, ingest all words into COUNTER_TO_ANAGRAMS.
    '''
    with open(file_path) as fp:
        for line in fp:
            word = line.strip()
            # Using frozenset to make counter hashable and ignore order.
            counter = frozenset(Counter(word).items())
            COUNTER_TO_ANAGRAMS[counter].add(word)


def solve_jumble(input_word: str):
    '''
    Given input_word, find all matching sub-anagrams in COUNTER_TO_ANAGRAMS.
    '''
    for i in range(1, len(input_word)+1):
        # Use combination instead of permutation because we do not
        # need to worry about letter order.
        combos = set(combinations(input_word, i))
        for combo in combos:
            counter = frozenset(Counter(combo).items())
            for word in COUNTER_TO_ANAGRAMS.get(counter, []):
                if word != input_word:
                    print(word)


if __name__ == '__main__':
    word_file = sys.argv[1]
    user_word = sys.argv[2]
    ingest_word_list(word_file)
    solve_jumble(user_word)
