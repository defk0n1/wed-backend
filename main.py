from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from amazon import scrape  # Replace with the actual name of your scraper script module

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define a request schema
class ScrapeRequest(BaseModel):
    url: str    

@app.post("/scrape")
async def scrape_product(request: ScrapeRequest):
    url = request.url
    try:
        # Call your scraper script function
        product_data = scrape(url)  # Update to match your function name
        if not product_data:
            raise ValueError("Failed to scrape data")
        return {"success": True, "data": product_data}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

