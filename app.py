import json
import requests
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

############################
### Lab Part 1: JSON 
############################

@app.route('/movie')
def movies():
    json_string = """
                    {
                    "title" : "Black Panther", 
                    "releaseDate" : "2/16/2018",
                    "image_url": "https://ksassets.timeincuk.net/wp/uploads/sites/55/2018/02/KXC1W2-920x584.jpg"
                    }
                    """
    parsed_json = json.loads(json_string)
    return render_template('movie.html', movie=parsed_json)


@app.route('/tvshows')
def tv_shows():
    json_string1 = """
    [{
    "url":"http://www.tvmaze.com/shows/2705/narcos",
    "name":"Narcos",
    "language":"English",
    "genres":[  
      "Drama",
      "Crime"
    ]}
    
    {"url":"http://www.tvmaze.com/shows/305/black-mirror",
    "name":"Black Mirror",
    "language":"English",
    "genres":[  
        "Drama",
        "Science-Fiction",
        "Thriller"
   ]},
   "url":"http://www.tvmaze.com/shows/305/black-mirror",
   "name":"Black Mirror",
    "type":"Scripted",
    "language":"English",
    "genres":[  
        "Drama",
        "Science-Fiction",
        "Thriller"
    ]
    }]
    """
    # Write code here to take the `json_string` and return list of movies to the user

    parsed_json1 = json.loads(json_string1)
    return render_template('tv_shows.html', tvshows=parsed_json1)


############################
### Lab Part 2: API requests
############################
@app.route('/dogs')
def dog_breeds():
    
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    
    parsed_content = json.loads(response.content)
    dog_list = parsed_content["message"]

    print("dog_list")
    return render_template('dogs.html', dogs=dog_list)

    return render_template('dogs.html')

if __name__ == '__main__':
    app.run(debug=True)