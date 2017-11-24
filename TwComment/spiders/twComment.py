#TwComment

from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
import logging
import json
from scrapy.conf import settings
from scrapy import http
from TwComment.items import Comment
import scrapy

class TwComment(CrawlSpider):
    name = 'TwComment'
    #the name of the spider

    def start_requests(self):
        #实时新闻
        #urls = ['https://twitter.com', 'https://twitter.com/i/streams/category/686639666771046402', 'https://twitter.com/i/streams/category/686639666779394057', 'https://twitter.com/i/streams/category/686639666779426835', 'https://twitter.com/i/streams/category/686639666779394055', 'https://twitter.com/i/streams/category/686639666779426842', 'https://twitter.com/i/streams/category/686639666779426845', 'https://twitter.com/i/streams/category/686639666779394072', 'https://twitter.com/i/streams/category/690675490684678145', 'https://twitter.com/i/streams/category/692079932940259328', 'https://twitter.com/i/streams/category/788602775839965184', 'https://twitter.com/i/streams/category/841388582518562816', 'https://twitter.com/i/streams/category/841390443338309632']
        
        #13个实时
        #urls = ['https://twitter.com', 'https://twitter.com/i/streams/category/686639666771046402',]
        #urls = ['https://twitter.com/i/streams/category/686639666779394057', 'https://twitter.com/i/streams/category/686639666779426835',]
        #urls = ['https://twitter.com/i/streams/category/686639666779394055', 'https://twitter.com/i/streams/category/686639666779426842',]
        #urls = ['https://twitter.com/i/streams/category/686639666779426845', 'https://twitter.com/i/streams/category/686639666779394072']
        #urls = ['https://twitter.com/i/streams/category/690675490684678145', 'https://twitter.com/i/streams/category/692079932940259328']
        #urls = ['https://twitter.com/i/streams/category/788602775839965184', 'https://twitter.com/i/streams/category/841388582518562816']
        #urls = ['https://twitter.com/i/streams/category/841390443338309632']
        

