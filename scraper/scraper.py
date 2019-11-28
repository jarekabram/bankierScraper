import scrapy

class Scraper(scrapy.Spider):
    name = 'bankier'
    pages = ['rynki' , 'gielda' , 'gospodarka' , 'surowce' , 'fundusze' , 'narzedzia' , 'wiadomosci']
    subpage = 'wiadomosci'
    start_url = 'https://www.bankier.pl/'

    def start_requests(self):
        urls = []
        for page in self.pages:
            full_website = self.start_url + page
            urls.append(full_website)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)