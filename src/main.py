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


print(get_points(4277869, 2025))