# Warframe
Warframe DPS Python Module

if you want to use as-is in python, remove the last line of max_dps.py, as that relaunches the exe.

assertion gets text from google docs file to display at start up.  Main program asserts that "out of date" is not in that text, in case there is a major flaw in the exe version, it will die at startup.

### To use in python insetead of exe

#### from max_dps import Weapon, weapons

#### boltor = Weapon(weapons['Boltor'])

add a mod

#### boltor.mod(any mod found in warframe_mods.py)

run calculation

#### boltor.dps()

get burst or sustained dps

#### dps = boltor.get_stats('sustained')
