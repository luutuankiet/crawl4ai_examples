# https://www.examtopics.com/discussions/google/view/7080-exam-professional-cloud-architect-topic-1-question-2/
# https://www.examtopics.com/discussions/google/view/54378-exam-professional-cloud-architect-topic-1-question-3/


import asyncio
from crawl4ai import (
    AsyncUrlSeeder, 
    AsyncWebCrawler, 
    SeedingConfig, 
    CrawlerRunConfig, 
    DefaultMarkdownGenerator,
    PruningContentFilter,
    CrawlResult

)
root_url = "https://docs.lightdash.com"

content_filter = PruningContentFilter(
)

crawl_config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
        content_filter=content_filter,
        options={
            "ignore_links": True,
        }
    ),
    verbose=True,
    stream=True
)


async def discover_urls(url: str) -> list:
    seed_config = SeedingConfig(
        live_check=True,
        extract_head=True,
        pattern="*/docs.lightdash.com/*",
        verbose=True
        )
    seeder = AsyncUrlSeeder()
    results = await seeder.urls(url,seed_config)
    results = [item['url'] for item in results]
        
    return results


def process_results(res: CrawlResult):
    if not res.success:
        return

    with open(f'./md/{res.metadata['title'].replace(' ','_').replace('/','_')}.md', 'w') as f:
        url = res.url
        title = res.metadata['title']
        markdown_content = res.markdown.fit_markdown

        output_block = (
            f"# {title}\n\n"
            f"**Source:** {url}\n\n"
            f"{markdown_content}\n\n"
        )
        f.write(output_block)

async def main():
    urls = await discover_urls(root_url)
    async with AsyncWebCrawler() as crawler:
        # async for result in await crawler.arun("https://cloud.google.com/looker/docs/admin-panel-general-localization",config=crawl_config):
        async for result in await crawler.arun_many(urls=urls,config=crawl_config):
            process_results(result)



if __name__ == "__main__":
    asyncio.run(main())
