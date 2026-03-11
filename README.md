# KPL Fantasy Squad Scraper
=========================

A lightweight Python tool to extract player data from the **Kenya Premier League (KPL) Fantasy** website. The script navigates through team pages, extracts squad rosters (including Names, IDs, Positions, and Jersey Numbers), and organizes them into individual CSV files by team name.

🚀 Features
-----------

-   **Team-Based Scrapes:** Iterates through team IDs (1--22).

-   **Detailed Extraction:** Captures Player Name, Player ID, Squad Position, and Jersey Number.

-   **Automatic Organization:** Groups players by team and saves them into separate `.csv` files.

-   **Filename Sanitization:** Automatically cleans team names to ensure they are valid filenames.

-   **Rate Limiting:** Includes built-in delays to respect the website's server.

🛠️ Installation
----------------

1.  **Clone the repository** (or save the script to a folder):

    Bash

    ```
    git clone https://github.com/yourusername/kpl-fantasy-scraper.git
    cd kpl-fantasy-scraper

    ```

2.  **Install dependencies**:

    This script requires `requests` for fetching pages and `BeautifulSoup4` for parsing HTML.

    Bash

    ```
    pip install requests beautifulsoup4

    ```

📂 Usage
--------

Run the script directly from your terminal or command prompt:

Bash

```
python scraper.py

```

### How it works:

1.  The script creates a directory named `kpl_teams_data/`.

2.  It sends requests to `https://kplfantasy.com/team/{id}`.

3.  It parses the `squad-player-card` components.

4.  It saves each team's roster into its own file (e.g., `Ulinzi Stars.csv`).

📊 Output Structure
-------------------

After running, your project folder will look like this:

Plaintext

```
.
├── scraper.py
├── README.md
└── kpl_teams_data/
    ├── Gor Mahia.csv
    ├── Ulinzi Stars.csv
    ├── AFC Leopards.csv
    └── ... (22 files total)

```

### Sample CSV Content (`Ulinzi Stars.csv`):

| **Player ID** | **Player Name** | **Position** | **Jersey** |
| --- | --- | --- | --- |
| 1 | Byrne Omondi | Goalkeeper | 23 |
| 155 | Justin Opande | Defender | 30 |

⚠️ Disclaimer
-------------

This tool is for educational purposes and personal data analysis only. Please ensure you comply with the website's Terms of Service and `robots.txt` policies regarding automated data collection.
