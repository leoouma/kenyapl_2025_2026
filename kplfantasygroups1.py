import requests
from bs4 import BeautifulSoup
import csv
import time
import os

def scrape_and_group_by_team(start_team, end_team):
    base_url = "https://kplfantasy.com/team/"
    all_players = []
    
    # Create an output directory for the team files
    output_dir = "kpl_teams_data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Starting extraction for Teams {start_team} to {end_team}...")

    for team_id in range(start_team, end_team + 1):
        url = f"{base_url}{team_id}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            team_name = soup.find('h1').get_text(strip=True) if soup.find('h1') else f"Team_{team_id}"
            
            # Sanitize team name for filename (remove special characters)
            safe_team_name = "".join([c for c in team_name if c.isalnum() or c in (' ', '_')]).strip()
            team_filename = os.path.join(output_dir, f"{safe_team_name}.csv")
            
            player_cards = soup.find_all('div', class_='squad-player-card')
            team_players = []

            for card in player_cards:
                name_link = card.find('h3', class_='squad-player-name').find('a')
                player_name = name_link.get_text(strip=True)
                player_id = name_link['href'].split('=')[-1]
                
                position_el = card.find('p', class_='squad-player-position')
                position = position_el.get_text(strip=True) if position_el else "N/A"
                
                jersey_el = card.find('p', class_='squad-player-jersey')
                jersey = jersey_el.get_text(strip=True).replace("Jersey:", "").strip() if jersey_el else "N/A"
                
                team_players.append({
                    "Player ID": player_id,
                    "Player Name": player_name,
                    "Position": position,
                    "Jersey": jersey
                })

            # Save this specific team's file immediately
            if team_players:
                with open(team_filename, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=["Player ID", "Player Name", "Position", "Jersey"])
                    writer.writeheader()
                    writer.writerows(team_players)
                print(f"Saved {len(team_players)} players to {team_filename}")

            time.sleep(0.5)

        except Exception as e:
            print(f"Error on Team {team_id}: {e}")

if __name__ == "__main__":
    scrape_and_group_by_team(1, 22)