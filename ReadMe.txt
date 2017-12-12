ScrapyCrawl program
crawl comments with emoji only from twitter pages

File Explanation: 
twComment.py (/TwComment/spiders/twComment.py) is the crawl file
	TwComment is the name of this spider
	urls are the starting website
	output: results.json 
		format: 
			content: comment
			image: emoji image
			title: emoji title

select_data.py uses for select data and remove duplicate item(same content and same emoji)
	input: results.json
	output: newUniData.json

Run: 
Open one of url block or type a new url
Under file directory, run "scrapy crawl TwComment"

