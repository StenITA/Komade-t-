# funktsioonide definitsoonid Ülesanne

def komad(lause):
    # asendus tehted
    lause = lause.replace(" sest ", ", sest ")
    lause = lause.replace(' aga ', ', aga ')
    lause = lause.replace(' et ', ', et ')
    lause = lause.replace('2', 'ä')
    lause = lause.replace('y', 'ü')
    lause = lause.replace('6', 'õ')
    lause = lause.capitalize()
    print(lause)
    
# Sidesõnad    
    
def side(lause):
    lause = lause.replace(' otsekui ', ', otsekui ')
    lause = lause.replace(' justkui ', ', justkui ')
    lause = lause.replace(' ehkki ', ', ehkki ')
    lause = lause.replace(' vaid ', ', vaid ')
    lause = lause.replace(' ent ', ', ent ')
    lause = lause.replace(' või ', ', või ')
    lause = lause.replace(' ehk ', ', ehk ')
    lause = lause.replace(' ega ', ', ega ')
    lause = lause.replace(' ja ', ', ja ')
    lause = lause.replace(' ning ', ', ning ')
    lause = lause.replace(' aga ', ', aga ')
    lause = lause.replace(' kuid ', ', kuid ')
    lause = lause.replace(' sest ', ', sest ')
    lause = lause.replace(' et ', ', et ')
    lause = lause.replace(' kuna ', ', kuna ')
    lause = lause.replace(' kui ', ', kui ')
    lause = lause.replace(' nagu ', ', nagu ')
    lause = lause.replace(' kuigi ', ', kuigi ')
    lause = lause.replace(' kuni ', ', kuni ')
    lause = lause.capitalize()
    print(lause)
    
# Asesõnad    
    
def ase(lause):    
    lause = lause.replace(' kes ', ', kes ')
    lause = lause.replace(' mis ', ', mis ')
    lause = lause.replace(' kelle ', ', kelle ')
    lause = lause.replace(' mille ', ', mille ')
    lause = lause.replace(' keda ', ', keda ')
    lause = lause.replace(' mida või ', ', mida või ')
    lause = lause.capitalize()
    print(lause)
    
# Määrsõnad    
    
def määr(lause):    
    
    lause = lause.replace(' missugune ', ', missugune ')
    lause = lause.replace(' kas ', ', kas ')
    lause = lause.replace(' miks ', ', miks ')
    lause = lause.replace(' kuhu ', ', kuhu ')
    lause = lause.replace(' kuidas ', ', kuidas ')
    lause = lause.replace(' kust ', ', kust ')
    lause = lause.capitalize()
    
    print(lause)



# programmi algus

komad('mulle meeldib magada sest ma olen v2sinud sest olin kaua yleval.')
komad('magasin h2sti sest et ei olnud v2sinud aga ei tunne ennast v2ga h2sti')
komad('proge tunnid on v2ga l6busad ja mul pole kunagi igav')
määr('Sul kõlab nagu lahe kass mis on tema tõug ja missugune ta välja näeb? ')
ase('Tere kes teie olete ja mis teie siin teete?')
side('Alguses lõi Jumal taeva ja maa. See on hea raamat aga too teine on huvitavam. Jüri on noorem kui Mari.')
