import random

class Character:
    def __init__(self, lv=1, pdv=1, ini=0, PA=0, PM=0, PO=0, invo=0, so=0, terre=0, feu=0, eau=0, air=0, sa=0, pui=0, cri=0, do=0, docri=0, dofeu=0, doneu=0, doterre=0, doeau=0, doair=0, dopou=0, doar=0, doso=0, dome=0, dodist=0, retpa=0, retpm=0, esqpa=0, esqpm=0, reperneu=0, reperterre=0, reperfeu=0, repereau=0, reperair=0, reneu=0, refeu=0, reair=0, reeau=0, reterre=0, reperme=0, reperdist=0, recri=0, repou=0):
        self.lv = lv
        self.pdv = pdv
        self.ini = ini
        self.PA = PA
        self.PM = PM
        self.PO = PO
        self.invo = invo
        self.so = so
        self.terre = terre
        self.feu = feu
        self.eau = eau
        self.air = air
        self.sa = sa
        self.pui = pui
        self.cri = cri
        self.do = do
        self.docri = docri
        self.dofeu = dofeu
        self.doneu = doneu
        self.doterre = doterre
        self.doeau = doeau
        self.doair = doair
        self.dopou = dopou
        self.doar = doar
        self.doso = doso
        self.dome = dome
        self.dodist = dodist
        self.retpa = retpa
        self.retpm = retpm
        self.esqpa = esqpa
        self.esqpm = esqpm
        self.reperneu = reperneu
        self.reperterre = reperterre
        self.reperfeu = reperfeu
        self.repereau = repereau
        self.reperair = reperair
        self.reneu = reneu
        self.refeu = refeu
        self.reair = reair
        self.reeau = reeau
        self.reterre = reterre
        self.reperme = reperme
        self.reperdist = reperdist
        self.recri = recri
        self.repou = repou

class DamageCalculator:
    def __init__(self, carac_l, carac_d):
        self.carac_l = carac_l
        self.carac_d = carac_d

    def calculate_damage(self, cribase, min_damage, max_damage, mincri, maxcri, elem, do, mel, dofin=0, pou=0, pousupcri=0, ar=False, dore=0):
        
        rng_cri = random.randint(1, 100)

        if mel:
            type_do = "dome"
            type_re = "reperme"
        else:
            type_do = "dodist"
            type_re = "reperdist"

        if ar:
            if rng_cri > (self.carac_l.cri + cribase):
                return (((random.randint(min_damage, max_damage) * ((100 + getattr(self.carac_l,elem) + self.carac_l.pui) / 100) + getattr(self.carac_l,do) + self.carac_l.do) * ((100 + getattr(self.carac_l,type_do)) / 100) * ((100 + self.carac_l.doar) / 100) * ((100 + dofin) / 100) - getattr(self.carac_d,"do"+elem)) * ((100 - getattr(self.carac_d,"reper" + elem)) / 100) * ((100 - getattr(self.carac_d,type_re)) / 100) * ((100 - dore) / 100) + (((self.carac_l.lv / 2) + (self.carac_l.dopou - self.carac_d.repou + 32)) * pou / 4))
            else:
                pou += pousupcri
                return (((random.randint(mincri, maxcri) * ((100 + getattr(self.carac_l,elem) + self.carac_l.pui) / 100) + getattr(self.carac_l,do) + self.carac_l.docri + self.carac_l.do) * ((100 + getattr(self.carac_l,type_do)) / 100) * ((100 + self.carac_l.doar) / 100) * ((100 + dofin) / 100) - self.carac_d.recri - getattr(self.carac_d,"do"+elem)) * ((100 - getattr(self.carac_d,"reper" + elem)) / 100) * ((100 - getattr(self.carac_d,type_re)) / 100) * ((100 - dore) / 100) + (((self.carac_l.lv / 2) + (self.carac_l.dopou - self.carac_d.repou + 32)) * pou / 4))

        else:
            if (rng_cri > (self.carac_l.cri + cribase)) and (cribase >= 0):
                if min_damage == max_damage == mincri == maxcri == 0:
                    return (((self.carac_l.lv / 2) + (self.carac_l.dopou - self.carac_d.repou + 32)) * pou / 4)
                else:
                    return (((random.randint(min_damage, max_damage) * ((100 + getattr(self.carac_l, elem) + self.carac_l.pui) / 100) + getattr(self.carac_l, do) + self.carac_l.do) * ((100 + getattr(self.carac_l, type_do)) / 100) * ((100 + self.carac_l.doso) / 100) * ((100 + dofin) / 100) - getattr(self.carac_l, 'do'+elem)) * ((100 - getattr(self.carac_l, "reper" + elem)) / 100) * ((100 - getattr(self.carac_l, type_re)) / 100) * ((100 - dore) / 100) + (((self.carac_l.lv / 2) + (self.carac_l.dopou - self.carac_d.repou + 32)) * pou / 4))
            else:
                pou += pousupcri
                if min_damage == max_damage == mincri == maxcri == 0:
                    return ((self.carac_l.lv / 2) + (self.carac_l.dopou - self.carac_d.repou + 32)) * pou / 4
                else:
                    return (((random.randint(mincri, maxcri) * ((100 + getattr(self.carac_l,elem) + self.carac_l.pui) / 100) + getattr(self.carac_l,do) + self.carac_l.docri + self.carac_l.do) * ((100 + getattr(self.carac_l,type_do)) / 100) * ((100 + self.carac_l.doso) / 100) * ((100 + dofin) / 100) - self.carac_d.recri - getattr(self.carac_d, "do"+elem)) * ((100 - getattr(self.carac_d,"reper" + elem)) / 100) * ((100 - getattr(self.carac_d,type_re)) / 100) * ((100 - dore) / 100) + (((self.carac_l.lv / 2) + (self.carac_l.dopou - self.carac_d.repou + 32)) * pou / 4))


