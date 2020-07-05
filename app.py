from flask import Flask, render_template
from newsapi import NewsApiClient
from flask_bootstrap import Bootstrap

app = Flask(__name__,instance_relative_config = True)



# Initializing Flask Extensions
bootstrap = Bootstrap(app)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key = 'b3fefd9be43745ce806ac142643aca1e')
    topheadlines = newsapi.get_top_headlines(sources = 'abc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    
    mylist = zip(news, desc, img)

    return render_template('index.html', context = mylist)

@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key = 'b3fefd9be43745ce806ac142643aca1e')
    topheadlines = newsapi.get_top_headlines(sources = 'bbc-news')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    
    mylist = zip(news, desc, img)

    return render_template('bbc.html', context = mylist)

@app.route('/abc')
def abc():
    newsapi = NewsApiClient(api_key = 'b3fefd9be43745ce806ac142643aca1e')
    topheadlines = newsapi.get_top_headlines(sources = 'abc-news-au')

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    
    mylist = zip(news, desc, img)

    return render_template('abc.html', context = mylist)

if __name__ == "__main__":
    app.run(debug = True)
 