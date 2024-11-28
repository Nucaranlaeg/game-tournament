import random
import sys
from importlib import import_module
from tqdm import tqdm

scenarios = [
	# {
	# 	"name": "One good player",
	# 	"contestants": [
	# 		{"name": "A", "skill": 2},
	# 		{"name": "B", "skill": 3},
	# 		{"name": "C", "skill": 4},
	# 		{"name": "D", "skill": 1000},
	# 	],
	# 	"games": 2,
	# },
	{
		"name": "Ten weak players",
		"contestants": [
			{"name": "A", "skill": 20},
			{"name": "B", "skill": 21},
			{"name": "C", "skill": 22},
			{"name": "D", "skill": 23},
			{"name": "E", "skill": 24},
			{"name": "F", "skill": 25},
			{"name": "G", "skill": 26},
			{"name": "H", "skill": 27},
			{"name": "I", "skill": 28},
			{"name": "J", "skill": 29},
		],
		"games": 4,
	},
	{
		"name": "Two groups",
		"contestants": [
			{"name": "A", "skill": 10},
			{"name": "B", "skill": 11},
			{"name": "C", "skill": 12},
			{"name": "D", "skill": 13},
			{"name": "E", "skill": 14},
			{"name": "F", "skill": 101},
			{"name": "G", "skill": 102},
			{"name": "H", "skill": 103},
			{"name": "I", "skill": 104},
			{"name": "J", "skill": 105},
		],
		"games": 12,
	},
	{
		"name": "Huge pool",
		"contestants": [
			{"name": "A", "skill": 10},
			{"name": "B", "skill": 11},
			{"name": "C", "skill": 13},
			{"name": "D", "skill": 15},
			{"name": "E", "skill": 17},
			{"name": "F", "skill": 19},
			{"name": "G", "skill": 21},
			{"name": "H", "skill": 24},
			{"name": "I", "skill": 27},
			{"name": "J", "skill": 30},
			{"name": "K", "skill": 33},
			{"name": "L", "skill": 37},
			{"name": "M", "skill": 41},
			{"name": "N", "skill": 46},
			{"name": "O", "skill": 51},
			{"name": "P", "skill": 57},
			{"name": "Q", "skill": 63},
			{"name": "R", "skill": 70},
			{"name": "S", "skill": 77},
			{"name": "T", "skill": 85},
			{"name": "U", "skill": 94},
			{"name": "V", "skill": 104},
			{"name": "W", "skill": 115},
			{"name": "X", "skill": 127},
			{"name": "Y", "skill": 140},
			{"name": "Z", "skill": 154},
			{"name": "a", "skill": 170},
			{"name": "b", "skill": 188},
			{"name": "c", "skill": 207},
			{"name": "d", "skill": 228},
			{"name": "e", "skill": 251},
			{"name": "f", "skill": 277},
			{"name": "g", "skill": 305},
			{"name": "h", "skill": 336},
			{"name": "i", "skill": 370},
			{"name": "j", "skill": 408},
			{"name": "k", "skill": 449},
			{"name": "l", "skill": 494},
			{"name": "m", "skill": 544},
			{"name": "n", "skill": 599},
			{"name": "o", "skill": 659},
			{"name": "p", "skill": 725},
			{"name": "q", "skill": 798},
			{"name": "r", "skill": 878},
			{"name": "s", "skill": 966},
			{"name": "t", "skill": 1063},
			{"name": "u", "skill": 1170},
			{"name": "v", "skill": 1287},
			{"name": "w", "skill": 1416},
			{"name": "x", "skill": 1558},
			{"name": "y", "skill": 1714},
			{"name": "z", "skill": 1886},
		],
		"games": 20,
	},
	{
		"name": "32 skilled players",
		"contestants": [
			{"name": "A", "skill": 1000},
			{"name": "B", "skill": 1100},
			{"name": "C", "skill": 1300},
			{"name": "D", "skill": 1500},
			{"name": "E", "skill": 1700},
			{"name": "F", "skill": 1900},
			{"name": "G", "skill": 2100},
			{"name": "H", "skill": 2400},
			{"name": "I", "skill": 2700},
			{"name": "J", "skill": 3000},
			{"name": "K", "skill": 3300},
			{"name": "L", "skill": 3700},
			{"name": "M", "skill": 4100},
			{"name": "N", "skill": 4600},
			{"name": "O", "skill": 510},
			{"name": "P", "skill": 570},
			{"name": "Q", "skill": 630},
			{"name": "R", "skill": 700},
			{"name": "S", "skill": 770},
			{"name": "T", "skill": 850},
			{"name": "U", "skill": 940},
			{"name": "V", "skill": 1040},
			{"name": "W", "skill": 1150},
			{"name": "X", "skill": 1270},
			{"name": "Y", "skill": 1400},
			{"name": "Z", "skill": 1540},
			{"name": "a", "skill": 1700},
			{"name": "b", "skill": 1880},
			{"name": "c", "skill": 2070},
			{"name": "d", "skill": 2280},
			{"name": "e", "skill": 2510},
			{"name": "f", "skill": 2770},
		],
		"games": 32,
	},
]

def make_games(contestants, games):
	def play_game(players):
		if len(players) > 4:
			raise "Too many players"
		nonlocal games
		games -= 1
		if games < 0:
			raise "Too many games played"
		players = [[x, random.randint(0, x["skill"])] for x in contestants if x["name"] in players]
		players.sort(key=lambda x: -x[1])
		return [x[0]["name"] for x in players]
	return play_game

def run_tournament(tournament, contestants, games, trials):
	correct_wins = 0
	avg_rank = 0
	best_skill = max([x["skill"] for x in contestants])
	for i in tqdm(range(trials)):
		random.shuffle(contestants)
		try:
			winner = tournament([x["name"] for x in contestants], games, make_games(contestants, games))
			winner_skill = [x["skill"] for x in contestants if x["name"] == winner][0]
			if winner_skill == best_skill:
				correct_wins += 1
			winner_pos = sum([1 for x in contestants if x["skill"] <= winner_skill])
			avg_rank += winner_pos / len(contestants)
		except KeyboardInterrupt:
			raise
		except:
			pass
	return correct_wins, avg_rank

def run_all_scenarios(tournament):
	trials = 100000
	correct_wins = 0
	avg_rank = 0
	for scenario in scenarios:
		print(f"Running {scenario['name']}...")
		scenario['correct_wins'], scenario['avg_rank'] = run_tournament(tournament, scenario['contestants'], scenario['games'], trials)
		correct_wins += scenario['correct_wins']
		avg_rank += scenario['avg_rank']
	for scenario in scenarios:
		print(f"{scenario['name']:20}: {scenario['correct_wins']:.4f}    {scenario['avg_rank']:.4f}")
	print(f"{'Average':20}: {correct_wins / len(scenarios):.4f}    {avg_rank / len(scenarios):.4f}")

tourney = import_module(sys.argv[1])
run_all_scenarios(tourney.run_tournament)
