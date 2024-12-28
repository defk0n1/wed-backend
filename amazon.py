from selectorlib import Extractor
import json
import requests

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('selectors.yml')

def scrape(url):
    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.com/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    print(f"Downloading {url}")
    r = requests.get(url, headers=headers)
    if r.status_code > 500:
        if "To discuss automated access to Amazon data please contact" in r.text:
            print(f"Page {url} was blocked by Amazon. Please try using better proxies")
        else:
            print(f"Page {url} must have been blocked by Amazon as the status code was {r.status_code}")
        return None

    # Extract data using the selector
    extracted_data = e.extract(r.text)

    if not extracted_data:
        return None

    # Extracting images data and parsing it if present
    if 'images' in extracted_data and extracted_data['images']:
        dynamic_image_data = json.loads(extracted_data['images'])

        # Construct image links based on size
        image_links = {}
        for link, size in dynamic_image_data.items():
            size_key = f"{size[0]}x{size[1]}"
            image_links[size_key] = link
    else:
        image_links = {}

    # Extract other product details
    title = extracted_data.get('name', None)
    price = extracted_data.get('price', None)
    short_description = extracted_data.get('short_description', None)
    rating = extracted_data.get('rating', None)
    number_of_reviews = extracted_data.get('number_of_reviews', None)
    variants = extracted_data.get('variants', [])
    product_description = extracted_data.get('product_description', None)
    sales_rank = extracted_data.get('sales_rank', None)
    link_to_all_reviews = extracted_data.get('link_to_all_reviews', None)

    # Return all the extracted product details
    return {
        "title": title,
        "price": price,
        "short_description": short_description,
        "images": image_links,
        "rating": rating,
        "number_of_reviews": number_of_reviews,
        "variants": variants,
        "product_description": product_description,
        "sales_rank": sales_rank,
        "link_to_all_reviews": link_to_all_reviews
    }
