import scrapy

# Define a new spider
class PlayersSpider(scrapy.Spider):
    name = 'players'    
    # Start scraping from these URLs
    start_urls = [f'https://hoopshype.com/salaries/players/{yr}-{yr+1}/' for yr in range(2020, 2021)]
    counter = 0   # Counter to limit the number of items scraped
    
    # Set the delay between consecutive requests to 2 seconds to avoid overloading the server
    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }
    # This function parses the initial response
    def parse(self, response):
        # Loop over each row in the table except the header
        for row in response.css('table.hh-salaries-ranking-table tr')[1:]:
            if self.counter >= 100: # Break the loop if 100 players have been scraped
                break

            # Extract the player's name and link
            player_name = row.css('td.name a::text').get().strip()
            player_link = row.css('td.name a::attr(href)').get()
            
            # If the link is relative, make it absolute
            if player_link is not None and "http" not in player_link:
                player_link = response.urljoin(player_link)
            
            self.counter += 1   # Increment the counter

            # Make a request to the player's page to extract more data
            yield scrapy.Request(url=player_link, callback=self.parse_player, meta={'player_name': player_name, 'year': response.url.split('/')[-2].split('-')[0], 'player_link': player_link})
    
    # This function parses the player's page
    def parse_player(self, response):
        # Extract the player's date of birth and salary
        born = response.css('b:contains("Born:") + span.player-bio-text-line-value::text').get(default='N/A').strip()
        salary = response.css('b:contains("Salary:") + span.player-bio-text-line-value::text').get(default='N/A').strip()
        
        # Yield the data as a dictionary
        yield {
            'Player': response.meta.get('player_name'),
            'Salary': salary,
            'Year': response.meta.get('year'),
            'Link': response.meta.get('player_link'),
            'Born': born,
        }
