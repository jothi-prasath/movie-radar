import requests
from flask import Flask, render_template

app = Flask(__name__)

# TMDB API key
API_KEY = ''

URL = f'https://api.themoviedb.org/3/movie/now_playing'

params = {
    'api_key': API_KEY,
    'with_original_language': 'ta',  # Tamil language
}

@app.route('/')
def index():
    try:
        response = requests.get(URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            #print(data)
            now_playing_movies = data['results']
            
            movie_data = []
            for movie in now_playing_movies:
                movie_details = {
                    'title': movie['title'],
                    'release_date': movie['release_date'],
                    'overview': movie['overview'],
                    'poster_url': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}",
                }
                movie_data.append(movie_details)
            
            return render_template('index.html', movies=movie_data)
        else:
            return f"Unable to fetch data from TMDB. Status code: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
