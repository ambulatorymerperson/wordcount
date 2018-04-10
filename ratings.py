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

    all_restaurants = sorted(all_restaurants)    
    for restaurant in all_restaurants:
        restaurants_and_ratings[restaurant[0]] = restaurant[1] 


    for restaurant in restaurants_and_ratings:
        value = restaurants_and_ratings[restaurant]

        print "{} is rated at {}.".format(restaurant, value)

 
restaurant_rating_organizer("scores.txt")