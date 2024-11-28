You are in charge of running a board game tournament.  Unfortunately, you only have one copy of the game and only so much time, so only a limited number of games can be played.  Similarly, you have a bunch of players but the game only accommodates up to four.  Since you want to run the best tournament possible, you want to ensure that the best player wins.

Your task, therefore is to write a function (in python, for ease of running in the controller) which runs a tournament - deciding who plays in which game, comparing results, and ultimately returning who wins.

## Spec

```
def run_tournament(contestants, games, play_game):
  # contestants: an array of contestant names
  # games: a number - this is the maximum number of games you're allowed to play
  # play_game: a function which takes an array of contestants and returns the outcome of a game which they all play

  # returns a single string, expected to be the name of one of the competitors
```

Each `contestant` is given a name and a skill value (hidden).  When a game is played, each contestant in the game generates a random integer from 0 to their skill value, and then the list of contestants is sorted based on the numbers generated.

`games` is guaranteed to be at least `(len(contestants)-1)/3`, enough that if you eliminate 3 contestants each round, you'll have one winner remaining.

`play_game` raises an exception if it is given more than four players or a game is started once all the allowed games have been played.  It returns the names of the four players it was passed, sorted so that the winner is first.

## Scoring

I will run 100000 games for each entry for each of 4 different tournament setups.  They can be found in the linked repository.  I may add another tournament setup if it appears necessary (in particular, if an entry seems to be abusing some facet of the current setups).

If your function raises an exception, no points are scored.  If your function returns the name of the contestant with the highest skill, you score one point.  The winner is the submission that scores highest on average across all of the tournament setups.  I may accept a winner once at least 2 weeks have passed since the last entry.

## Scores

| Entry | Ten weak players | Two groups | Huge pool | 32 skilled players | Average |
|-------|-----|-----|-----|-----|-----|
|example| 1800| 2127| 2589| 2518| 2259|

#### Average rank / number of contestants (for interest's sake)

| Entry | Ten weak players | Two groups | Huge pool | 32 skilled players | Average |
|-------|-----|-----|-----|-----|-----|
|example|.6796|.8055|.9520|.9011|.8345|