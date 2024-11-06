from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.loader import ItemLoader
from scrapy.linkextractors import LinkExtractor

#FIRST VERSION OF THE CRAWLSPIDER ONLY WITH ONE URL
#IN THE NEXT STEP WE WILL FEED THE CRAWLSPIDER WITH MULTIPLE URLs
#FOR FURTHER STEPS WE WILL ALSO TRY TO DOWNLOAD ALL THE PDFs IN THE PAGE
#AT SOME POINT I SHOULD IMPLEMENT SOME KIND OF CODE TO MAKE IT EASER TO REVIEW ALL THE RESPONSES FROM SCRAPY

#Defines all the items we want to extract
class claselicitacion(Item):
    organo_contratacion = Field()
    estado_licitacion = Field()
    objeto_contrato = Field()
    presupuesto_base = Field()
    tipo_contrato = Field()
    codigo_cpv = Field()
    ubicacion = Field()
    fecha = Field()
    url = Field()

#Defines the type of spider, in this case we could use a "normal" spide but since this is a first draft and it will get complicated
#we prefere to start using from now "cralwspider"
class LicitacionCrawlSpider(CrawlSpider):
    name = 'licitacion_crawl'

    #It's important to specify that the site is written in spanish and it has to use the UTF-8 encoding
    #THe "presupuesto base" changes it's format depending on the language of the user agent, we define it as spanish
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'ROBOTSTXT_OBEY': False,
        'FEED_EXPORT_ENCODING': 'utf-8',  # Add this for proper encoding
        'FEEDS': {
            '2_ProjectFinder.json': {
                'format': 'json',
                'encoding': 'utf-8',  # Specify UTF-8 encoding
                'indent': 4,
            },
#               I've tried to import to a .csv file, but it imports it to a single row and is separated with comas
#               Maybe is better to import only to a json file and then convert the json file to a csv file
#                'ProjectFinder.csv': {
#                'format': 'csv',
#                'encoding': 'utf-8'
#            },
        },
        'DEFAULT_REQUEST_HEADERS': {
            'Accept-Language': 'es-ES,es;q=0.9',    #Specify language to spanish to keep the numbers format in spain type
        }
    }

    #We start with one URL, but I'll get more complicated
    start_urls = [
        'https://contrataciondelestado.es/wps/poc?uri=deeplink%3Adetalle_licitacion&idEvl=%2FDc2yfrXk2%2BIzo3LHNPGcQ%3D%3D'
        ]
    
    #We have to define some rules, even if we don't want the crawlspider to go to anyother links for now
    #In following stages we will want the crawl other URLs and download all the pdfs
    #I've tried to leave the LinkExtractor() empty, but it doesn't work...
    rules = (
        Rule(
            LinkExtractor(
                allow=r'deeplink%3Adetalle_licitacion'
            ),
            callback='parse_item',
            follow=False,
        ),
    )

    def parse_item(self, response):
        #Debuggin
        #print('Hello crawl')
        #print("Response status:", response.status)
        #print("Response URL:", response.url)

        item = ItemLoader(item=claselicitacion(), response=response)

        #I'm using the id='filaX_coumna2' to find the information I want
        #I have to be sure that this format is the same in all the URLs, probably not
        #For now, let's continue like this
        item.add_xpath('organo_contratacion',
                       '//li[@id="fila2_columna2"]//span[@class="outputText"]/text()')
        
        item.add_xpath('estado_licitacion',
                       '//li[@id="fila3_columna2"]//span[@class="outputText"]/text()')
        
        item.add_xpath('objeto_contrato',
                       '//li[@id="fila4_columna2"]//span[@class="outputText"]/text()')
        
        item.add_xpath('presupuesto_base',
                       '//li[@id="fila5_columna2"]//span[@class="outputText"]/text()')
        
        item.add_xpath('tipo_contrato',
                       '//li[@id="fila7_columna2"]//span[@class="outputText"]/text()')
        
        item.add_xpath('codigo_cpv',
                       '//li[@id="fila8_columna2"]//span[@class="outputText"]/text()')
        
        item.add_xpath('ubicacion',
                       '//li[@id="fila9_columna2"]//span[@class="outputText"]/text()')

        item.add_xpath('fecha',
                       '//li[@id="fila12_columna2"]//span[@class="outputText"]/text()')
        
        item.add_value('url', response.url)


        yield item.load_item()

#TERMINAL EXECUTION
#scrapy runspider ProjectFinder.py