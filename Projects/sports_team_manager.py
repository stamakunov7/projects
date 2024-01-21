def main():
    sport = input("Enter the sport: ")
    team_name = input("Enter the team name: ")
    num_players = int(input("Enter the number of players for record: "))

    with open('script1.txt', 'w') as emp_file:

        emp_file.write(f"{sport}\n")
        emp_file.write(f"{team_name}\n")
        emp_file.write(f"{num_players}\n")

        for i in range(1, num_players + 1):
            print("Enter data: ")
            player_name = input("Player name: ")
            num_games = int(input("Enter the number of games: "))

            emp_file.write(f"{player_name}\n")
            emp_file.write(f"{num_games}\n")

            for game in range(1, num_games + 1):
                game_stat = float(input(f"Game {game}: "))
                emp_file.write(f"{game_stat}\n")

    print()
    print("Statistics have been recorded and saved to script1.txt")

if __name__ == '__main__':
    main()