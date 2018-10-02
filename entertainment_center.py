import fresh_tomatoes
import media

#Instances are created of class Movie
toy_story = media.Movie("toystory" , "A story of boy and toy that come to it's life." , "https://s-media-cache-ak0.pinimg.com/originals/8e/bd/48/8ebd48f66f760c1066bb7f82204d8866.jpg" , "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar" , "A marine on an alien planet." , "https://media-cache.cinematerial.com/p/500x/kytw5i6k/avatar-movie-poster.jpg" , "https://www.youtube.com/watch?v=5PSNL1qE6VY")

twilight = media.Movie("Twilight","A story based on vampires","http://myhollywooddream.com/wp-content/uploads/2008/10/twilightposters.jpg","https://www.youtube.com/watch?v=QDRLSqm_WVg")

padmaavat = media.Movie("Padmaavati","A fight of Rajput king and his wife Padmaavati vs Allaudin khilji. ","https://shyfyy.files.wordpress.com/2018/01/padmaavat-1.jpg","https://www.youtube.com/watch?v=X_5_BLt76c0")

padman = media.Movie("Padman","Man sets out to create a sanitary pad machine and to provide inexpensive sanitary pads to the women of rural India.","https://static.toiimg.com/photo/61816142.cms","https://www.youtube.com/watch?v=-K9ujx8vO_A")

raees = media.Movie("Raees","A bootlegger sets out to improve his community as a promising leader but falls in a political trap.","http://www.indicine.com/img/2016/12/Raees-New-Poster-1.jpg","https://www.youtube.com/watch?v=J7_1MU3gDk0")

movies =[toy_story , avatar , twilight , padmaavat , padman , raees]


fresh_tomatoes.open_movies_page(movies)


