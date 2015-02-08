"""Import require modules. Them media module which
enables calls to be made to its Movie Class making
it possible to create instances of the Movie class.

The fresh_tomatoes module enables a function called
'open_movies_page' to be called.
"""
import media
import fresh_tomatoes


__author__ = "Hamza Yahaya"
__date__ = "10 February 2015"
__credits__ = """Thanks to the awesome teaching team at Udacity"""



#instances of Movie class and their attributes
focus = media.Movie("Focus",
                    "A story about a con man falling in love",
                    "https://upload.wikimedia.org/wikipedia/en/b/bf/2015_Focus_film_poster.png",
                    "https://www.youtube.com/watch?v=6vY9UPiI4eQ")
    
mad_max = media.Movie("Mad Max: Fury Road",
                      "A post-apocalyptic action film",
                      "https://upload.wikimedia.org/wikipedia/en/f/fb/Mad_Max_Fury_Road_poster.jpg",
                      "https://www.youtube.com/watch?v=b_4nzm9ICuo")

entourage = media.Movie("Entourage",
                         "Four friends living the American dream in L.A",
                         "https://upload.wikimedia.org/wikipedia/en/d/df/Entourage_film_2015_poster.jpg",
                         "https://www.youtube.com/watch?v=Vz2HyCgUWh4")

age_of_Ultron = media.Movie("Age of Ultron",
                            "A  superhero film based on the Marvel Comics superhero team the Avengers",
                            "https://upload.wikimedia.org/wikipedia/en/1/1b/Avengers_Age_of_Ultron.jpg",
                            "https://www.youtube.com/watch?v=MZoO8QVMxkk")

ps_i_loveu = media.Movie("P.S I Love You",
                     "A story about Lost Love",
                     "http://upload.wikimedia.org/wikipedia/en/7/7f/PS_I_Love_You_%28film%29.jpg",
                     "http://www.youtube.com/watch?v=CZzW6_hR068")

about_time = media.Movie("About Time",
                     "A story about Love and Time Travel",
                     "http://upload.wikimedia.org/wikipedia/en/8/88/About_Time_Poster.jpg",
                     "http://www.youtube.com/watch?v=T7A810duHvw")

perks_wall_flower = media.Movie("The Perks of Being A Wall Flower",
                     "A story about a high school kid",
                     "http://upload.wikimedia.org/wikipedia/en/0/0b/The_Perks_of_Being_a_Wallflower_Poster.jpg",
                     "https://www.youtube.com/watch?v=rJmzrYyppkc")

what_if = media.Movie("What If",
                      "A  romantic comedy film about a boy miserable job and lives with his sister and nephew",
                      "https://upload.wikimedia.org/wikipedia/en/d/d4/The_F_Word_theatrical_poster.png",
                      "https://www.youtube.com/watch?v=A86JGbBEaBk")


like_crazy = media.Movie("Like Crazy",
                     "Love, Hearbreaks & Makeup",
                     "http://upload.wikimedia.org/wikipedia/en/1/19/Like_Crazy.jpg",
                     "http://www.youtube.com/watch?v=r-ZV-bwZmBw")

terminator_genisys = media.Movie("Terminator Genisys",
                                 "Man Against Machine",
                                 "https://upload.wikimedia.org/wikipedia/en/f/fb/Terminator_Genisys_poster.jpg",
                                 "https://www.youtube.com/watch?v=N4zhBQfqVCc")

five_to_seven = media.Movie("5 to 7",
                            "An aspiring novelist has an extramarital affair with a French diplomat's wife",
                            "http://www.movie-list.com/img/posters/big/5to7.jpg",
                            "https://www.youtube.com/watch?v=9HimzZ6QG2o")

furious_seven = media.Movie("Furious 7",
                            "Sequel to the 2013 film Fast & Furious 6 and the seventh installment in the Fast & Furious film series.",
                            "https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",
                            "https://www.youtube.com/watch?v=yISKeT6sDOg")



#a list containing the isntances(movies) of the class Movie                      
movies = [furious_seven,what_if, like_crazy,terminator_genisys, five_to_seven, focus,
          mad_max, entourage, age_of_Ultron, ps_i_loveu, about_time, perks_wall_flower]

# A function that takes in one argument,the of movies and creates an HTML file which displays all the movies.
fresh_tomatoes.open_movies_page(movies)




