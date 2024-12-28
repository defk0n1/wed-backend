# Amazon Product Scraper API

A FastAPI backend service that scrapes Amazon product pages and returns structured data. The API provides a simple endpoint to fetch product information by submitting an Amazon product URL.

## Features

- Scrapes product details from Amazon product pages
- Returns structured JSON data including:
  - Product title
  - Price
  - Rating
  - Number of reviews
  - Product description
  - Technical details
  - Images URLs
-

## API Endpoints

### POST /scrape

Scrapes product information from a provided Amazon URL.

**Request Body:**
```json
{
    "url": "https://www.amazon.com/dp/PRODUCT_ID"
}
```

**Response:**
```json
{
    "success": true,
    "data": {
        "title": "Product Title",
        "current_price": 99.99,
        "original_price": 129.99,
        "rating": 4.5,
        "review_count": 1234,
        "description": "Product description...",
        "features": ["Feature 1", "Feature 2"],
        "images": ["image_url_1", "image_url_2"],
        "technical_details": {
            "brand": "Brand Name",
            "model": "Model Number",
            "weight": "2.5 pounds"
        }
    }
}
```

## Error Responses

- **400 Bad Request**: Invalid Amazon URL
- **404 Not Found**: Product page not found
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Scraping failed

## Usage Example

```python
import requests

url = "http://localhost:8000/scrape"
payload = {
    "url": "https://www.amazon.com/dp/B01NAFJ86E"
}
response = requests.post(url, json=payload)
product_data = response.json()
```

## Dependencies

- FastAPI
- Requests
- Pydantic
- uvicorn
- selectorlib


## Important Notes

- This API is for educational purposes only
- Please review Amazon's robots.txt and terms of service before use
- Implement appropriate rate limiting to avoid IP blocks
- Consider using proxy rotation for production use
