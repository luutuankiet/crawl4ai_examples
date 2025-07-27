# crawl_prompt_engineering - Web Scraping for AI Best Practices

## Introduction
This project demonstrates the practical application of the `crawl4ai` Python library for web scraping. Its primary goal is to extract AI best practices content from the `promptingguide.ai` website, filter out non-English content, and consolidate it into a single, clean markdown document (`scraped.md`). This output is specifically designed for deep analysis in large language model (LLM) tools like NotebookLM.

## Features
*   **Efficient Web Crawling:** Leverages `crawl4ai` for high-performance and robust web scraping.
*   **Automatic URL Discovery:** Employs `AsyncUrlSeeder` to automatically discover and manage URLs from the target website, reducing manual configuration.
*   **Non-English Content Filtering:** Employs regular expressions to automatically filter out non-English pages, ensuring relevant content.
*   **Automated Markdown Generation:** Converts scraped HTML content into clean, readable markdown format using `DefaultMarkdownGenerator`.
*   **Optimized Content for LLMs (`fit_markdown`):** Utilizes `result.markdown.fit_markdown` to intelligently filter out hyperlinks and noise, producing much shorter, token-efficient content ideal for LLM consumption.
*   **Version-Controlled Configuration:** The initial seed URLs and crawling configurations are maintained under version control for reproducibility and easy modification.
*   **Sorted Output:** Scraped content is sorted by URL before being written to the output file, ensuring consistent and organized results.

## Project Structure
The core logic of this project resides within this directory:
*   [`main.py`](main.py): The main Python script that orchestrates the crawling process, including URL discovery, filtering, and markdown generation.
*   [`filtered_seeds.json`](filtered_seeds.json): A JSON file containing a pre-defined list of URLs that can be used as initial seeds for the crawler. The `main.py` script also performs live URL discovery from the `root_url`.
*   [`scraped.md`](scraped.md): The output file where all the scraped and processed markdown content is consolidated.

## Getting Started

### Prerequisites
*   Python 3.8 or higher
*   `pip` (Python package installer)

### Installation
1.  Install the `crawl4ai` library:
    ```bash
    pip install crawl4ai
    ```
2.  Run the `crawl4ai-setup` command to install necessary browser binaries for Playwright:
    ```bash
    crawl4ai-setup
    ```

### Execution
Navigate to this directory (`scripts/promptingguide_ai/`) and run the `main.py` script:
```bash
python main.py
```

Upon successful execution, a `scraped.md` file will be generated in this directory, containing the aggregated markdown content from the crawled website.

## Configuration
The crawling behavior can be customized by modifying the `main.py` script:
*   `root_url`: Change this variable to target a different website for crawling.
*   `non_english` regex: Adjust this regular expression to modify the filtering criteria for non-English content.
*   `filtered_seeds.json`: Update this file with specific URLs you wish to include or exclude from the initial seeding process.

## Use Case
This project provides a hands-on example of how to leverage `crawl4ai` to:
*   Rapidly gather structured and relevant information from websites.
*   Automate the process of preparing content for LLM training, fine-tuning, or retrieval-augmented generation (RAG) systems.
*   Maintain a version-controlled configuration for repeatable and auditable data collection.

## Future Enhancements
*   Implement more sophisticated content filtering mechanisms (e.g., based on keywords, content length, or specific HTML elements).
*   Add support for different output formats (e.g., JSON, CSV) in addition to Markdown.
*   Integrate with scheduling tools to automate periodic crawls and updates.
*   Expand error handling and logging for more robust operation.