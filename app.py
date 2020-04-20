from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr10/anigif_enhanced-29828-1403646582-7.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr06/anigif_enhanced-28244-1403646370-2.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr10/anigif_enhanced-29510-1403646649-3.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr10/anigif_enhanced-30034-1403646599-7.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr09/anigif_enhanced-4743-1403646817-9.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr08/anigif_enhanced-23675-1403646767-8.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr10/anigif_enhanced-29994-1403646740-39.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr08/anigif_enhanced-23704-1403646787-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/18/enhanced/webdr02/anigif_enhanced-10067-1403647307-22.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/18/enhanced/webdr06/anigif_enhanced-28044-1403647272-11.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/18/enhanced/webdr09/anigif_enhanced-4685-1403647551-18.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/18/enhanced/webdr02/anigif_enhanced-24306-1403647326-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/18/enhanced/webdr07/anigif_enhanced-3756-1403647724-4.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr09/anigif_enhanced-4743-1403646233-1.gif",
    "https://img.buzzfeed.com/buzzfeed-static/static/2014-06/24/17/enhanced/webdr05/anigif_enhanced-2087-1403646837-1.gif"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
