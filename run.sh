#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run scraper with arguments
python3 lead_scraper.py "$@"
