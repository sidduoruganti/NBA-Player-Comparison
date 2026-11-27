# NBA Player Comparison: Compares two players stats and scores each one for a specific season

import requests

def get_points(player_id, season):
    
    url = f"https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/{player_id}/stats"
    response = requests.get(url)
    data = response.json()

    for category in data["categories"]:
        if category["name"] == "averages":
            pts_index = category["labels"].index("PTS")
            for row in category["statistics"]:
                if row["season"]["year"] == season:
                    return row["stats"][pts_index]
    return None

def search_players(name):

    url = "https://site.web.api.espn.com/apis/search/v2"
    response = requests.get(url, params={"query": name, "limit": 10})
    data = response.json()

    players = []
    for group in data.get("results", []):
        if group["type"] == "player":
            for item in group["contents"]:
                if "l:46" in item["uid"]:
                    player_id = item["uid"].split("a:")[1]
                    players.append((item["displayName"], player_id))
    return players


def choose_player(name):

    players = search_players(name)
    if len(players) == 0:
        print("No NBA players found for", name)
        return None

    for i, (display_name, player_id) in enumerate(players):
        print(i + 1, display_name)

    while True:
        choice = input("Pick a number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(players):
            return players[int(choice) - 1][1]
        print("Please enter a number from the list.")


name = input("Player name: ")
player_id = choose_player(name)
if player_id is not None:
    print(get_points(player_id, 2025))