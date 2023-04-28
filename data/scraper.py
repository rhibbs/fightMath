import requests
from bs4 import BeautifulSoup

#Scraper for initial query
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

#Scraper for the individual fighter's page Once User Selected
async def history_scraper(url):
    #Follows same structure as above function
    results = []
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')
    table_rows = soup.find_all('tr', {'class': 'b-fight-details__table-row b-fight-details__table-row__hover js-fight-details-click'})
    for row in table_rows:
        name_cells = row.find_all('td', {'class': 'b-fight-details__table-col l-page_align_left'})
        if name_cells is not None:
        # Extract the fighter's name from the name cell
            for name in name_cells:
                if name is not None:
                    fight_matchup = name.find('a', {'class': 'b-link b-link_style_black'})
                    try:
                        opponent = fight_matchup.text
                        results.append(opponent)
                    #opponent = fight_matchup[1].a.text
                        #print(f"selected = {selected_fighter}")
                    #print(f"opponent = {opponent}")
                    except:
                        IndexError
                else:
                    pass
        return results

            #try:
            #    first = name_cells[0].a.text
            #    last = name_cells[1].a.text
            #    #results.append((first,last,link,wins,losses))
            #    #print(f"wins: {wins}")
            #    #print(f"losses: {losses}")
            #    print(f"First name: {first}")
            #    print(f"Last name: {last}")
            #    print(f"Name Cells: {name_cells}")
            #    #print(f"link : {link}")
            #    #print("------------------")    
            #except:
            #    IndexError

        #else:
        #    pass
#history_scraper('http://www.ufcstats.com/fighter-details/13b2f59210dda9cc')