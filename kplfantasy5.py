import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_kpl_by_teams(start_team, end_team):
    base_url = "https://kplfantasy.com/team/"
    all_players = []
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Starting extraction for Teams {start_team} to {end_team}...")

    for team_id in range(start_team, end_team + 1):
        url = f"{base_url}{team_id}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                print(f"Skipping Team {team_id}: Server returned {response.status_code}")
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the Team Name (usually the main page title)
            team_name = soup.find('h1').get_text(strip=True) if soup.find('h1') else f"Team {team_id}"
            
            # Find all player cards
            player_cards = soup.find_all('div', class_='squad-player-card')
            
            for card in player_cards:
                # 1. Extract Name and Player ID from the <a> tag
                name_link = card.find('h3', class_='squad-player-name').find('a')
                player_name = name_link.get_text(strip=True)
                player_url = name_link['href']
                player_id = player_url.split('=')[-1] # Extracts '1' from '/player?id=1'
                
                # 2. Extract Position
                position_el = card.find('p', class_='squad-player-position')
                position = position_el.get_text(strip=True) if position_el else "N/A"
                
                # 3. Extract Jersey Number
                jersey_el = card.find('p', class_='squad-player-jersey')
                jersey = jersey_el.get_text(strip=True).replace("Jersey:", "").strip() if jersey_el else "N/A"
                
                all_players.append({
                    "Team Name": team_name,
                    "Player ID": player_id,
                    "Player Name": player_name,
                    "Position": position,
                    "Jersey": jersey
                })
            
            print(f"Successfully scraped {len(player_cards)} players from {team_name}")
            time.sleep(0.5) # Polite delay

        except Exception as e:
            print(f"Error on Team {team_id}: {e}")

    return all_players

def save_to_csv(data):
    if not data:
        return
    
    filename = "kpl_full_roster.csv"
    keys = ["Team Name", "Player ID", "Player Name", "Position", "Jersey"]
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"\nSaved {len(data)} players to {filename}")

if __name__ == "__main__":
    # Range 1 to 22 as requested
    final_data = scrape_kpl_by_teams(1, 22)
    save_to_csv(final_data)