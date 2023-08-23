import random
nbplayer = 2

def damage_line(cribase,min,max,mincri,maxcri,elem,do,carac_l,carac_d,mel,dofin=0,pou=0,pousupcri=0,ar=False,dore=0):
    if mel:
        type_do = "dome"
        type_re = "reperme"
    else:
        type_do = "dodist"
        type_re = "reperdist"

    rng_cri = random.randint(1, 100)

    if ar:    
        if rng_cri > (carac_l["cri"]+cribase):
            return (((random.randint(min, max)*((100+carac_l[elem]+carac_l["pui"])/100)+carac_l[do]+carac_l["do"])*((100+carac_l[type_do])/100)*((100+carac_l["doar"])/100)*((100+dofin)/100)) - carac_d["re"+elem]) * ((100-carac_d["reper"+elem])/100)*((100-carac_d[type_re])/100)*((100-dore)/100) + (((carac_l["lv"]/2)+(carac_l["dopou"]-carac_d["repou"]+32))*pou/4)
        else:
            #print("Critique !")
            pou = pou + pousupcri
            return (((random.randint(mincri, maxcri)*((100+carac_l[elem]+carac_l["pui"])/100)+carac_l[do]+carac_l["docri"]+carac_l["do"])*((100+carac_l[type_do])/100)*((100+carac_l["doar"])/100)*((100+dofin)/100)) - carac_d["recri"] - carac_d["re"+elem])*((100-carac_d["reper"+elem])/100)*((100-carac_d[type_re])/100)*((100-dore)/100) + (((carac_l["lv"]/2)+(carac_l["dopou"]-carac_d["repou"]+32))*pou/4)

    else:
        if (rng_cri < (carac_l["cri"]+cribase)) and (cribase >= 0):  

            #print("Critique !")
            pou = pou + pousupcri
            if min == max == mincri == maxcri == 0:
               return ((carac_l["lv"]/2)+(carac_l["dopou"]-carac_d["repou"]+32))*pou/4
            else :
                return (((random.randint(mincri, maxcri)*((100+carac_l[elem]+carac_l["pui"])/100)+carac_l[do]+carac_l["docri"]+carac_l["do"])*((100+carac_l[type_do])/100)*((100+carac_l["doso"])/100)*((100+dofin)/100)) - carac_d["recri"] - carac_d["re"+elem])*((100-carac_d["reper"+elem])/100)*((100-carac_d[type_re])/100)*((100-dore)/100) + (((carac_l["lv"]/2)+(carac_l["dopou"]-carac_d["repou"]+32))*pou/4)   
        
        else:
            if min == max == mincri == maxcri == 0:
               return (((carac_l["lv"]/2)+(carac_l["dopou"]-carac_d["repou"]+32))*pou/4)
            else :
                return (((random.randint(min, max)*((100+carac_l[elem]+carac_l["pui"])/100)+carac_l[do]+carac_l["do"])*((100+carac_l[type_do])/100)*((100+carac_l["doso"])/100)*((100+dofin)/100)) - carac_d["re"+elem])*((100-carac_d["reper"+elem])/100)*((100-carac_d[type_re])/100)*((100-dore)/100) + (((carac_l["lv"]/2)+(carac_l["dopou"]-carac_d["repou"]+32))*pou/4)

def soin():
    pass

carac_l = {
    "lv":200,
    "pdv":4345,
    "ini":3860,
    "PA":11,
    "PM":6,
    "PO":4,
    "invo":2,
    "so":2,
    "terre":420,
    "feu":1040,
    "eau":200,
    "air":200,
    "sa":410,
    "pui":110,
    "cri":64,
    "do":0,
    "docri":60,
    "dofeu":112,
    "doneu":52,
    "doterre":52,
    "doeau":20,
    "doair":20,
    "dopou":12,
    "doar":0,
    "doso":2,
    "dome":-14,
    "dodist":14,
    "retpa":41,
    "retpm":57,
    "esqpa":53,
    "esqpm":51,
    "reperneu":18,
    "reperterre":34,
    "reperfeu":42,
    "repereau":26,
    "reperair":31,
    "reneu":0,
    "refeu":0,
    "reair":0,
    "reeau":0,
    "reterre":0,
    "reperme":0,
    "reperdist":0,
    "recri":0,
    "repou":0
}

carac_Kardorim = {
    "lv":12,
    "pdv":140+(nbplayer-1)*10,
    "ini":200,
    "PA":7,
    "PM":4,
    "fo":50,
    "ine":50,
    "cha":50,
    "age":50,
    "sa":50,
    "retpa":5,
    "retpm":5,
    "esqpa":15,
    "esqpm":10,
    "reperneu":20,
    "reperterre":-15,
    "reperfeu":20,
    "repereau":-10,
    "reperair":5,
    "reneu":0,
    "refeu":0,
    "reair":0,
    "reeau":0,
    "reterre":0,
    "reperme":0,
    "reperdist":0
}

carac_Kardorib = {
    "lv":10,
    "pdv":60,
    "ini":100,
    "PA":7,
    "PM":4,
    "terre":50,
    "ine":0,
    "cha":0,
    "age":50,
    "pui":0,
    "sa":0,
    "cri":0,
    "retpa":0,
    "retpm":0,
    "esqpa":5,
    "esqpm":15,
    "doneu":0,
    "do":0,
    "dome":0,
    "doso":0,
    "reperneu":0,
    "reperterre":0,
    "reperfeu":0,
    "repereau":0,
    "reperair":0,
    "reneu":0,
    "refeu":0,
    "reair":0,
    "reeau":0,
    "reterre":0,
    "reperme":0,
    "reperdist":0,
    "dopou":0
}

def Kardorib_Embrochement(carac_l):
    return damage_line(0,31,37,31,37,"terre","doneu",carac_Kardorib,carac_l,True,0,2,0,False)


def liberation(carac_l,carac_r):
    return damage_line(0,0,0,0,0,"terre","doneu",carac_l,carac_r,True,0,4,0,False)