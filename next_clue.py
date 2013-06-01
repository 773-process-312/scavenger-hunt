import os
import sys
import random
import generate_clues as gc

def check_hint(clue, hint):
    if (clue == 3):
        count = len(os.listdir("/usr"))
        return hint == count

if __name__ == "__main__":

    if (len(sys.argv) != 4):
        sys.exit("Need a secret number, clue number, and hint")
    secret_number = int(sys.argv[1])
    clue_number = int(sys.argv[2])
    hint_number = int(sys.argv[3])

    clue_indexes = gc.gen_clue_list(gc.START_CLUE, gc.LAST_CLUE,
                                    gc.CLUE_SPACE, secret_number)
    print clue_indexes
    if (check_hint(clue_number, hint_number)):
        print clue_indexes[clue_number - gc.START_CLUE]
    else:
        R = random.Random()
        R.seed(secret_number + clue_number + hint_number)
        print R.randint(1, gc.CLUE_SPACE)



