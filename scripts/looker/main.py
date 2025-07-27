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
    BFSDeepCrawlStrategy,
    CrawlResult

)
import re


from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    DomainFilter,
    ContentTypeFilter
)

root_url = "https://cloud.google.com/looker/docs/intro"


content_filter = PruningContentFilter(
)

filter_chain = FilterChain([
    # Only follow URLs with specific patterns
    URLPatternFilter(patterns=["*/looker/*"]),

    # Only crawl specific domains
    # DomainFilter(
    #     allowed_domains=["cloud.google.com"],
    # ),
])

crawl_config = CrawlerRunConfig(
    markdown_generator=DefaultMarkdownGenerator(
        content_filter=content_filter,
        options={
            "ignore_links": True,
        }
    ),
    deep_crawl_strategy=BFSDeepCrawlStrategy(
        filter_chain=filter_chain,
        max_depth=5,
        include_external=False
    ),
    verbose=True,
    stream=True
)


async def discover_urls() -> list:
    seed_config = SeedingConfig(
        live_check=True,
        extract_head=True,
        pattern="*/docs/*",
        verbose=True
        )
    seeder = AsyncUrlSeeder()
    results = await seeder.urls(root_url,seed_config)
        
    return results



def process_results(res: CrawlResult):
    if not res.success:
        return

    with open(f'./md/{res.metadata['title'].replace(' ','_')}.md', 'w') as f:
        url = res.url
        title = res.metadata['title']
        markdown_content = res.markdown.fit_markdown

        output_block = (
            f"# {title}\n\n"
            f"**Source:** {url}\n\n"
            f"{markdown_content}\n\n"
        )
        f.write(output_block)



# async def main():
#     urls = await discover_urls()
#     async with AsyncWebCrawler() as crawler:
#         async for result in await crawler.arun_many(urls,config=crawl_config):
#             process_results(result)


non_english_pattern = re.compile(r'^https:\/\/cloud\.google\.com\/looker\/.*[?&]hl=[a-z]{2}(?:-[A-Z0-9]{2,})?')

async def main():
    async with AsyncWebCrawler() as crawler:
        # async for result in await crawler.arun("https://cloud.google.com/looker/docs/admin-panel-general-localization",config=crawl_config):
        async for result in await crawler.arun(root_url,config=crawl_config):
            process_results(result) if not non_english_pattern.match(result.url)  else None



if __name__ == "__main__":
    asyncio.run(main())
