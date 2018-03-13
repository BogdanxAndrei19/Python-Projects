import fresh_tomatoes
import media


toyStory = media.Movie("Toy Story","A story of a boy and his toys",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

##print(toyStory.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

##print (avatar.storyline)
##avatar.show_trailer()

shawshank = media.Movie("The Shawshank Redemption",
                        "A touching story of 2 two prisoners who become friends",
                        "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=6hB3S9bIaco")

##print (shawshank.storyline)
##shawshank.show_trailer()

movies = [toyStory, avatar, shawshank]
fresh_tomatoes.open_movies_page(movies)
                     
