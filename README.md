KPL Fantasy Squad Scraper
=========================

A lightweight Python tool to extract player data from the **Kenya Premier League (KPL) Fantasy** website. The script navigates through team pages, extracts squad rosters (including Names, IDs, Positions, and Jersey Numbers), and organizes them into individual CSV files by team name.

🚀 Features
-----------

*   **Team-Based Scrapes:** Iterates through team IDs (1–22).
    
*   **Detailed Extraction:** Captures Player Name, Player ID, Squad Position, and Jersey Number.
    
*   **Automatic Organization:** Groups players by team and saves them into separate .csv files.
    
*   **Filename Sanitization:** Automatically cleans team names to ensure they are valid filenames.
    
*   **Rate Limiting:** Includes built-in delays to respect the website's server.
    

🛠️ Installation
----------------

1.  Bashgit clone https://github.com/yourusername/kpl-fantasy-scraper.gitcd kpl-fantasy-scraper
    
2.  This script requires requests for fetching pages and BeautifulSoup4 for parsing HTML.Bashpip install requests beautifulsoup4
    

📂 Usage
--------

Run the script directly from your terminal or command prompt:

Bash

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python scraper.py   `

### How it works:

1.  The script creates a directory named kpl\_teams\_data/.
    
2.  It sends requests to https://kplfantasy.com/team/{id}.
    
3.  It parses the squad-player-card components.
    
4.  It saves each team's roster into its own file (e.g., Ulinzi Stars.csv).
    

📊 Output Structure
-------------------

After running, your project folder will look like this:

Plaintext

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   .  ├── scraper.py  ├── README.md  └── kpl_teams_data/      ├── Gor Mahia.csv      ├── Ulinzi Stars.csv      ├── AFC Leopards.csv      └── ... (22 files total)   `

### Sample CSV Content (Ulinzi Stars.csv):

**Player IDPlayer NamePositionJersey**1Byrne OmondiGoalkeeper23155Justin OpandeDefender30

⚠️ Disclaimer
-------------

This tool is for educational purposes and personal data analysis only. Please ensure you comply with the website's Terms of Service and robots.txt policies regarding automated data collection.