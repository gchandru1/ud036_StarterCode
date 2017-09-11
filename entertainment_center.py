import fresh_tomatoes
import media

#Creating instances of class media for each movie in Phase 1 of the MCU

#IronMan1
im = media.Movie("Iron Man",
                 "After being held captive in an Afghan cave, billionaire engineer Tony Stark creates a unique weaponized suit of armor to fight evil.",
                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNTI2ODUwOF5BMl5BanBnXkFtZTcwMTU0NTIzMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                 "https://www.youtube.com/watch?v=bK_Y5LjSJ-Y")

#TheIncredibleHulk
tih = media.Movie("The Incredible Hulk",
                  "Bruce Banner, a scientist on the run from the U.S. Government, must find a cure for the monster he turns into, whenever he loses his temper.",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUyNzk3MjA1OF5BMl5BanBnXkFtZTcwMTE1Njg2MQ@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                  "https://www.youtube.com/watch?v=xbqNb2PFKKA")

#IronMan2
im2 = media.Movie("Iron Man 2",
                  "With the world now aware of his identity as Iron Man, Tony Stark must contend with both his declining health and a vengeful mad man with ties to his father's legacy.",
                  "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM0MDgwNjMyMl5BMl5BanBnXkFtZTcwNTg3NzAzMw@@._V1_.jpg",
                  "https://www.youtube.com/watch?v=BoohRoVA9WQ")

#Thor
thor = media.Movie("Thor",
                   "The powerful but arrogant god Thor is cast out of Asgard to live amongst humans in Midgard (Earth), where he soon becomes one of their finest defenders.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BOGE4NzU1YTAtNzA3Mi00ZTA2LTg2YmYtMDJmMThiMjlkYjg2XkEyXkFqcGdeQXVyNTgzMDMzMTg@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=YSC9CjSYvYA")

#CaptainAmerica
ca_tfa = media.Movie("Captain America: The First Avenger",
                     "Steve Rogers, a rejected military soldier transforms into Captain America after taking a dose of a 'Super-Soldier serum'. But being Captain America comes at a price as he attempts to take down a war monger and a terrorist organization.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYzOTc2NzU3N15BMl5BanBnXkFtZTcwNjY3MDE3NQ@@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=JerVrbLldXw")

#Avengers
avengers = media.Movie("Marvel's The Avengers",
                       "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

#Creating list of instances
movies = [im, tih, im2, thor, ca_tfa, avengers]
fresh_tomatoes.open_movies_page(movies)
