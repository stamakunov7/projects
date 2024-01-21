def main():
    with open('script1.txt', 'r') as emp_file:
        sport = emp_file.readline().strip()
        team_name = emp_file.readline().strip()
        num_players = int(emp_file.readline().strip())

        print(f"Sport: {sport}")
        print(f"Team Name: {team_name}")
        print("Player Stats:")
        print()

        for _ in range(num_players):
            player_name = emp_file.readline().strip()
            num_games = int(emp_file.readline().strip())

            print(f"Player Name: {player_name}")
            print(f"Number of Games: {num_games}")

            for game in range(1, num_games + 1):
                game_stat = float(emp_file.readline().strip())
                print(f"Game {game}: {game_stat}")

            print()

if __name__ == '__main__':
    main()