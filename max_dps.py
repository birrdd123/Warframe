from xlrd import open_workbook
import itertools
from time import clock, sleep
from math import factorial
import warframe_mods
import testing
from multiprocessing import Process, Queue, freeze_support
import os



#  Open worksheet - assign 1st col to dictionary - assign entire row to list for each col
xl = open_workbook(os.path.dirname(os.path.abspath(__file__))+'/warframe_weapons.xlsx')
sheet = xl.sheet_by_index(0)
weapons = {}
# backup has 92 rows (rifles)
for rowt in range(170):
    row1 = sheet.row(rowt)
    temprow = []
    for each in row1:
        temprow.append(each.value)
    # print(temprow)
    t = temprow
    try:
        weapons.update({t[0]:[t[1],t[2],t[3],t[4],t[5],t[6],t[7],t[8],t[9],float(str(t[10]).replace('x','')),t[11],t[12],float(str(t[13]).replace('s',''))]})
    except:
        pass


class Weapon:

    def __init__(self, dl):
        """dl is list from dictionary of weapons"""
        self.impact = dl[2]
        self.puncture = dl[3]
        self.slash = dl[4]
        self.ele = dl[5]
        if self.ele == '-':
            self.ele = 0
        if self.ele == '':
            self.ele = 0
        self.fire_rate = dl[7]
        self.c_chance = dl[8]
        self.c_dmg = dl[9]
        self.mag = dl[11]
        self.reload = dl[12]
        self.mods = []
        self.multishot = 1
        self.bonus_ele = 0
        # Initiate mod values (start 0) can use to clear later - faster than new instance of class
        self.clear_mods()

    # return sus for now to store
    def get_stats(self, type):
        if type == 'sustained':
            return self.sustained_dps
        if type == 'burst':
            return self.burst_dps


    def clear_mods(self):
        self.mod_impact = 0
        self.mod_puncture = 0
        self.mod_slash = 0
        self.mod_c_chance = 0
        self.mod_c_dmg = 0
        self.mod_multishot = 0
        self.mod_ele = 0
        self.mod_reload = 0
        self.mod_raw = 0
        self.mod_mag = 0
        self.mod_fire_rate = 0
        self.bonus_ele = 0

    def add_single(self, m):
        # print('added', m)
        if m[2] == 'raw':
            self.mod_raw += m[1]
        if m[2] == 'impact':
            self.mod_impact += m[1]
        if m[2] == 'puncture':
            self.mod_puncture += m[1]
        if m[2] == 'slash':
            self.mod_slash += m[1]
        if m[2] == 'c_chance':
            self.mod_c_chance += m[1]
        if m[2] == 'c_dmg':
            self.mod_c_dmg += m[1]
        if m[2] == 'multishot':
            self.mod_multishot += m[1]
        if m[2] == 'ele':
            self.mod_ele += m[1]
        if m[2] == 'reload':
            self.mod_reload += m[1]
        if m[2] == 'mag':
            self.mod_mag += m[1]
        if m[2] == 'fire_rate':
            self.mod_fire_rate += m[1]

    def mod(self, mod_list):
        for m in mod_list:
            if m[0] > 1:
                for x in range(m[0]):
                    self.add_single([m[0], m[1 + (x*2)], m[2 + (x*2)]])
                pass
            else:
                self.add_single(m)

    def dps(self):
        # add mods only
        self.impact = self.impact * (1 + self.mod_raw)
        self.puncture = self.puncture * (1 + self.mod_raw)
        self.slash = self.slash * (1 + self.mod_raw)
        self.ele = self.ele * (1 + self.mod_raw)
        self.c_chance = self.c_chance * (1 + self.mod_c_chance)
        self.c_dmg = self.c_dmg * (1 + self.mod_c_dmg)
        self.fire_rate = self.fire_rate * (1 + self.mod_fire_rate)
        self.mag = round(self.mag * (1 + self.mod_mag))
        self.multishot = self.mod_multishot
        self.reload = self.reload / (1 + self.mod_reload)
        # do bonus ele before adding specific physical as they dont count toward ele
        self.bonus_ele = self.mod_ele * (self.impact + self.puncture + self.slash + self.ele)

        # specific phys applied last
        self.impact = self.impact * (1 + self.mod_impact)
        self.puncture = self.puncture * (1 + self.mod_puncture)
        self.slash = self.slash * (1 + self.mod_slash)

        # after crit
        self.impact = ((self.impact * self.c_dmg) * self.c_chance) + (self.impact * (1 - self.c_chance))
        self.puncture = ((self.puncture * self.c_dmg) * self.c_chance) + (self.puncture * (1 - self.c_chance))
        self.slash = ((self.slash * self.c_dmg) * self.c_chance) + (self.slash * (1 - self.c_chance))
        self.ele = ((self.ele * self.c_dmg) * self.c_chance) + (self.ele * (1 - self.c_chance))
        self.bonus_ele = ((self.bonus_ele * self.c_dmg) * self.c_chance) + (self.bonus_ele * (1 - self.c_chance))

        # after multishot
        self.impact *= 1 + self.mod_multishot
        self.puncture *= 1 + self.mod_multishot
        self.slash *= 1 + self.mod_multishot
        self.ele *= 1 + self.mod_multishot
        self.bonus_ele *= 1 + self.mod_multishot
        # per shot
        self.damage_per_shot = self.impact + self.puncture + self.slash + self.bonus_ele + self.ele
        self.burst_dps = (self.damage_per_shot * self.mag) / (self.mag / self.fire_rate)
        self.sustained_dps = (self.damage_per_shot * self.mag) / ((self.mag / self.fire_rate) + self.reload)



def gun_thread1(gun, x, q, riven_mod = None):

    global start
    count = 0
    for each in x:
        if riven_mod:
            each = list(each)
            each.append(riven_mod)
        count+= 1
        bro = Weapon(weapons[gun])
        bro.mod(each)
        bro.dps()
        current = bro.get_stats('sustained')
        if current > start:
            start = current
            mods = each
    q.put(start)
    q.put(mods)



start = 0
def get_best_mods_multiprocess(gun, number_mods, mod_list, riven = None):
    q = Queue()
    global start
    mods_to_check = number_mods
    x = list(itertools.combinations(mod_list, mods_to_check))
    combinations = factorial(len(mod_list)) / (factorial(mods_to_check)* factorial(len(mod_list) - mods_to_check))
    print(int(combinations), 'Total Combinations')
    t1 = Process(target=gun_thread1, args=(gun, x[0:int(len(x) / 3)], q, riven))
    t2 = Process(target=gun_thread1, args=(gun, x[int(len(x) / 3):int(len(x) / 3)*2 ], q, riven))
    t3 = Process(target=gun_thread1, args=(gun, x[int(len(x) / 3)*2:], q, riven))
    t1.start()
    t2.start()
    t3.start()
    t2.join()
    t1.join()
    t3.join()
    highest = []
    while not q.empty():
        dmg = q.get()
        mods = [each[-1] for each in q.get()]
        highest.append([dmg, mods])
    best = max(highest)
    print('---------------------'+str(best[0])+' Sustained DPS ---------------------')
    print('Mods:'+ ' '.join(each for each in best[1]))
    print()

if __name__ == '__main__':
    freeze_support()
    q = Queue()
    testing.main()
    input('Enter to restart')
    os.system(os.path.dirname(os.path.abspath(__file__))+'\\max_dps.exe')

