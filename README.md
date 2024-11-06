# Web Scraping Automation for Spanish Public Procurement Data

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Script Breakdown](#script-breakdown)
  - [1_DeepLinks.py](#1_deeplinkspy)
  - [2_ProjectFinder.py](#2_projectfinderpy)
  - [3_json2csv.py](#3_json2csvpy)
- [Technical Details](#technical-details)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project automates the extraction and organization of public procurement data from the Spanish government website [contrataciondelestado.es](https://contrataciondelestado.es). By orchestrating a series of Python scripts, it navigates through web pages, scrapes relevant data, and converts it into a structured CSV format for easy analysis.

## Features

- **Automated Deep Link Generation**: Navigate and extract specific URLs based on search criteria.
- **Data Extraction with Scrapy**: Crawl tender pages to extract detailed procurement information.
- **JSON to CSV Conversion**: Transform the scraped JSON data into CSV format.
- **Future-Proof Design**: Built with scalability and future enhancements in mind.

## Prerequisites

- Python 3.6 or higher
- **Libraries**:
  - `selenium`
  - `beautifulsoup4`
  - `scrapy`
  - `pandas`
- WebDriver for Selenium (e.g., ChromeDriver)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up WebDriver**

   - Download the appropriate WebDriver for your browser (e.g., [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)).
   - Ensure it's added to your system PATH or specify the path in `1_DeepLinks.py`.

## Usage

Run the main script to execute the entire workflow:

```bash
python 0_Main.py
```

This script will sequentially execute:

1. `1_DeepLinks.py` to generate deep links.
2. `2_ProjectFinder.py` to scrape procurement data.
3. `3_json2csv.py` to convert JSON data into CSV format.

## Script Breakdown

### 1_DeepLinks.py

This script scrapes specific URLs from the Spanish public procurement website.

- **Technologies Used**: Selenium, BeautifulSoup
- **Purpose**: Automate the navigation and extraction of deep-link URLs based on predefined search criteria.
- **Focus**: Extract data related to "Works" with a specific CPV code (41000000).

### 2_ProjectFinder.py

A Scrapy-based crawler designed to extract procurement details.

- **Technologies Used**: Scrapy
- **Purpose**: Scrape tender pages to extract information such as:
  - Contracting Authority
  - Tender Status
  - Contract Object
  - Base Budget
  - Contract Type
  - CPV Code
  - Location
  - Key Dates
  - Tender URL
- **Features**:
  - Custom User Agent and UTF-8 encoding for proper handling of Spanish text.
  - Designed as a `CrawlSpider` for scalability.

### 3_json2csv.py

Converts the JSON output from Scrapy into CSV format.

- **Technologies Used**: pandas
- **Purpose**: Flatten nested JSON structures and handle lists within JSON by converting them to strings.
- **Output**: `3_ProjectFinder.csv` containing structured data ready for analysis.


## Future Improvements

- **Enhanced Input**: Provide the crawler with a list of URLs from `1_DeepLinks.py` for expanded coverage.
- **PDF Downloading**: Implement functionality to download all PDF documents linked in the crawled URLs.
- **Data Export Options**: Improve export options for better data analysis, possibly integrating databases.
- **Robust Scraping Logic**: Enhance the crawler to handle inconsistencies across different tender pages.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the [GNU License](LICENSE).

## Contact

- **Author**: [Isidre Canyelles]
- **Email**: isidrecc@gmail.com
Feel free to reach out for any questions or collaboration opportunities.

---

*README.md file generated with ChatGPT*
