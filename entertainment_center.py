import fresh_tomatoes
import media

# List having all movie details.

movies_list = [
  {
    'title': "Toy Story",
    'storyline': "A story of boy and toy that come to it's life.",
    'poster_url': "https://s-media-cache-ak0.pinimg.com/originals/"
                  "8e/bd/48/8ebd48f66f760c1066bb7f82204d8866.jpg",
    'trailer_url': "https://www.youtube.com/watch?v=KYz2wyBy3kc"
  },
  {
    'title': "Avatar",
    'storyline': "A marine on an alien planet.",
    'poster_url': "https://media-cache.cinematerial.com/p/500x/"
                  "kytw5i6k/avatar-movie-poster.jpg",
    'trailer_url': "https://www.youtube.com/watch?v=5PSNL1qE6VY"
  },
  {
    'title': "Twilight",
    'storyline': "A story based on vampires",
    'poster_url': "http://myhollywooddream.com/wp-content/uploads/"
                  "2008/10/twilightposters.jpg",
    'trailer_url': "https://www.youtube.com/watch?v=QDRLSqm_WVg",
  },
  {
    'title': "Padmaavati",
    'storyline': "A fight of Rajput king and his wife"
                 " Padmaavati vs Allaudin khilji. ",
    'poster_url': "https://shyfyy.files.wordpress.com/2018/01/padmaavat-1.jpg",
    'trailer_url': "https://www.youtube.com/watch?v=X_5_BLt76c0"
  },
  {
    'title': "Padman",
    'storyline': "Man sets out to create a sanitary pad machine and to provide"
                 " inexpensive sanitary pads to the women of rural India.",
    'poster_url': "https://static.toiimg.com/photo/61816142.cms",
    'trailer_url': "https://www.youtube.com/watch?v=-K9ujx8vO_A"
  },
  {
    'title': "Raees",
    'storyline': "A bootlegger sets out to improve his community as "
                 " a promising leader but falls in a political trap.",
    'poster_url': "http://www.indicine.com/img/2016/12/Raees-New-Poster-1.jpg",
    'trailer_url': "https://www.youtube.com/watch?v=J7_1MU3gDk0"
  }
]

movies = []


def add_movies():
    '''
    Add movies dynamically to movies list
    Args: None
    Returns: movies array with each passed media_item
    '''
    for item in movies_list:
        # Add each item of movies_list to instance of movie class
        media_item = media.Movie(
            item['title'],
            item['storyline'],
            item['poster_url'],
            item['trailer_url'])
        movies.append(media_item)
add_movies()

fresh_tomatoes.open_movies_page(movies)
