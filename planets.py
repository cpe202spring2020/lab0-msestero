def weight_on_planets():
   # write your code here
   earth_weight = float(input("What do you weigh on earth? \n"))
   mars_weight = earth_weight * .38
   jupiter_weight = earth_weight * 2.34
   print("On Mars you would weigh", mars_weight, "pounds.\nOn Jupiter you would weigh", jupiter_weight, "pounds.")


if __name__ == '__main__':
   weight_on_planets()