from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys 
import time
import pandas as pd

chrome_driver = r"C:\Users\hp\Documents\chromedriver\chromedriver-win64\chromedriver.exe"
service = Service(chrome_driver)
driver = webdriver.Chrome(service=service)

# Navigate to IMDB Top 250 movies page
driver.get('https://www.imdb.com/chart/top/')

wait = WebDriverWait(driver, 30)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3.ipc-title__text')))

movies_data = []
count = 0

# Get all movie elements (top 10)
movie_elements = driver.find_elements(By.CSS_SELECTOR, 'li.ipc-metadata-list-summary-item')

for movie_element in movie_elements:
    if count >= 10:  # Only get top 10
        break
    
    try:
        # Get movie title
        title_element = movie_element.find_element(By.CSS_SELECTOR, 'h3.ipc-title__text')
        title = title_element.text.strip()
        
        # Get year - try to find it in metadata
        year = ""
        try:
            # Look for year in metadata items
            metadata_elements = movie_element.find_elements(By.CSS_SELECTOR, 'span.cli-title-metadata-item')
            for metadata in metadata_elements:
                text = metadata.text.strip()
                # Check if it's a 4-digit year
                if len(text) == 4 and text.isdigit() and 1900 <= int(text) <= 2030:
                    year = text
                    break
        except:
            year = "N/A"
        
        # Get rating - try multiple selectors
        rating = ""
        try:
            rating_element = movie_element.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--rating')
            rating = rating_element.text.strip()
        except:
            try:
                rating_element = movie_element.find_element(By.CSS_SELECTOR, '[data-testid="rating-value"]')
                rating = rating_element.text.strip()
            except:
                try:
                    rating_element = movie_element.find_element(By.CSS_SELECTOR, '.ipc-rating-star--rating')
                    rating = rating_element.text.strip()
                except:
                    rating = "N/A"
        
        # Get number of votes - try multiple selectors
        votes = ""
        try:
            votes_element = movie_element.find_element(By.CSS_SELECTOR, 'span.ipc-rating-star--total-votes')
            votes = votes_element.text.strip()
        except:
            try:
                votes_element = movie_element.find_element(By.CSS_SELECTOR, '[data-testid="rating-count"]')
                votes = votes_element.text.strip()
            except:
                try:
                    votes_element = movie_element.find_element(By.CSS_SELECTOR, '.ipc-rating-star--total-votes')
                    votes = votes_element.text.strip()
                except:
                    votes = "N/A"
        
        # Get movie link
        movie_link = ""
        try:
            link_element = movie_element.find_element(By.CSS_SELECTOR, 'a[href*="/title/"]')
            movie_link = link_element.get_attribute('href')
        except:
            movie_link = "N/A"
        
        movies_data.append({
            'Rank': count + 1,
            'Title': title,
            'Year': year,
            'Rating': rating,
            'Votes': votes,
            'IMDB_Link': movie_link
        })
        
        count += 1
        print(f"Scraped movie {count}: {title} ({year}) - Rating: {rating}")
        
    except Exception as e:
        print(f"Error scraping movie {count + 1}: {e}")
        continue

print(f"\nTotal movies scraped: {len(movies_data)}")

# Display results
for movie in movies_data:
    print(f"#{movie['Rank']}: {movie['Title']} ({movie['Year']}) - Rating: {movie['Rating']}")

print("Result displayed. Exiting the automation.")
driver.quit()

# Save to Excel
excel_file_save_path = r"E:\Programming data\Projects\Top10_IMDB_Movies.xlsx"
df = pd.DataFrame(movies_data)
df.to_excel(excel_file_save_path, index=False)
print(f"File saved at {excel_file_save_path}")