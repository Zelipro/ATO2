#Ici nous allons essayer de creer un sort de bibliotheque permttant de faire des conversions de base
def base_10_k(Nbr,Base,precision = 10):
    if Base > 16:
        return "La base doit etre inferieure ou egale a 16"
    else:
        
        dic = {10 : "A",11 : "B",12 : "C",13 : "D",14 : "E",15 : "F"}
         
        def Ecrit_correct(nbr,Base):
            if Base <= 10:
                return "".join(nbr)
            else:
                part11 = ""
                for elmt in nbr:
                    if len(elmt) == 2:
                        part11 += dic.get(int(elmt))
                    else:
                        part11 += elmt
                return part11
            
        Paties = str(Nbr).split(".")
        Grand_liste = []
        i = 0
        while(Base**i <= int(Paties[0])):
            Grand_liste.append(Base**i)
            i += 1
        Grand_liste = Grand_liste[::-1]
        
        part1 = []
        nbr = int(Paties[0])
        for elmt in Grand_liste:
            i = 0
            while(elmt <= nbr):
                i += 1
                nbr -= elmt
            part1.append(str(i))
        
        if len(Paties) == 1:
            return Ecrit_correct(part1,Base)
        elif len(Paties) == 2:
            nbr = float("0." + Paties[1])
            part2 = ["."]
            
            occu = 0
            while(nbr != 0):
                nbr *= Base
                NBR = str(nbr).split(".")
                part2.append(NBR[0])
                nbr = float("0." + NBR[1])
                occu += 1
                if occu > precision:
                    break
            
            return Ecrit_correct(part1,Base) + Ecrit_correct(part2,Base) if Ecrit_correct(part2,Base) != "."  else Ecrit_correct(part1,Base)
        else:
            return f"{Nbr} n'est pas un nombre accepatable !"

def base_k_10(Nbr,Base):
    if Base > 16 :
        return "La base doit etres inferieur ou egal a 16"
    else:
        parties = str(Nbr).split(".")
        
        dic = {"A" : 10 ,"B" : 11 ,"C" : 12 ,"D" : 13 ,"E" : 14 ,"F" : 15}
        PARTA = []
        def Ecrit_correct(nbr,Base):
            if Base <= 10:
                return [x for x in str(nbr)]
            else:
                for elmt in str(nbr):
                    if elmt in dic.keys():
                        PARTA.append(dic.get(elmt))
                    else:
                        PARTA.append(elmt)
                return PARTA
            
        
        Grand_list = []
        PART1 = Ecrit_correct(parties[0],Base)
        for _ in range(len(PART1)):
            Grand_list.append(Base**_)
        
        val = 0
        for elmt1,elmt2 in zip(Grand_list[::-1],PART1):
            val += int(elmt2)*elmt1
        
        if len(parties) == 1:
            return val
        elif len(parties) == 2:
            Grand_list2 = []
            
            PART2 = Ecrit_correct(parties[1],Base)
            
            for _ in range(1,len(PART2)+1):
                Grand_list2.append(Base**(-_))  
                
            for elmt1 ,elmt2 in zip(Grand_list2,PART2):
                val += int(elmt2)*elmt1
            
            return val          
        
    



#print(base_10_k(2799,16))
#print(base_k_10("12",4))
print(base_10_k(base_k_10("A",16),2))