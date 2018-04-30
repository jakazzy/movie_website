import webbrowser
class Movie():
	"""This provides a way to save info about movies"""
	Valid_Ratings=["G","PG", "PG-13","R"]

	def __init__(self,movie_title,movie_story,poster_image,trailer_youtube_url):
		self.title=movie_title
		self.story_line=movie_story
		self.poster_image_url=poster_image
		self.trailer_youtube_url=trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

# if __name__=="__main__":
# 	avatar = Movie("avatar","the movie of avatar","poster image","poster url")
# 	print(avatar.movie_story)