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

# Create a chain of filters
filter_chain = FilterChain([
    # Only follow URLs with specific patterns
    URLPatternFilter(patterns=["*/google/*"]),

    # Only crawl specific domains
    DomainFilter(
        allowed_domains=["examtopics.com"],
    ),
])

content_filter = PruningContentFilter()


crawl_config = CrawlerRunConfig(
    deep_crawl_strategy=BFSDeepCrawlStrategy(
        filter_chain=filter_chain,
        max_depth=3,
        include_external=False
    ),
    verbose=True,
    stream=True
)


async def discover_urls() -> list:
    seed_config = SeedingConfig(
        live_check=True,
        extract_head=True,
        pattern="*/docs/*"
        )
    seeder = AsyncUrlSeeder()
    results = await seeder.urls(root_url,seed_config)
    # filtered_results = [res['url'] for res in results if not non_english.match(res['url'])]
        
    return results



def process_results(res: CrawlResult):
    if not res.success:
        return

    with open(f'./html/{res.metadata['title'].replace(' ','_')}.html', 'w') as f:
        f.write(res.html)

pattern = re.compile(r'^https:\/\/www\.examtopics\.com\/discussions\/google\/view\/.*machine-learning.*')
# root_url = "https://www.examtopics.com/discussions/google/view/305153-exam-professional-machine-learning-engineer-topic-1-question"
root_url = "https://www.examtopics.com"

async def main():
    urls = await dis

    async with AsyncWebCrawler() as crawler:
        async for result in await crawler.arun_many(root_url,config=crawl_config):
                if pattern.match(result.url):
                    process_results(result)



if __name__ == "__main__":
    asyncio.run(main())