#88 个名人
        #urls = ['https://twitter.com/BarackObama', 'https://twitter.com/BillClinton']
        #urls = ['https://twitter.com/HillaryClinton','https://twitter.com/FLOTUS']
        #urls = ['https://twitter.com/mike_pence','https://twitter.com/KellyannePolls']
        #urls = ['https://twitter.com/MichelleObama','https://twitter.com/Pontifex']
        #urls = ['https://twitter.com/Queen_Europe','https://twitter.com/BillGates']
        #urls = ['https://twitter.com/David_Cameron','https://twitter.com/JeffBezos']
        urls = ['https://twitter.com/narendramodi','https://twitter.com/Cristiano']
        #urls = ['https://twitter.com/KingJames','https://twitter.com/rogerfederer']
        #urls = ['https://twitter.com/neymarjr','https://twitter.com/RafaelNadal']
        #urls = ['https://twitter.com/StephenCurry30','https://twitter.com/DjokerNole']
        #urls = ['https://twitter.com/RondaRousey','https://twitter.com/serenawilliams']
        #urls = ['https://twitter.com/MariaSharapova','https://twitter.com/TheNotoriousMMA']
        #urls = ['https://twitter.com/kobebryant','https://twitter.com/KDTrey5']
        #urls = ['https://twitter.com/FloydMayweather','https://twitter.com/GalGadot']
        #urls = ['https://twitter.com/EmmaWatson','https://twitter.com/lizasoberano']
        #urls = ['https://twitter.com/NargisFakhri','https://twitter.com/russellcrowe']
        #urls = ['https://twitter.com/McConaughey','https://twitter.com/LeoDiCaprio']
        #urls = ['https://twitter.com/realdepp','https://twitter.com/RobertDowneyJr']
        #urls = ['https://twitter.com/TomCruise','https://twitter.com/justinbieber']
        #urls = ['https://twitter.com/khloekardashian','https://twitter.com/kourtneykardash']
        #urls = ['https://twitter.com/KendallJenner','https://twitter.com/nytimes']
        #urls = ['https://twitter.com/cnnbrk','https://twitter.com/BBCBreaking']
        #urls = ['https://twitter.com/Google','https://twitter.com/FoxNews']
        #urls = ['https://twitter.com/WhiteHouse','https://twitter.com/ABC']
        #urls = ['https://twitter.com/ImRaina','https://twitter.com/BreakingNews']
        #urls = ['https://twitter.com/gmail','https://twitter.com/Aly_Raisman']
        #urls = ['https://twitter.com/JohnWall','https://twitter.com/JHarden13']
        #urls = ['https://twitter.com/espn','https://twitter.com/CNN']
        #urls = ['https://twitter.com/NBA','https://twitter.com/GameOfThrones']
        #urls = ['https://twitter.com/SamuelLJackson','https://twitter.com/AntDavis23']
        #urls = ['https://twitter.com/jtimberlake','https://twitter.com/tomhanks']
        #urls = ['https://twitter.com/mark_wahlberg','https://twitter.com/danielwuyanzu']
        #urls = ['https://twitter.com/TheLewisTan','https://twitter.com/adamcarolla']
        #urls = ['https://twitter.com/KyrieIrving','https://twitter.com/NiallOfficial']
        #urls = ['https://twitter.com/chelseahandler','https://twitter.com/twhiddleston']
        #urls = ['https://twitter.com/taylorswift13','https://twitter.com/chrishemsworth']
        #urls = ['https://twitter.com/MarvelStudios','https://twitter.com/Schwarzenegger']
        #urls = ['https://twitter.com/JimCameron','https://twitter.com/TheRock']
        #urls = ['https://twitter.com/OfficialKat', 'https://twitter.com/SophieT']
        #urls = ['https://twitter.com/Maisie_Williams','https://twitter.com/susmitchakrabo1']
        #urls = ['https://twitter.com/ladygaga','https://twitter.com/katyperry']
        #urls = ['https://twitter.com/KimKardashian','https://twitter.com/aplusk']
        #urls = ['https://twitter.com/rihanna','https://twitter.com/justdemi']
        #urls = ['https://twitter.com/rustyrockets','https://twitter.com/MileyCyrus']
        
    
        #名人twitter， 爬过
        #urls = ['https://twitter.com/BarackObama', 'https://twitter.com/BillClinton','https://twitter.com/HillaryClinton','https://twitter.com/FLOTUS','https://twitter.com/mike_pence','https://twitter.com/KellyannePolls','https://twitter.com/MichelleObama','https://twitter.com/Pontifex','https://twitter.com/Queen_Europe','https://twitter.com/BillGates','https://twitter.com/David_Cameron','https://twitter.com/JeffBezos','https://twitter.com/narendramodi','https://twitter.com/Cristiano','https://twitter.com/KingJames','https://twitter.com/rogerfederer','https://twitter.com/neymarjr','https://twitter.com/RafaelNadal','https://twitter.com/StephenCurry30','https://twitter.com/DjokerNole','https://twitter.com/RondaRousey','https://twitter.com/serenawilliams','https://twitter.com/MariaSharapova','https://twitter.com/TheNotoriousMMA','https://twitter.com/kobebryant','https://twitter.com/KDTrey5','https://twitter.com/FloydMayweather','https://twitter.com/GalGadot','https://twitter.com/EmmaWatson','https://twitter.com/lizasoberano','https://twitter.com/NargisFakhri','https://twitter.com/russellcrowe','https://twitter.com/McConaughey','https://twitter.com/LeoDiCaprio','https://twitter.com/realdepp','https://twitter.com/RobertDowneyJr','https://twitter.com/TomCruise','https://twitter.com/justinbieber','https://twitter.com/khloekardashian','https://twitter.com/kourtneykardash','https://twitter.com/KendallJenner','https://twitter.com/nytimes','https://twitter.com/cnnbrk','https://twitter.com/BBCBreaking','https://twitter.com/Google','https://twitter.com/FoxNews','https://twitter.com/WhiteHouse','https://twitter.com/ABC','https://twitter.com/ImRaina','https://twitter.com/BreakingNews','https://twitter.com/gmail','https://twitter.com/Aly_Raisman','https://twitter.com/JohnWall','https://twitter.com/JHarden13','https://twitter.com/espn','https://twitter.com/CNN','https://twitter.com/NBA','https://twitter.com/GameOfThrones','https://twitter.com/SamuelLJackson','https://twitter.com/AntDavis23','https://twitter.com/jtimberlake','https://twitter.com/tomhanks','https://twitter.com/mark_wahlberg','https://twitter.com/danielwuyanzu','https://twitter.com/TheLewisTan','https://twitter.com/adamcarolla','https://twitter.com/KyrieIrving','https://twitter.com/NiallOfficial','https://twitter.com/chelseahandler','https://twitter.com/twhiddleston','https://twitter.com/taylorswift13','https://twitter.com/chrishemsworth','https://twitter.com/MarvelStudios','https://twitter.com/Schwarzenegger','https://twitter.com/JimCameron','https://twitter.com/TheRock','https://twitter.com/OfficialKat', 'https://twitter.com/SophieT','https://twitter.com/Maisie_Williams','https://twitter.com/susmitchakrabo1','https://twitter.com/ladygaga','https://twitter.com/katyperry','https://twitter.com/KimKardashian','https://twitter.com/aplusk','https://twitter.com/rihanna','https://twitter.com/justdemi','https://twitter.com/rustyrockets','https://twitter.com/MileyCyrus']
        
        for url in urls:
            yield http.Request(url, callback=self.parse_page)
    

    def parse_page(self, response):
        items = response.xpath('//div[@class="js-tweet-text-container"]/p[@lang=\"en\"]/img[@class=\'Emoji Emoji--forText\']')
        for item in self.parse_tweet_item(items):
            yield item
        
        #next_page_id = response.xpath('//div[@data-permalink-path]').xpath('attribute::data-permalink-path').extract()
        next_page_id = response.xpath('//div[@class="js-tweet-text-container"]/p[@lang=\"en\"]/a[@class=\"twitter-atreply pretty-link js-nav\"]').xpath('attribute::href').extract()
        
        for item in next_page_id:
            next_page = "https://twitter.com" + ''.join(item)
            yield response.follow(next_page, self.parse_page)

    def parse_tweet_item(self, items):
        for item in items:
            #try:
                comment = Comment()

                comment['content'] = item.xpath('ancestor::p/text()').extract()[0]
                comment['image'] = item.xpath('attribute::alt').extract()[0]
                comment['title'] = item.xpath('attribute::title').extract()[0]
                
                if comment['content'] == '':
                    # If there is not text, we ignore the comment
                    continue
                yield comment
                #except:
#logger.error("Error comment:\n%s" % item.xpath('.').extract()[0])




            












