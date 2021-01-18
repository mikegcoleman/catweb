from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images 
images = [
    "https://images.pexels.com/photos/730896/pexels-photo-730896.jpeg?cs=srgb&dl=pexels-snapwire-730896.jpg&fm=jpg",
    "https://images.pexels.com/photos/1741205/pexels-photo-1741205.jpeg?cs=srgb&dl=pexels-lina-kivaka-1741205.jpg&fm=jpg",
    "https://images.pexels.com/photos/1056251/pexels-photo-1056251.jpeg?cs=srgb&dl=pexels-ihsan-aditya-1056251.jpg&fm=jpg",
    "https://images.pexels.com/photos/2071873/pexels-photo-2071873.jpeg?cs=srgb&dl=pexels-wojciech-kumpicki-2071873.jpg&fm=jpg",
    "https://www.pexels.com/photo/adorable-angry-animal-animal-portrait-208984/",
    "https://images.pexels.com/photos/774731/pexels-photo-774731.jpeg?cs=srgb&dl=pexels-marko-blazevic-774731.jpg&fm=jpg",
    "https://images.pexels.com/photos/126407/pexels-photo-126407.jpeg?cs=srgb&dl=pexels-inge-wallumr%C3%B8d-126407.jpg&fm=jpg",
    "https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?cs=srgb&dl=pexels-wojciech-kumpicki-2071882.jpg&fm=jpg",
    "https://images.pexels.com/photos/2071881/pexels-photo-2071881.jpeg?cs=srgb&dl=pexels-wojciech-kumpicki-2071881.jpg&fm=jpg",
    "https://images.pexels.com/photos/821736/pexels-photo-821736.jpeg?cs=srgb&dl=pexels-alex-andrews-821736.jpg&fm=jpg",
    "https://images.pexels.com/photos/68594/pexels-photo-68594.jpeg?cs=srgb&dl=pexels-nihat-68594.jpg&fm=jpg",
    "https://images.pexels.com/photos/1576193/pexels-photo-1576193.jpeg?cs=srgb&dl=pexels-serena-koi-1576193.jpg&fm=jpg",
    "https://www.pexels.com/photo/closeup-up-photography-of-dragon-li-kitten-691583/",
    "https://images.pexels.com/photos/248280/pexels-photo-248280.jpeg?cs=srgb&dl=pexels-pixabay-248280.jpg&fm=jpg",
    "https://images.pexels.com/photos/804475/pexels-photo-804475.jpeg?cs=srgb&dl=pexels-bekka-mongeau-804475.jpg&fm=jpg"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
