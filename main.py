from news_nlp import *
from news_extract import *
from newspaper_scrape import *
import time

if __name__ == '__main__':
    print("Welcome to the newspaper scrape project")
    print("in seconds,you will have access to the latest technology articles in the new york times")
    print("In addition,you will also be able to knwo snetiment of the news")
    name=input("Enter your name to get started")
    print("welcome"+name+"!you will now see the latest technology articles in the new york times")
    print("Extracting article hyperlinks...")
    time.sleep(2)
    print("Retriving the Summaries:")
    print()
    time.sleep(2)

    content_string=get_contenet_string("https://www.nytimes.com/section/technology")
    start_indices,end_indices=find_occurences(content_string)
    url_list=get_all_urls(start_indices,end_indices,content_string)
    for url in url_list:
        print("Artical_url"+str(url))
        article_summary=summarize_article(url)
        find_sentiment(article_summary)
        print("-------------------")
        time.sleep(7)
    print()
    print("the articles are successfully extracted ")
    print("in total,we were able to extract"+str(len(url_list)))
    print("Thanks for participating ,"+name+"!")