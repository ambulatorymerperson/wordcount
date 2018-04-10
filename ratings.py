import sys

filename = sys.argv[1]

def restaurant_rating_organizer(filename):
    """Restaurant rating lister."""
    #reads the ratings in from file(scores.txt)
    filename = open(filename)
    restaurants_and_ratings = {}
    all_restaurants = []

    for line in filename:
        line = line.rstrip()
        name_rating = line.split(":")
        all_restaurants.append(name_rating)


    for restaurant, rating in all_restaurants:
        restaurants_and_ratings[restaurant] = rating 


    # for restaurant in sorted(restaurants_and_ratings):
    #     value = restaurants_and_ratings[restaurant]

    #     print "{} is rated at {}.".format(restaurant, value)

    for restaurant, rating in sorted(restaurants_and_ratings.items()):
        print "{} is rated at {}.".format(restaurant, rating)

 
restaurant_rating_organizer(filename)