# NBA Player Comparison Tool

A Python command-line tool that compares two NBA players' stats side by side and scores each one for a chosen season.

## The Problem

I have followed the NBA my whole life, and debates about who is the greatest of all time or whether one is better than another almost always come down to statistics. Finding credible numbers for a specific player and season means looking through multiple sources, which is slow and makes it hard to back up an argument. Without an easy way to compare players fairly, these debates stay shallow and rarely get the nuance they deserve.

## How It Works

I am building a Python command line program that lets you enter two NBA players and a season and prints their key stats side by side. It also calculates an overall score for each player from a weighted formula, so debates can be settled with clear, consistent numbers.

The MVP includes:

- Reading the API key from an environment variable and sending authenticated requests
- Looking up two players by name and season, and handling names the API cannot find
- Printing points, rebounds, assists, and shooting percentages side by side
- Calculating a weighted overall score and showing which player scores higher

![System diagram](docs/diagram.png)

The planning documents are in the `docs/` folder: the [Eisenhower matrix](docs/Eisenhower%20Matrix.pdf) and the system diagram source file, [diagram.drawio.xml](docs/diagram.drawio.xml).

## Tech Stack

- **Language:** Python
- **requests:** Sends the HTTP calls to the API and returns the JSON response
- **json:** Reads the data the API sends back into Python dictionaries
- **os:** Reads the API key from an environment variable
- **curl:** Used once in the terminal to test the API before writing any code
- **Git and GitHub:** Version control for the project, with the API key kept out of the code and the repo

## Roadmap

- [ ] Career-wide overall score across all seasons
- [ ] Percentile rankings against the rest of the league
- [ ] Playoff stats and advanced metrics such as PER
- [ ] Saving API responses to a local file to stay within rate limits
