import requests
from bs4 import BeautifulSoup as soup

def get_contenet_string(url):
    page=requests.get(url)
    page_soup=soup(page.content,'html.parser')
    #print(page_soup)
    containers=page_soup.find_all("script",{"type":"application/ld+json"})
    article_list=[]
    print(containers)
    for container in containers:
        for dictionary in container:
            article_list.append(dictionary)
    print(article_list)
    article_list[0:2]=[''.join(article_list[0:2])]
    content_string=article_list[0]
    print(content_string)
    article_index=content_string.index("itemListElement")
    content_string=content_string[article_index+18:]
    return content_string



def find_occurences(content_string):
    star_indices=[]
    end_indices=[]
    for i in range(len(content_string)):
        if content_string.startswith("https://www.nytimes.com/2021",i):
            star_indices.append(i)
        if content_string.startswith(".html",i):
            end_indices.append(i+5)
    print(star_indices)
    print(end_indices)

    #end_indices.remove(end_indices[4])
    #end_indices.remove(end_indices[5])
    return star_indices,end_indices


def get_all_urls(star_indices,end_indices,content_string):
    url_list=[]
    for i in range(len(star_indices)):
        url_list.append(content_string[star_indices[i]:end_indices[i]])
    return url_list

content_string=get_contenet_string("https://www.nytimes.com/international/section/technology")
start_indices,end_indices=find_occurences(content_string)


url_list=get_all_urls(start_indices,end_indices,content_string)
print(url_list)