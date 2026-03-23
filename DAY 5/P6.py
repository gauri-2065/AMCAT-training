# variable length argument / variable number of arguments
def cityName(*city):
    print("City Name: ",city)

cityName("Mumbai","Nagpur","Pune","Mumbai")


#*city accepts arguments as a tuple.