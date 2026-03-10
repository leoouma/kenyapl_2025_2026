import requests
from bs4 import BeautifulSoup
import csv
import time

def scrape_kpl_player_details(start_id, end_id):
    base_url = "https://kplfantasy.com/player?id="
    all_players = []
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    print(f"Extraction starting for {end_id - start_id + 1} possible IDs...")

    for p_id in range(start_id, end_id + 1):
        url = f"{base_url}{p_id}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code != 200:
                continue
            
            soup = BeautifulSoup(response.text, 'html.parser')
            details_div = soup.find('div', id='details')
            
            if not details_div:
                continue

            # Extract Name from <h2>
            name = details_div.find('h2').get_text(strip=True) if details_div.find('h2') else "Unknown"
            
            # Extract Squad Number and Team from <p> tags
            # We search for the specific label text within the paragraphs
            squad_number = "N/A"
            team_name = "N/A"
            
            paragraphs = details_div.find_all('p')
            for p in paragraphs:
                text = p.get_text()
                if "Squad Number:" in text:
                    squad_number = text.split("Squad Number:")[-1].strip()
                elif "Team:" in text:
                    team_name = text.split("Team:")[-1].strip()

            all_players.append({
                "Player ID": p_id,
                "Name": name,
                "Team": team_name,
                "Squad Number": squad_number
            })

            # Print progress every 50 players to stay updated
            if len(all_players) % 50== 0:
                print(f"Collected {len(all_players)} players (Current ID: {p_id})")

            time.sleep(0.2) # Small delay to avoid hammering the server

        except Exception as e:
            print(f"Error on ID {p_id}: {e}")

    return all_players

def save_to_csv(data):
    if not data:
        print("No data found to save.")
        return
    
    filename = "kpl_player_databasefull.csv"
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["Player ID", "Name", "Team", "Squad Number"])
        writer.writeheader()
        writer.writerows(data)
    print(f"\nFinished! {len(data)} players saved to {filename}")

if __name__ == "__main__":
    # Range 1 to 929 as requested
    scraped_data = scrape_kpl_player_details(1, 929)
    save_to_csv(scraped_data)