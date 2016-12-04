"""Headlines project from 'Flask by Example'
"""
import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc' : 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn' : 'http://rss.cnn.com/rss/edition.rss',
             'seattle' : 'http://www.thestranger.com/seattle/Rss.xml'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
    """pull the articles from RSS
    """
    feed = feedparser.parse(RSS_FEEDS[publication])
    return render_template("home.html", articles=feed['entries'])

if __name__ == "__main__":
    app.run(port=5000, debug=True)
