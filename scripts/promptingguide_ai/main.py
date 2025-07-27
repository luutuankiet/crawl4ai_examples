import asyncio
from crawl4ai import (
    AsyncUrlSeeder, 
    AsyncWebCrawler, 
    SeedingConfig, 
    CrawlerRunConfig, 
    DefaultMarkdownGenerator,
    PruningContentFilter
)
import re


non_english = re.compile(r'^https:\/\/www\.promptingguide\.ai\/[a-z]{2}\/')
root_url = "https://www.promptingguide.ai"

async def discover_urls() -> list:
    seed_config = SeedingConfig(
        live_check=True,
        extract_head=True,
        )
    seeder = AsyncUrlSeeder()
    results = await seeder.urls(root_url,seed_config)
    filtered_results = [res['url'] for res in results if not non_english.match(res['url'])]
        
    return filtered_results



async def main():
    urls = await discover_urls()
    content_filter = PruningContentFilter()
    crawl_config = CrawlerRunConfig(
        markdown_generator=DefaultMarkdownGenerator(
            content_filter=content_filter,
            options={
                "ignore_links": True,
            }
        ),
    )
    async with AsyncWebCrawler() as crawler:
        results = await crawler.arun_many(
            urls=urls,
            config=crawl_config
        )
        passed_results = []
        for result in results:
            if result.success:
                passed_results.append(result)


    # Sort the list by the 'url' value in each dictionary
        sorted_results = sorted(passed_results, key=lambda result: result.url)


        # Now, loop over the newly sorted list to write to the file
        with open('scraped.md', 'w') as f:
            for result in sorted_results: 
                url = result.url
                title = result.metadata['title']
                markdown_content = result.markdown.fit_markdown

                output_block = (
                    f"---\n\n"
                    f"# {title}\n\n"
                    f"**Source:** {url}\n\n"
                    f"{markdown_content}\n\n"
                )
                f.write(output_block)


if __name__ == "__main__":
    asyncio.run(main())