# Example usage:
carac_l = Character(
    lv=200,
    pdv=3903,
    ini=1963,
    PA=12,
    PM=6,
    PO=3,
    invo=5,
    so=0,
    terre=100,
    feu=100,
    eau=100,
    air=1363,
    sa=465,
    pui=110,
    cri=8,
    docri=0,
    dofeu=25,
    doneu=25,
    doterre=25,
    doeau=25,
    doair=198,
    dopou=25,
    doar=0,
    doso=1,
    dome=-15,
    dodist=21,
    retpa=46,
    retpm=46,
    esqpa=67,
    esqpm=87,
    reperneu=10,
    reperterre=10,
    reperfeu=10,
    repereau=37,
    reperair=10,
    reneu=5,
    refeu=10,
    reair=10,
    reeau=5,
    reterre=5,
    reperme=10,
    reperdist=5,
    recri=110,
    repou=55
)

carac_d = Character()

calculator = DamageCalculator(carac_l, carac_d)
print("Default:")
#run 1000 times to get average damage, the minimum and the maximum
min = 100000
max = 0
sum = 0
for i in range(100000):
    damage = calculator.calculate_damage(cribase=10, min_damage=34, max_damage=38, mincri=41, maxcri=46, elem="air", do="doair", mel=False, dofin=0, pou=0, pousupcri=0, ar=False, dore=0)
    sum += damage
    if damage < min:
        min = damage
    if damage > max:
        max = damage

print(f"Sorts Air 34-38 41-46 10%cc base: {sum/100000} (min: {min}, max: {max})")


carac_l.cri = carac_l.cri - 1
carac_l.doso = carac_l.doso + 1

calculator = DamageCalculator(carac_l, carac_d)

print("For 1% do more, -1% crit:")
#run 1000 times to get average damage, the minimum and the maximum
min = 100000
max = 0
sum = 0
for i in range(100000):
    damage = calculator.calculate_damage(cribase=10, min_damage=34, max_damage=38, mincri=41, maxcri=46, elem="air", do="doair", mel=False, dofin=0, pou=0, pousupcri=0, ar=False, dore=0)
    sum += damage
    if damage < min:
        min = damage
    if damage > max:
        max = damage

print(f"Sorts Air 34-38 41-46 10%cc base : {sum/100000} (min: {min}, max: {max})")



carac_l.cri = carac_l.cri + 1

calculator = DamageCalculator(carac_l, carac_d)

print("For 1% do more:")
min = 100000
max = 0
sum = 0
for i in range(100000):
    damage = calculator.calculate_damage(cribase=10, min_damage=34, max_damage=38, mincri=41, maxcri=46, elem="air", do="doair", mel=False, dofin=0, pou=0, pousupcri=0, ar=False, dore=0)
    sum += damage
    if damage < min:
        min = damage
    if damage > max:
        max = damage

print(f"Sorts Air 34-38 41-46 10%cc base: {sum/100000} (min: {min}, max: {max})")
