#inheritacne is where we can define a lot of functins and attributtes
#it allows you to inherit from an existing class to use all the properties
from chef import Chef
from ghanaian_chef import Ghanaian_Chef


myChef = Chef()
myChef.make_a_special_dish()


myGhanaian_Chef = Ghanaian_Chef()
myGhanaian_Chef.make_a_special_dish()
