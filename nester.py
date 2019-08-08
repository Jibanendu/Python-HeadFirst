
''' The purpose of the function is to do a recursive loop 
within a list and to read all the values inside a list
'''
def print_values(movies):
    for movie in movies:
        if isinstance(movie,list):
            print_values(movie)
        else:
            print(movie)