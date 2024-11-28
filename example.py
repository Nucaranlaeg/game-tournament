# Example tournament runner

def run_tournament(contestants, games, play_game):
	while len(contestants) > 1:
		winner = play_game(contestants[:4])[0]
		contestants = contestants[4:] + [winner]
	return winner
