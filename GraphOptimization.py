from matplotlib import pyplot as plt
from math import floor

commonTailsman = 9
uncommonTailsman = 13
rareTailsman = 10
epicTailsman = 6
legendaryTailsman = 1

mainStrength = 74
mainCritDamage = 54
mainCritChance = 62

petStrength = 0
petCritDamage = 0
petCritChance = 0

weaponDamage = 265
weaponStrength = 150
weaponCritDamage = 80
weaponCritChance = 0

armorStrength = 160 
armorCritDamage = 0
armorCritChance = 0

global combatMultiplier
combatMultiplier = 1.92

fierceEpic=1
pureEpic=0
fierceLegendary=3
pureLegendary=0

armorStrength += (fierceEpic*8+fierceLegendary*10+pureEpic*6+pureLegendary*8)
armorCritDamage += (fierceEpic*14+fierceLegendary*18+pureEpic*6+pureLegendary*8)
armorCritChance += (fierceEpic*5+fierceLegendary*6+pureEpic*8+pureLegendary*10)

petBlaze = 1.30
armorStrength *= petBlaze
armorCritDamage *= petBlaze
armorCritChance *= petBlaze

#to calculate maxstat, we give 1 point to crit power or strength for each modifier and take the most
maxstats = commonTailsman*4+uncommonTailsman*5+rareTailsman*7+epicTailsman*10+legendaryTailsman*16

def damageCalculate(dmg, strength, critDmg):
 return ((((5+dmg+floor(strength/5))*(1+(strength/100)))*combatMultiplier)*(1+(critDmg/100)))

def damageCalculate2(dmg, strength, critDmg):
 return ((((5+dmg+floor(strength/5))*(1+(strength/100)))*combatMultiplier))

def damageCalculate3(dmg, strength, critDmg, critChance):
 return (damageCalculate(dmg, strength, critDmg)*critChance/100)+(damageCalculate2(dmg, strength, critDmg)*((100-critChance)/100))

y_TotalDamage = []
y_AverageDamage = []
x_Strength = []


for i in range(maxstats+1):
 totalStrength = mainStrength + weaponStrength + armorStrength + petStrength + i                        #starts from 0
 totalCritDamage = mainCritDamage + weaponCritDamage + armorCritDamage + petCritDamage + maxstats - i       #starts from end
 totalCritChance = mainCritChance + weaponCritChance + armorCritChance + petCritChance
 if totalCritChance >= 100:
     totalCritChance = 100
 y_TotalDamage.append(floor(damageCalculate(weaponDamage, totalStrength, totalCritDamage)))
 y_AverageDamage.append(floor(damageCalculate3(weaponDamage, totalStrength, totalCritDamage, totalCritChance)))
 x_Strength.append(i)

plt.plot(x_Strength, y_TotalDamage)
plt.plot(x_Strength, y_AverageDamage)
plt.ylabel("Final Damage")
plt.xlabel("Strength")
plt.title('DPS ' + str(mainStrength + weaponStrength + armorStrength + petStrength + y_TotalDamage.index(max(y_TotalDamage))) + " " + str(mainCritDamage + weaponCritDamage + armorCritDamage + petCritDamage + maxstats-y_TotalDamage.index(max(y_TotalDamage))))
plt.axhline(y = max(y_TotalDamage), color ="red")
plt.axhline(y = max(y_AverageDamage), color ="red")
plt.annotate("Max:"+str(max(y_TotalDamage))+" Str:"+str(y_TotalDamage.index(max(y_TotalDamage)))+" Crit:"+str(maxstats-y_TotalDamage.index(max(y_TotalDamage))), xy=(y_TotalDamage.index(max(y_TotalDamage)), max(y_TotalDamage)), xytext=(y_TotalDamage.index(max(y_TotalDamage)), max(y_TotalDamage) + 10),  arrowprops=dict(facecolor='black', shrink=0.01))
plt.annotate("Max:"+str(max(y_AverageDamage))+" Str:"+str(y_AverageDamage.index(max(y_AverageDamage)))+" Crit:"+str(maxstats-y_AverageDamage.index(max(y_AverageDamage))), xy=(y_AverageDamage.index(max(y_AverageDamage)), max(y_AverageDamage)), xytext=(y_AverageDamage.index(max(y_AverageDamage)), max(y_AverageDamage) + 10),  arrowprops=dict(facecolor='black', shrink=0.01))
plt.show()
