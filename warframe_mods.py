import os

argon_scope = [1, 1.35, 'c_chance', '-Argon Scope-']
bladed_rounds = [1, 1.2, 'c_dmg', '-Bladed Rounds-']
crash_course = [1, 1.2, 'impact', '-Crash Course-']
critical_delay = [2, .48, 'c_chance', -.36, 'fire_rate', '-Critical Delay-']
cryo_rounds = [1, .9, 'ele', '-Cryo Rounds reg-']
fanged_fusillade = [1, 1.2, 'slash', '-Fanged Fusillade-']
# fast_hands = [1, .3, 'reload', '-Fast Hands-']
hammer_shot = [1, .6, 'c_dmg', '-Hammer Shot-']
heavy_caliber = [1, 1.65, 'raw', '-Heavy Caliber-']
hellfire = [1, .9, 'ele', '-Hellfire-']
high_voltage = [1, .6, 'ele', '-high_voltage-']
primed_cryo_rounds = [1, 1.65, 'ele', '-primed cryo rounds-']
infected_clip = [1, .9, 'ele', '-infected_clip-']
magazine_warp = [1, .3, 'mag', '-magazine_warp-']
malignant_force = [1, .6, 'ele', '-malignant_force-']
piercing_caliber = [1, 1.2, 'puncture', '-piercing_caliber-']
piercing_hit = [1, .3, 'puncture', '-piercing_hit-']
point_strike = [1, 1.5, 'c_chance', '-point_strike-']
primed_fast_hands = [1, .55, 'reload', '-primed_fast_hands-']
rime_rounds = [1, .6, 'ele', '-rime_rounds-']
rupture = [1, .3, 'impact', '-rupture-']
sawtooth_clip = [1, .3, 'slash', '-sawtooth_clip-']
serration = [1, 1.65, 'raw', '-serration-']
shred = [1, .3, 'fire_rate', '-shred-']
speed_trigger = [1, .6, 'fire_rate', '-speed_trigger-']
split_chamber = [1, .9, 'multishot', '-split chamber-']
stormbringer = [1, .9, 'ele', '-stormbringer-']
thermite_rounds = [1, .6, 'ele', '-thermite_rounds-']
vile_acceleration = [2, .9, 'fire_rate', -.15, 'raw', '-Vile Acceleration-']
vital_sense = [1, 1.2, 'c_dmg', '-Vital Sense-']
wildfire = [2, .2, 'mag', .6, 'ele', '-Wildfire-']

rifle = [argon_scope, bladed_rounds,  crash_course, cryo_rounds, critical_delay,  fanged_fusillade, primed_fast_hands, hammer_shot, heavy_caliber, hellfire,  infected_clip, magazine_warp, piercing_caliber, piercing_hit, point_strike, rime_rounds, rupture, sawtooth_clip, serration, shred, speed_trigger, split_chamber, stormbringer, thermite_rounds, vile_acceleration, vital_sense, wildfire, primed_cryo_rounds, high_voltage, malignant_force]

# rifle_no_primed_cryo = [argon_scope, bladed_rounds, crash_course, cryo_rounds, critical_delay,  fanged_fusillade, primed_fast_hands, hammer_shot, heavy_caliber, hellfire,  infected_clip, magazine_warp, piercing_caliber, piercing_hit, point_strike, rime_rounds, rupture, sawtooth_clip, serration, shred, speed_trigger, split_chamber, stormbringer, thermite_rounds, vile_acceleration, vital_sense, wildfire, high_voltage]
#
# rifle_no_low_ele = [argon_scope, bladed_rounds, crash_course, critical_delay,  fanged_fusillade, primed_fast_hands, hammer_shot, heavy_caliber, hellfire,  infected_clip, magazine_warp, piercing_caliber, piercing_hit, point_strike, rupture, sawtooth_clip, serration, shred, speed_trigger, split_chamber, stormbringer, vile_acceleration, vital_sense, wildfire, primed_cryo_rounds]
#
# rifle_no_argon_bladed = [crash_course, critical_delay,  fanged_fusillade, primed_fast_hands, hammer_shot, heavy_caliber, hellfire,  infected_clip, magazine_warp, piercing_caliber, piercing_hit, point_strike, rime_rounds, rupture, sawtooth_clip, serration, shred, speed_trigger, split_chamber, stormbringer, thermite_rounds, vile_acceleration, vital_sense, wildfire, primed_cryo_rounds, high_voltage]
#
# rifle_no_argon = [bladed_rounds, crash_course, critical_delay,  fanged_fusillade, primed_fast_hands, hammer_shot, heavy_caliber, hellfire,  infected_clip, magazine_warp, piercing_caliber, piercing_hit, point_strike, rime_rounds, rupture, sawtooth_clip, serration, shred, speed_trigger, split_chamber, stormbringer, thermite_rounds, vile_acceleration, vital_sense, wildfire, primed_cryo_rounds, high_voltage]
#
# rifle_no_split = [crash_course, critical_delay,  fanged_fusillade, primed_fast_hands, hammer_shot, heavy_caliber, hellfire,  infected_clip, magazine_warp, piercing_caliber, piercing_hit, point_strike, rime_rounds, rupture, sawtooth_clip, serration, shred, speed_trigger, stormbringer, thermite_rounds, vile_acceleration, vital_sense, wildfire, cryo_rounds, high_voltage]


