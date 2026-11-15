# API Test Notes

## Why I tested this
My original plan used an NBA API with an API key. However, The free key options made me pay for all single player statistics, so I tested ESPN's public endpoints with curl instead.

## What I tested
Each line below is a request I ran in the terminal. None of them needed an API key.

Search for a player by name (this also finds retired players):

curl -s "https://site.web.api.espn.com/apis/search/v2?query=kobe%20bryant&limit=5"

Get every season for one player (Kareem Abdul-Jabbar here):

curl -s "https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/4145/stats"

Get one season for one player, which I used to double-check numbers (Jose Alvarado, 2024-25):

curl -s "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2025/types/2/athletes/4277869/statistics"

Get a player's record for one season (Kobe Bryant, 2007-08):

curl -s "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2008/athletes/110?lang=en&region=us"

Get a team's record for one season (the Lakers, 2007-08):

curl -s "https://sports.core.api.espn.com/v2/sports/basketball/leagues/nba/seasons/2008/teams/13?lang=en&region=us"

## What I found about searching
- ESPN has two search endpoints. The older one, "common/v3/search", only found current players. It had no NBA results for Kobe Bryant or Michael Jordan.
- The newer one, "apis/search/v2", found both of them. It also returns players from other sports and from college, so my program will keep only the NBA entries. Those have "l:46" in their uid, and the player ID is the number after "a:". For example, Kobe is 110, Jordan is 1035, Iverson is 366, and Kareem is 4145.

## What I found about stats
- ESPN has two ways to get stats. The career endpoint ("common/v3") gives every season for a player in one request. The season endpoint ("core") gives one season per request.
- The season endpoint has gaps. For Kareem Abdul-Jabbar it said "No stats found" for every year I tried from 1970 to 1989, even though his player record exists. The career endpoint had his seasons from 1976 on. Neither had his 1970 to 1975 seasons.
- The career endpoint covered the other players I tried from start to finish, such as Jordan (1985 to 2003) and Kobe (1997 to 2016).
- Each row is one season. The row names the year and the team, and it holds a list of numbers. A separate list of labels says what each number means, in the same order. For example, GP is games played and PTS is points. The numbers come as text, so my code will convert them.
- If a player was traded in the middle of a season, that season has more than one row. Alvarado's 2025-26 season has one row for each team plus a "Totals" row. I will use the Totals row.
- The two endpoints agree. Alvarado's 2024-25 season shows 56 games and 10.3 points per game on the career endpoint, and 56 games and 10.339286 on the season endpoint. The career endpoint rounds to one decimal place.
- Old seasons have real numbers. Jordan averaged 28.2 points in 1984-85 (ESPN returned 28.207317) and 30.4 points in 1995-96 (ESPN returned 30.378048, which is 2,491 points over 82 games). I checked the 1995-96 number against Land of Basketball and it matched: https://www.landofbasketball.com/nba_players_season_stats/1996/michael_jordan.htm
- Early seasons show zeros for things that were not counted yet. Kareem's 1976 row has 0.0 turnovers and no three-pointers. These zeros mean "not recorded," so my formula cannot count them.
- A few stats only exist for some seasons (DRPM, WARP, RPM, ORPM, and plusMinus), so I will not use them.

## Position and team
- Position seems to be one value per player, not one per season. Kobe shows SF, and Kareem's is "NA." I will show it only to help tell apart players with the same name.
- Team does change by season. Kobe in 2008 returned the Lakers (LAL).

## My plan
- Search by name with "apis/search/v2", keep the NBA entries, and read the player ID.
- Get stats from the career endpoint and pick the row for the season the user asked for. If there is no row for that season, show a "no stats found" message.

## Things to watch
- ESPN's endpoints are unofficial, so they could change without notice.
- ESPN names a season by the year it ends, so 2025 means 2024-25.
