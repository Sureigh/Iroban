from typing import Literal, Dict, List

from discord import PartialEmoji


# Consider:
# Perhaps it is possible, using a guild id/Context object, to get emoji IDs through the bot?
# It would look cleaner. And probably be better for future compatibility...

class ColorEmojis:
    """A dataclass used to generate and store a list of PartialEmojis."""

    # To consider: auto-handling emoji adding + cap checking
    # (See elif block below to comprehend basic idea)

    def __init__(self, color, ids, specials: dict):
        self.emojis = {}

        if color.lower() in ['blue', 'green', 'red', 'yellow']:
            # Numbered card integration
            for i, _id in zip(range(len(ids)), ids):
                name = f'{color}_{i}'
                self.emojis[name] = PartialEmoji(name=name, id=_id, animated=False)

            # Special card integration
            for card, _id in specials.items():
                name = f'{color}_{card}'
                self.emojis[name] = PartialEmoji(name=name, id=_id, animated=False)

        else:  # Currently unreachable until elif is removed
            raise TypeError(f'{color} is not a valid color name nor hex code.')

        """
        elif int(color.lstrip('#'), base=16):
            Maybe consider allowing custom colors. Just a consideration, though.
            
            Process: 
            - Check if we can register 
            - Take the hex value from `color`, open svg file 
              (meaning we have to store the original 0-9 + special emojis locally)
              [How do we even open it to edit? Does open() work??]
            - Edit the hex value for each file.
            - Datastream of the svg is registered as an emoji in a server. 
            - If over normal emoji cap, will convert to gif and add as animated gif.
        """

    def __iter__(self):
        return self.emojis.items()


# TODO: Make non-colored emojis/colored specials animated.
#  Only numbered colored ones stay normal

# TODO: Make these animated
colour_change = PartialEmoji(name='colour_change', id=848717422520434699, animated=False)
plus_4 = PartialEmoji(name='4_', id=848717422705901570, animated=False)

# TODO: These too \/
blue_spec = {'skip': 848717454979891201, 'reverse': 848717454629011456, 'p2': 848717450337714226}
green_spec = {'skip': 848717535524290580, 'reverse': 848717534156292118, 'p2': 848717529928826880}
red_spec = {'skip': 848717567378849823, 'reverse': 848717566511677541, 'p2': 848717562456178729}
yellow_spec = {'skip': 848735526806093844, 'reverse': 848735701553905684, 'p2': 848717597020913724}

blue_emojis = ColorEmojis(
    'blue',
    [848717450400235570, 848717450626465833, 848717450865541151, 848717451432427521, 848717453353811968,
     848717454795735052, 848717454799667270, 848717453873905715, 848717454536474665, 848717454532280342],
    blue_spec
)

green_emojis = ColorEmojis(
    'green',
    [848717529613729823, 848717530456784936, 848717530746454046, 848717530553516055, 848717531404435526,
     848717531954806826, 848717532227305483, 848717532965109791, 848717533338796043, 848717533933600779],
    green_spec
)

red_emojis = ColorEmojis(
    'red',
    [848717562329169951, 848717562707574795, 848717563545911316, 848717564284764200, 848717564250816512,
     848717564506275881, 848717565151674388, 848717565086007327, 848717565953703976, 848717566553489418],
    red_spec
)

# TODO: Unfuck this pls
# yert
yellow_emojis: dict = {
    **ColorEmojis(
        'yellow',
        [848717597331030016, 848717597390274581, 848717597993598976, 848717598270685205, 848717598745296966,
         848717599373656074, 848717599285575701, 848717599503155241],
        yellow_spec
    ).emojis,
    **{'yellow_8': PartialEmoji(name='yellow_8', id=848735623627931648, animated=True),
       'yellow_9': PartialEmoji(name='yellow_9', id=848735489859125269, animated=True)}
}

# Damn my IDE really do be hatin this typehint
all_emojis: Dict[Literal["yellow", "red", "blue", "green", "other"], List[PartialEmoji]] = {
    "yellow": yellow_emojis,
    "red": red_emojis,
    "blue": blue_emojis,
    "green": green_emojis,
    "other": [plus_4, colour_change]
}
