############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, name, is_bestseller=False, 
                 ):
        """Initialize a melon."""

        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk','1998','green',True,'Muskmelon',True)
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas','2003','orange',False,'Casaba')
    casaba.add_pairing('strawberry')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)
    
    crenshaw = MelonType('cren','1996','green',True,'Crenshaw',False)
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)
    
    yellow_watermelon = MelonType('yw','2013','yellow',False,'Yellow Watermelon',True)
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)
    
    # print(casaba.pairings)
    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for paring in melon.pairings:
            print(f'-{paring}')
        #keep looping until length of index reaches the end

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_dict = {}

    for melon in melon_types:
        melon_dict[melon.code] = melon.name

    print(melon_dict)

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



