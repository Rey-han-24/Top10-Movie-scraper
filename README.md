🎬 IMDb Top 10 Scraper – Python Automation Project

A fully automated Python project that scrapes IMDb’s Top 10 movies and exports the data into Excel.

📌 Features
✅ Scrapes the Top 10 movies from IMDb
✅ Extracts: Rank, Title, Year, Rating, and Link
✅ Selenium automates browser interaction
✅ Data is saved in an Excel spreadsheet using Pandas
✅ Fully automated – run and get fresh data instantly

🧰 Tech Stack
Python 3
Selenium
Pandas
openpyxl
Chrome + ChromeDriver (or any supported browser)

🚀 How It Works
Launch the Python script
Selenium opens IMDb Top 250 page
Scrapes data for the first 10 movies
Stores the data in a Pandas DataFrame
Exports the data to IMDb_Top_10.xlsx

💡 See the image below for a visual flowchart of the process.

📦 Output Sample
Rank | Title               | Year | Rating | Link
1    | The Shawshank...    | 1994 | 9.2    | https://imdb.com/...
2    | The Godfather       | 1972 | 9.1    | https://imdb.com/...
...


🛠 Setup Instructions
Clone this repo:
git clone https://github.com/Rey-han-24/Top10-Movie-scraper.git
cd Top10-Movie-scraper

Install dependencies:
pip install -r requirements.txt

Run the script:
python main.py

tip: Make sure to have chrome driver installed and edit the path with the one in the code 
