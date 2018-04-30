import media
import fresh_tomatoes
hunger_games= media.Movie("hunger_games","game of hunger","https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg","https://youtu.be/FovFG3N_RSU")

avengers =media.Movie("avengers", "super heros movie", "https://www.studentproblems.com/wp-content/uploads/2018/04/avengers-infinity-war.jpg","https://youtu.be/QwievZ1Tx-8")

wonder_woman=media.Movie("wonder woman","super hero woman","https://upload.wikimedia.org/wikipedia/en/e/ed/Wonder_Woman_%282017_film%29.jpg","https://youtu.be/1Q8fG0TtVAY")

black_panther = media.Movie("black panther", "Black American actin super hero movie", "https://vignette.wikia.nocookie.net/marvelcinematicuniverse/images/3/36/Black_Panther_Poster.jpg/revision/latest?cb=20171207153752", "https://youtu.be/xjDjIWPwcPU")
acrimony=media.Movie("Tyler Perry's Acrimony", "Psychological thriller movie", "https://upload.wikimedia.org/wikipedia/en/9/9b/TylerPerrysAcrimonyTeaserPoster.jpg", "https://www.youtube.com/watch?v=wlpunOUxYSo")

proud_mary=media.Movie("proud mary", "Thriller", "http://www.impawards.com/2018/posters/proud_mary.jpg", "https://www.youtube.com/watch?v=FWQcAgQxiRI" )




movies=[hunger_games,avengers, wonder_woman, black_panther,acrimony,proud_mary]


#fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.Valid_Ratings)
print(media.Movie.__doc__)