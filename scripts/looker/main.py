# https://www.examtopics.com/discussions/google/view/7080-exam-professional-cloud-architect-topic-1-question-2/
# https://www.examtopics.com/discussions/google/view/54378-exam-professional-cloud-architect-topic-1-question-3/


import asyncio
import os # Import os module
import re
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


from crawl4ai.deep_crawling.filters import (
    FilterChain,
    URLPatternFilter,
    DomainFilter,
    ContentTypeFilter
)

root_url = "https://cloud.google.com/looker/docs/intro"

# Define a custom filter to skip already processed URLs
# Removed BaseFilter inheritance as it's not directly importable
class AlreadyProcessedFilter:
    def __init__(self, processed_urls: set[str]):
        self.processed_urls = processed_urls

    async def apply(self, url: str, **kwargs) -> bool:
        # The filter method should return True to allow, False to block
        return url not in self.processed_urls

content_filter = PruningContentFilter(
)

# The filter_chain will be updated dynamically in main()
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
        filter_chain=filter_chain, # This will be updated in main()
        max_depth=5,
        include_external=False
    ),
    verbose=True,
    stream=True
)

def sanitize_filename(filename: str):
    # Replace non-breaking spaces with regular spaces
    filename = filename.replace('\xa0', ' ')
    # Replace any character that is not alphanumeric, space, hyphen, or underscore with an underscore
    filename = re.sub(r'[^\w\s-]', '_', filename)
    # Replace multiple spaces or underscores with a single underscore
    filename = re.sub(r'[\s_]+', '_', filename)
    # Remove leading/trailing underscores or hyphens
    filename = filename.strip('_-')
    return filename


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



async def get_processed_urls(md_dir: str = './md/') -> set[str]:
    """Reads existing markdown files and extracts source URLs."""
    processed_urls = set()
    if not os.path.exists(md_dir):
        return processed_urls

    for filename in os.listdir(md_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(md_dir, filename)
            try:
                with open(filepath, 'r') as f:
                    for line in f:
                        if line.startswith('**Source:**'):
                            url = line.replace('**Source:**', '').strip()
                            processed_urls.add(url)
                            break  # Found the URL, move to next file
            except Exception as e:
                print(f"Error reading file {filepath}: {e}")
    return processed_urls


def process_results(res: CrawlResult):
    if not res.success:
        # Removed res.error as it might not exist and caused Pylance error
        print(f"Failed to crawl: {res.url}")
        return
    
    # Ensure metadata is not None before accessing
    metadata = res.metadata if res.metadata is not None else {}
    try:
        filename = res.url.split('https://cloud.google.com/looker/docs/')[1]
    except IndexError:
        filename = ''
    filename = filename if filename != '' else metadata.get('title')
    if not filename:
        raise Exception(f"document filename cannot be built : url '{res.url}'")
    filename = sanitize_filename(filename)

    output_path = f'./md/{filename}.md'
    try:
        with open(output_path, 'w') as f:
            url = res.url
            title = metadata.get('title')
            # Ensure markdown is not None before accessing fit_markdown
            markdown_content = res.markdown.fit_markdown if res.markdown is not None else ""

            output_block = (
                f"# {title}\n\n"
                f"**Source:** {url}\n\n"
                f"{markdown_content}\n\n"
            )
            f.write(output_block)
        print(f"Successfully saved: {output_path}")
    except IOError as e:
        print(f"Error writing file {output_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while processing {res.url}: {e}")


non_english_pattern = re.compile(r'^https:\/\/cloud\.google\.com\/looker\/.*[?&]hl=[a-z]{2}(?:-[A-Z0-9]{2,})?')

async def main():
    processed_urls = await get_processed_urls()
    print(f"Found {len(processed_urls)} already processed URLs.")

    # Create the custom filter with the processed URLs
    already_processed_filter = AlreadyProcessedFilter(processed_urls)

    # Add the custom filter to the existing filter chain
    # Ensure the filter_chain is a new instance or mutable if it's shared
    # Convert filter_chain.filters tuple to a list before concatenation
    updated_filter_chain = FilterChain(list(filter_chain.filters) + [already_processed_filter])
    
    # Create a new CrawlerRunConfig with the updated filter_chain
    # This is important to ensure the deep_crawl_strategy uses the new filter
    updated_crawl_config = CrawlerRunConfig(
        markdown_generator=crawl_config.markdown_generator,
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            filter_chain=updated_filter_chain,
            max_depth=3,
            include_external=False
        ),
        verbose=crawl_config.verbose,
        stream=crawl_config.stream
    )

    async with AsyncWebCrawler() as crawler:
        # Revert to original arun for deep crawl, using the updated config
        async for result in await crawler.arun(root_url, config=updated_crawl_config):
            process_results(result) if not non_english_pattern.match(result.url) else None


if __name__ == "__main__":
    asyncio.run(main())
