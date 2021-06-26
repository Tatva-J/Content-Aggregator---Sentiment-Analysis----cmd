from textblob import TextBlob

def find_sentiment(text):
    news=TextBlob(text)
    sentiments=[]
    for sentences in news.sentences:
        sentiment=sentences.sentiment
        for metric in sentiment:
            sentiments.append(metric)
    print(sentiments)
    polarity_data=[]
    subjectivity_data=[]
    for i in range(len(sentiments)):
        if i%2==0:
            polarity_data.append(sentiments[i])
        else:
            subjectivity_data.append(sentiments[i])
    print(polarity_data)
    print(subjectivity_data)
    polarity_average=calculate_average(polarity_data)
    subjectivity_average=calculate_average(subjectivity_data)
    print(polarity_average)
    print(subjectivity_average)
    print("final analysis")
    print("-----------------")
    print("Polarity:"+calculate_sentiment(polarity_average,"polarity"))
    print("Subjective:"+calculate_sentiment(subjectivity_average,"subjectivity"))
def calculate_average(list):
    return sum(list)/len(list)
def calculate_sentiment(sentiment,type):
    sentiment_Category=""
    if type=="polarity":
        if sentiment>0.75:
            sentiment_Category="Extremely Postive"
        elif sentiment>0.5:
            sentiment_Category="Significanlty Postive"
        elif sentiment>0.3:
            sentiment_Category="Fairly Postive"
        elif sentiment>0.1:
            sentiment_Category="Slighlty Postive"
        elif sentiment>-0.1:
            sentiment_Category="Slighlty Negative"
        elif sentiment>-0.3:
            sentiment_Category="Fairly Negative"
        elif sentiment>-0.5:
            sentiment_Category="Significantly Negative"
        elif sentiment>-0.75:
            sentiment_Category="Extremely Negative"
        else:
            sentiment_Category="Neutral"
        return sentiment_Category
    elif type=="subjectivity":
        if sentiment > 0.75:
            sentiment_Category = "Extremely Subjective"
        elif sentiment > 0.5:
            sentiment_Category = "Fairly Subjective"
        elif sentiment > 0.3:
            sentiment_Category = "Fairly objective"
        elif sentiment > 0.1:
            sentiment_Category = "Extremely objective"
        return sentiment_Category
    else:
        print("Invalid Input")
text="That can spell disaster for small businesses. Downtime can cost up to $8,600 an hour, with the average amount of downtime totaling around seven hours. Being hit with ransomware is more than just a nuisance. If left unsolved for too long, it can cripple your business completely."
find_sentiment(text)
