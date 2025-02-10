# German Real Estate Market Analysis Tool 🏠

## Overview
This project provides a comprehensive analysis tool for the German real estate market, focusing on major cities including Berlin, Munich, Hamburg, Frankfurt, and Cologne. The tool collects property data, performs statistical analysis, and generates visual insights about market trends.

## Features
- 🤖 Automated data collection from real estate listings
- 📊 Statistical analysis of property prices
- 📈 Data visualization and reporting
- 🗺️ City-based market comparison
- 📝 Detailed logging system

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
1. Clone the repository
git clone https://github.com/shaumne/German-Real-Estate
cd german-real-estate-analysis

2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

## Usage

### Running the Scraper
python german_real_estate_scraper.py

### Generating Visualizations
python visualization.py

## Project Structure
```
german-real-estate-analysis/
├── german_real_estate_scraper.py  # Main scraper implementation
├── visualization.py               # Data visualization module
├── requirements.txt              # Project dependencies
├── .gitignore                    # Git ignore rules
└── README.md                     # Project documentation
```

## Output Files
- real_estate_data_YYYYMMDD.csv: Raw data export
- price_analysis.png: Price comparison visualization
- sqm_price_analysis.png: Price per square meter analysis
- scraper_log_YYYYMMDD.log: Operation logs

## Data Analysis Features
- Average property prices by city
- Price per square meter distribution
- Room count analysis
- Price trends over time
- Statistical summaries

## Contributing
1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- Beautiful Soup documentation
- Pandas documentation
- Seaborn visualization gallery