with open(os.path.dirname(os.path.abspath(__file__))+'\\exclude_mods.txt', 'r') as ex:
    exclude = ex.read().splitlines()
    exclude = [each.upper().replace(' ', '') for each in exclude]


for mod in exclude:
    for each in rifle:
        if mod in each[-1].upper().replace(' ', ''):
            rifle.remove(each)


anemic_agility = [2, .9, 'fire_rate', -.15, 'raw', 'Anemic Agility']
barrel_diffusion = [1, 1.2, 'multishot', 'Barrel Diffusion']
bore = [1, 1.2, 'puncture', 'Bore']
concussion_rounds = [1, .6, 'impact', 'Concussion Rounds']
convulsion = [1, .9, 'ele', 'Convulsion']
creeping_bullseye = [2, .48, 'c_chance', -.36, 'fire_rate', 'Creeping Bullseye']
deep_freeze = [1, .9, 'ele', 'Deep Freeze']
frostbite = [1, .6, 'ele', 'Frostbite']
gunslinger = [1, .72, 'fire_rate', 'Gunslinger']
heated_charge = [1, .9, 'ele', 'Heated Charge reg']
hollow_point = [2, .6, 'c_dmg', -.15, 'raw', 'Hollow Point']
hornet_strike = [1, 2.2, 'raw', 'Hornet Strike']
hydraulic_crosshairs = [1, 1.35, 'c_chance', 'Hydraulic Crosshairs']
ice_storm = [2, .4, 'mag', .4, 'ele', 'Ice Storm']
jolt = [1, .6, 'ele', 'Jolt']
lethal_torrent = [2, .6, 'fire_rate', .6, 'multishot', 'Lethal Torrent']
magnum_force = [1, .66, 'raw', 'Magnum Force']
maim = [1, 1.2, 'slash', 'Maim']
no_return = [1, .6, 'puncture', 'No Return']
pathogen_rounds = [1, .9, 'ele', 'Pathogen Rounds']
pistol_gambit = [1, 1.2, 'c_chance', 'Pistol Gambit reg']
pistol_pestilence = [1, .6, 'ele', 'Pistol Pestilence']
pressurized_magazine = [1, .9, 'fire_rate', 'Pressurized Magazine']
primed_heated_charge = [1, 1.65, 'ele', 'Primed Heated Charge']
primed_pistol_gambit = [1, 1.87, 'c_chance', 'Primed Pistol Gambit']
primed_slip_magazine = [1, .55, 'mag', 'Primed Slip Magazine']
primed_target_cracker = [1, 1.1, 'c_dmg', 'Primed Target Cracker']
pummel = [1, 1.2, 'impact', 'Pummel']
quickdraw = [1, .48, 'reload', 'Quickdraw']
razor_shot = [1, .6, 'slash', 'Razor Shot']
scorch = [1, .6, 'ele', 'Scorch']
sharpened_bullets = [1, .75, 'c_dmg', 'Sharpened Bullets']
slip_magazine = [1, .3, 'mag', 'Slip Magazine reg']
stunning_speed = [1, .4, 'reload', 'Stunning Speed']
tainted_clip = [2, .6, 'mag', -.3, 'reload', 'Tainted Clip']
target_cracker = [1, .6, 'c_dmg', 'Target Cracker reg']

