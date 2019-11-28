import scrapy

class Scraper(scrapy.Spider):
    name = 'bankier'
    pages = ['rynki , gielda , gospodarka , surowce  , fundusze , narzedzia , wiadomosci']
    start_urls = ['https://www.bankier.pl/']

    def parse(self, response):
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)