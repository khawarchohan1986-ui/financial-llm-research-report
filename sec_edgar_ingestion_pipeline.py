"""
Project 1: Automated SEC EDGAR Financial Disclosures Ingestion Pipeline
Author: Khawar Abbas
Description: Resilient wrapper to ingest unstructured financial disclosures, 
SEC Form 10-K filings, and live earnings text streams for downstream analysis.
"""

import requests
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SECDataIngestionPipeline:
    def __init__(self, user_agent="KhawarAbbas research.contact@gmail.com"):
        self.headers = {"User-Agent": user_agent}
        self.base_url = "https://data.sec.gov/submissions/"

    def fetch_company_submissions(self, cik_str):
        """Fetches company submission history and unstructured filing metadata from SEC."""
        formatted_cik = str(cik_str).zfill(10)
        url = f"{self.base_url}CIK{formatted_cik}.json"
        
        try:
            logging.info(f"Fetching CIK data for: {formatted_cik}")
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                logging.error(f"Failed to fetch data. Status code: {response.status_code}")
                return None
        except Exception as e:
            logging.exception("An error occurred during API ingestion.")
            return None

if __name__ == "__main__":
    pipeline = SECDataIngestionPipeline()
    # Example CIK for Apple Inc.
    data = pipeline.fetch_company_submissions("0000320193")
    if data:
        logging.info("Successfully ingested metadata and filing streams.")
