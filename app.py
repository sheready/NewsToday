from flask import Flask, render_template
from newsapi import NewsApiClient
from flask_bootstrap import Bootstrap

app = Flask(__name__,instance_relative_config = True)



# Initializing Flask Extensions
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    newsapi = NewsApiClient(api_key = 'b3fefd9be43745ce806ac142643aca1e')
    topheadlines = newsapi.get_top_headlines(sources = 'mashable')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        url.append(myarticles['url'])

    
    mylist = zip(news, desc, img, date, url)

    return render_template('mashable.html', context = mylist)

@app.route('/techcrunch')
def bbc():
    newsapi = NewsApiClient(api_key = 'b3fefd9be43745ce806ac142643aca1e')
    topheadlines = newsapi.get_top_headlines(sources = 'techcrunch')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
    
    mylist = zip(news, desc, img, date, url)

    return render_template('techcrunch.html', context = mylist)

@app.route('/wired')
def abc():
    newsapi = NewsApiClient(api_key = 'b3fefd9be43745ce806ac142643aca1e')
    topheadlines = newsapi.get_top_headlines(sources = 'wired')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
    
    mylist = zip(news, desc, img, date, url)

    return render_template('wired.html', context = mylist)

@app.route('/headlines')
def head():
    newsapi = NewsApiClient(api_key = 'b3fefd9be43745ce806ac142643aca1e')
    topheadlines = newsapi.get_top_headlines(sources = 'cbs-news, cnn, the-wall-street-journal')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    date = []
    url = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        date.append(myarticles['publishedAt'])
        url.append(myarticles['url'])
    
    mylist = zip(news, desc, img, date, url)

    return render_template('index.html', context = mylist)

if __name__ == "__main__":
    app.run(debug = True)
 