pistol = [anemic_agility, barrel_diffusion, bore, concussion_rounds, convulsion, creeping_bullseye, deep_freeze, frostbite, gunslinger, heated_charge, hollow_point, hornet_strike, hydraulic_crosshairs, ice_storm, jolt, lethal_torrent, magnum_force, maim, no_return, pathogen_rounds, pistol_gambit, pistol_pestilence, pressurized_magazine, primed_heated_charge, primed_pistol_gambit, primed_slip_magazine, primed_target_cracker, pummel, quickdraw, razor_shot, scorch, sharpened_bullets, slip_magazine, stunning_speed, tainted_clip, target_cracker]

for mod in exclude:
    for each in pistol:
        if mod in each[-1].upper().replace(' ', ''):
            pistol.remove(each)
if __name__ == '__main__':
    print(len(rifle), len(pistol))



accelerated_blast = [2, .6, 'fire_rate', .6, 'puncture', 'Accelerated Blast']
ammo_stock = [1, .6, 'mag', 'Ammo Stock']
blaze = [2, .6, 'raw', .6, 'ele', 'Blaze']
blunderbuss = [1, .9, 'c_chance', 'Blunderbuss']
breach_loader = [1, 1.2, 'puncture', 'Breach Loader']
burdened_magazine = [2, .6, 'mag', -.18, 'reload', 'Burdened Magazine']
charged_shell = [1, .9, 'ele', 'Charged Shell']
chilling_grasp = [1, .9, 'ele', 'Chilling Grasp']
chilling_reload = [2, .6, 'ele', .4, 'reload', 'Chilling Reload']
contagious_spread = [1, .9, 'ele', 'Contagious Spread']
critical_deceleration = [2, .48, 'c_chance', -.36, 'fire_rate', 'Critical Deceleration']
disruptor = [1, .3, 'impact', 'Disruptor']
flachette = [1, .3, 'puncture', 'Flachette']
frail_momentum = [2, .9, 'fire_rate', -.15, 'raw', 'Frail Momentum']
frigid_blast = [1, .6, 'ele', 'Frigid Blast']
full_contact = [1, 1.2, 'impact', 'Full Contact']
hells_chamber = [1, 1.2, 'multishot', 'Hells Chamber']
incendiary_coat = [1, .9, 'ele', 'Incendiary Coat']
laser_sight = [1, 1.2, 'c_chance', 'Laser Sight']
point_blank = [1, .9, 'raw', 'Point Blank reg']
primed_point_blank = [1, 1.65, 'raw', 'Primed Point Blank']
primed_ravage = [1, 1.10, 'c_dmg', 'Primed Ravage']
ravage = [1, .6, 'c_dmg', 'Ravage reg']
repeater_clip = [1, 1.05, 'fire_rate', 'Repeater Clip']
scattering_inferno = [1, .6, 'ele', 'Scattering Inferno']
seeking_fury = [1, .15, 'reload', 'Seeking Fury']
shell_shock = [1, .6, 'ele', 'Shell Shock']
shotgun_spazz = [1, .9, 'fire_rate', 'Shotgun Spazz']
shrapnel_shot = [1, .99, 'c_dmg', 'Shrapnel Shot']
shredder = [1, .3, 'slash', 'Shredder']
sweeping_serration = [1, 1.2, 'slash', 'Sweeping Serration']
tactical_pump = [1, .3, 'reload', 'Tactical Pump']
toxic_barrage = [1, .6, 'ele', 'Toxic Barrage']
vicious_spread = [1, .9, 'raw', 'Vicious Spread']

shotgun = [accelerated_blast, ammo_stock, blaze, blunderbuss, breach_loader, burdened_magazine, charged_shell, chilling_grasp, chilling_reload, contagious_spread, critical_delay, disruptor, flachette, frail_momentum, frigid_blast, full_contact, hells_chamber, incendiary_coat, laser_sight, point_blank, primed_point_blank, primed_ravage, ravage, repeater_clip, scattering_inferno, seeking_fury, shell_shock, shotgun_spazz, shrapnel_shot, shredder, sweeping_serration, tactical_pump, toxic_barrage, vicious_spread]


for mod in exclude:
    for each in shotgun:
        if mod in each[-1].upper().replace(' ', ''):
            shotgun.remove(each)










