from subprocess import Popen, PIPE
import sys
from time import sleep

sleeptime = 0
def run_tournament(contestants, games, play_game):
    # contestants: an array of contestant names
    # games: a number - this is the maximum number of games you're allowed to play
    # play_game: a function which takes an array of contestants and returns the outcome of a game which they all play
    # returns a single string, expected to be the name of one of the competitors
    process = Popen([arg for arg in sys.argv[2:]], stdout=PIPE, stdin=PIPE, text=True, universal_newlines=True, bufsize=1)
    process.stdin.write(str(len(contestants)) + "\n")
    for c in contestants:
        process.stdin.write(c + "\n")
    process.stdin.write(str(games) + "\n")
    i=0
    while i<games:
        #sleep(sleeptime)
        line = process.stdout.readline().strip()
        if line == "run":
            #sleep(sleeptime)
            numplayers = int(process.stdout.readline())
            players = []
            for j in range(numplayers):
                #sleep(sleeptime)
                players.append(process.stdout.readline().strip())
            res = play_game(players)
            for p in res:
                process.stdin.write(p+"\n")
            i+=1
        elif line == "ret":
            #sleep(sleeptime)
            return process.stdout.readline().strip()
        else:
            raise ChildProcessError("Command not in [run, ret] recieved")
    raise ChildProcessError("No games are left, but never returned")

# run using: python3 main.py helper $(which <program>) [additional args passed to program...]

# https://codegolf.stackexchange.com/a/276954/82199
