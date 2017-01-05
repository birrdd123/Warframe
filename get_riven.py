from max_dps import get_best_mods_multiprocess, weapons
import warframe_mods
from time import clock, sleep
from assertion import message
import os


pistols = 'ACRID;\
AKJAGARA;\
AKSOMATI;\
AKSTILETTO;\
AKSTILETTO PRIME;\
AKZANI;\
ANGSTRUM;\
ATOMOS;\
AZIMA;\
BALLISTICA;\
BALISTICA, RAKTA;\
BOLTO;\
BOLTO, AK;\
BOLTO, TELOS AK;\
BRAKK;\
BRONCO;\
BRONCO PRIME;\
BRONCO, AK;\
BRONCO, AK PRIME;\
CASTANAS;\
CASTANAS SANCTI;\
CESTRA;\
CESTRA, DUAL;\
CESTRA, SECURA DUAL;\
DESPAIR;\
DETRON;\
DETRON MARA;\
DUAL TOXOCYST;\
EMBOLIST;\
FURIS;\
FURIS, A;\
FURIS, DEX;\
FURIS, MK1;\
GAMMACOR;\
GAMMACOR SYNOID;\
HIKOU;\
HIKOU PRIME;\
KOHMAK;\
KOHMAK, TWIN;\
KRAKEN;\
KULSTAR;\
KUNAI;\
KUNAI MK1;\
LATO;\
LATO PRIME;\
LATO VANDAL;\
LATO, AK;\
LEX;\
LEX PRIME;\
LEX, AK;\
MAGNUS;\
MAGNUS, AK;\
MARELOK;\
MARELOK VAYKOR;\
NUKOR;\
POX;\
PYRANA;\
SEER;\
SICARUS;\
SICARUS PRIME;\
SONICOR;\
SPECTRA;\
SPIRA;\
SPIRA PRIME;\
STATICOR;\
STUG;\
TALONS;\
TWIN GRAKATAS;\
TWIN GREMLINS;\
TWIN ROGGA;\
TYSIS;\
VASTO;\
VASTO, AK;\
VASTO PRIME;\
VIPER;\
VIPER, TWIN;\
VIPER, WRAITH TWIN;\
PEACEMAKER;'
pistols = pistols.split(';')

shotguns = ['BOAR', 'BOAR PRIME', 'DRAKGOON', 'HEK', 'HEK, VAYKOR', 'KOHM', 'PHAGE', 'SOBEK', 'STRUN', 'STRUN, MK1', 'STRUN WRAITH', 'TIGRIS', 'TIGRIS PRIME', 'TIGRIS, SANCTI']



riven_mod = []
riven_to_use = []
with open(os.path.dirname(os.path.abspath(__file__))+'\Riven Mod.txt', 'r') as riven:
    x = riven.read().splitlines()

for each in x:
    if each[each.find(':')+1:] != '':
        riven_mod.append(each.replace('%', '').split(':'))

roll_count = 0
for each in riven_mod:
    if 'Raw Damage' in each:
        roll_count += 1
        riven_to_use.append(float(each[1])/100)
        riven_to_use.append('raw')
    if 'Crit Damage' in each:
        roll_count += 1
        riven_to_use.append(float(each[1])/100)
        riven_to_use.append('c_dmg')
    if 'Crit Chance' in each:
        roll_count += 1
        riven_to_use.append(float(each[1])/100)
        riven_to_use.append('c_chance')
    if 'Fire Rate' in each:
        roll_count += 1
        riven_to_use.append(float(each[1])/100)
        riven_to_use.append('fire_rate')
    if 'Impact' in each:
        roll_count += 1
        riven_to_use.append(float(each[1])/100)
        riven_to_use.append('impact')
    if 'Magazine Capacity' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('mag')
    if 'Multishot' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('multishot')
    if 'Puncture' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('puncture')
    if 'Reload Speed' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('reload')
    if 'Slash' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('slash')
    if 'Elemental-1' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('ele')
    if 'Elemental-2' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('ele')
    if 'Elemental-3' in each:
        roll_count += 1
        riven_to_use.append(float(each[1]) / 100)
        riven_to_use.append('ele')

riven_to_use.append('-Riven Mod-')
riven_to_use.insert(0, roll_count)
# print(riven_to_use)



def main():
    print(message)
    assert 'out of date' not in message.lower()
    a = clock()
    weapon_name = input('Enter Weapon Name: ')
    num_mods = input('Enter Number of Mods to check (1-8) Use 7 if using Riven Mod:')
    use_riven = input('Use Riven Mod?(y/n):')
    ton_riv = [2, .4, 'multishot', .75, 'mag', 'tonkor riv not mine']

    if weapon_name.upper() in pistols:
        if use_riven.upper() == 'Y':
            get_best_mods_multiprocess(weapon_name.upper(), int(num_mods), warframe_mods.pistol, riven= riven_to_use)
        else:
            get_best_mods_multiprocess(weapon_name.upper(), int(num_mods), warframe_mods.pistol, riven=None)
    elif weapon_name.upper() in shotguns:
        if use_riven.upper() == 'Y':
            get_best_mods_multiprocess(weapon_name.upper(), int(num_mods), warframe_mods.shotgun, riven=riven_to_use)
        else:
            get_best_mods_multiprocess(weapon_name.upper(), int(num_mods), warframe_mods.shotgun, riven=None)

    else:
        if use_riven.upper() == 'Y':
            get_best_mods_multiprocess(weapon_name.upper(), int(num_mods), warframe_mods.rifle, riven = riven_to_use)
        else:
            get_best_mods_multiprocess(weapon_name.upper(), int(num_mods), warframe_mods.rifle, riven=None)
    print('Completed in %s seconds' %str(clock()-a))

