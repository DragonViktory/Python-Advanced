def team_lineup(*player_info):
    country_counts = {}
    players_by_country = {}

    for player, country in player_info:
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1

        if country in players_by_country:
            players_by_country[country].append(player)
        else:
            players_by_country[country] = [player]

    sorted_player_info = dict(sorted(players_by_country.items(), key=lambda x: (-len(x[1]), x[0])))

    formatted_output = []

    current_country = None
    for player, country in sorted_player_info.items():
        formatted_output.append(f"{player}:")
        for c in country:
            formatted_output.append(f"  -{c}")

    return "\n".join(formatted_output)

print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))