from newspaper import Article,fulltext
import nltk
import requests
def summarize_article(url):
    article=Article(url)
    article.download()
    article.parse()
    #nltk.download('punkt')
    article.nlp()
    print("Authors:"+str(article.authors))
    date=article.publish_date
    print("publish date:"+str(date.strftime("%m/%d/%Y")))
    print("Top Image Url:"+str(article.top_image))

    image_string="All Images:"
    for image in article.images:
        image_string+="\n\t"+image
    print(image_string)

    print("A quick Article Summary")
    print("-------------------------")
    #print(article.summary)
    #print(article.text)
    return article.summary

summarize_article("https://www.nytimes.com/2021/06/17/technology/apple-china-doug-guthrie.html?searchResultPosition=2")
