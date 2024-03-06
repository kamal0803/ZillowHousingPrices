from zillow_scrapping import ZillowScrapping
from form_filling import FormFilling

URL = "https://appbrewery.github.io/Zillow-Clone/"

zillow_scrapping = ZillowScrapping(URL)

prices, addresses, listing_links = zillow_scrapping.rent_details_scrapping()

prices = [zillow_scrapping.modified_prices(s) for s in prices]
addresses = [zillow_scrapping.clean_address(address) for address in addresses]

f = FormFilling()

for i in range(len(listing_links)):
    f.form_filling_inputs(addresses[i], prices[i], listing_links[i])