import requests
from bs4 import BeautifulSoup

# Set the URL of the website you want to scrape
#fighter_name = input("Type fighter last name, first name or nickname here: ")
async def scrape_fighters(fighter_name):
    url = f"http://www.ufcstats.com/statistics/fighters/search?query={fighter_name}"
    results = []
    # Send a request to the website and get the HTML content
    response = requests.get(url)
    html_content = response.content

    # Create a Beautiful Soup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the table row with class 'b-statistics__table-row'
    table_rows = soup.find_all('tr', {'class': 'b-statistics__table-row'})

    # Find the table cells with class 'b-statistics__table-col'
    for row in table_rows:
        # Find the table cell with the fighter's name
        name_cells = row.find_all('td', {'class': 'b-statistics__table-col'})
        if name_cells is not None:
        # Extract the fighter's name from the name cell
            try:
                link = row.find('a').get('href')
                first = name_cells[0].a.text
                last = name_cells[1].a.text
                wins = name_cells[7].text
                losses = name_cells[8].text
                results.append((first,last,link,wins,losses))
                #print(f"wins: {wins}")
                #print(f"losses: {losses}")
                #print(f"First name: {first}")
                #print(f"Last name: {last}")
                #print(f"link : {link}")
                #print("------------------")    
            except:
                IndexError

        else:
            pass
    return results