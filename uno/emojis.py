from typing import Literal

from discord import PartialEmoji

colour_change = PartialEmoji(name='colour_change', id=848717422520434699, animated=False)
plus_4 = PartialEmoji(name='4_', id=848717422705901570, animated=False)
blue_p2 = PartialEmoji(name='blue_p2', id=848717450337714226, animated=False)
blue_0 = PartialEmoji(name='blue_0', id=848717450400235570, animated=False)
blue_1 = PartialEmoji(name='blue_1', id=848717450626465833, animated=False)
blue_2 = PartialEmoji(name='blue_2', id=848717450865541151, animated=False)
blue_3 = PartialEmoji(name='blue_3', id=848717451432427521, animated=False)
blue_4 = PartialEmoji(name='blue_4', id=848717453353811968, animated=False)
blue_7 = PartialEmoji(name='blue_7', id=848717453873905715, animated=False)
blue_9 = PartialEmoji(name='blue_9', id=848717454532280342, animated=False)
blue_8 = PartialEmoji(name='blue_8', id=848717454536474665, animated=False)
blue_reverse = PartialEmoji(name='blue_reverse', id=848717454629011456, animated=False)
blue_5 = PartialEmoji(name='blue_5', id=848717454795735052, animated=False)
blue_6 = PartialEmoji(name='blue_6', id=848717454799667270, animated=False)
blue_skip = PartialEmoji(name='blue_skip', id=848717454979891201, animated=False)
green_0 = PartialEmoji(name='green_0', id=848717529613729823, animated=False)
green_p2 = PartialEmoji(name='green_p2', id=848717529928826880, animated=False)
green_1 = PartialEmoji(name='green_1', id=848717530456784936, animated=False)
green_3 = PartialEmoji(name='green_3', id=848717530553516055, animated=False)
green_2 = PartialEmoji(name='green_2', id=848717530746454046, animated=False)
green_4 = PartialEmoji(name='green_4', id=848717531404435526, animated=False)
green_5 = PartialEmoji(name='green_5', id=848717531954806826, animated=False)
green_6 = PartialEmoji(name='green_6', id=848717532227305483, animated=False)
green_7 = PartialEmoji(name='green_7', id=848717532965109791, animated=False)
green_8 = PartialEmoji(name='green_8', id=848717533338796043, animated=False)
green_9 = PartialEmoji(name='green_9', id=848717533933600779, animated=False)
green_reverse = PartialEmoji(name='green_reverse', id=848717534156292118, animated=False)
green_skip = PartialEmoji(name='green_skip', id=848717535524290580, animated=False)
red_0 = PartialEmoji(name='red_0', id=848717562329169951, animated=False)
red_p2 = PartialEmoji(name='red_p2', id=848717562456178729, animated=False)
red_1 = PartialEmoji(name='red_1', id=848717562707574795, animated=False)
red_2 = PartialEmoji(name='red_2', id=848717563545911316, animated=False)
red_4 = PartialEmoji(name='red_4', id=848717564250816512, animated=False)
red_3 = PartialEmoji(name='red_3', id=848717564284764200, animated=False)
red_5 = PartialEmoji(name='red_5', id=848717564506275881, animated=False)
red_7 = PartialEmoji(name='red_7', id=848717565086007327, animated=False)
red_6 = PartialEmoji(name='red_6', id=848717565151674388, animated=False)
red_8 = PartialEmoji(name='red_8', id=848717565953703976, animated=False)
red_reverse = PartialEmoji(name='red_reverse', id=848717566511677541, animated=False)
red_9 = PartialEmoji(name='red_9', id=848717566553489418, animated=False)
red_skip = PartialEmoji(name='red_skip', id=848717567378849823, animated=False)
yellow_p2 = PartialEmoji(name='yellow_p2', id=848717597020913724, animated=False)
yellow_0 = PartialEmoji(name='yellow_0', id=848717597331030016, animated=False)
yellow_1 = PartialEmoji(name='yellow_1', id=848717597390274581, animated=False)
yellow_2 = PartialEmoji(name='yellow_2', id=848717597993598976, animated=False)
yellow_3 = PartialEmoji(name='yellow_3', id=848717598270685205, animated=False)
yellow_4 = PartialEmoji(name='yellow_4', id=848717598745296966, animated=False)
yellow_6 = PartialEmoji(name='yellow_6', id=848717599285575701, animated=False)
yellow_5 = PartialEmoji(name='yellow_5', id=848717599373656074, animated=False)
yellow_7 = PartialEmoji(name='yellow_7', id=848717599503155241, animated=False)
yellow_9 = PartialEmoji(name='yellow_9', id=848735489859125269, animated=True)
yellow_skip = PartialEmoji(name='yellow_skip', id=848735526806093844, animated=True)
yellow_8 = PartialEmoji(name='yellow_8', id=848735623627931648, animated=True)
yellow_reverse = PartialEmoji(name='yellow_reverse', id=848735701553905684, animated=True)

yellow_emojis = [yellow_0, yellow_1, yellow_2, yellow_3, yellow_4, yellow_5, yellow_6, yellow_7, yellow_8, yellow_9,
                 yellow_p2, yellow_reverse, yellow_skip]
red_emojis = [red_0, red_1, red_2, red_3, red_4, red_5, red_6, red_7, red_8, red_9, red_p2, red_reverse, red_skip]
green_emojis = [green_0, green_1, green_2, green_3, green_4, green_5, green_6, green_7, green_8, green_9, green_p2,
                green_reverse, green_skip]
blue_emojis = [blue_0, blue_1, blue_2, blue_3, blue_4, blue_5, blue_6, blue_7, blue_8, blue_9, blue_p2, blue_reverse,
               blue_skip]

all_emojis: dict[Literal["yellow", "red", "blue", "green", "other"], list[PartialEmoji]] = {
    "yellow": yellow_emojis,
    "red": red_emojis,
    "blue": blue_emojis,
    "green": green_emojis,
    "other": [plus_4, colour_change]
}