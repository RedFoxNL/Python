def bepaal_wissel(prijs, ontvangen):
    # dictionary met key = biljet of munt en value = aantal
    geld_dict = {50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
    wisselgeld = ontvangen - prijs
    # maak en sorteer lijst
    lijst = 50,20,10,5,2,1

    for b in lijst:
        count = 0
        # als er wisselgeld >= b dan ...
        while wisselgeld >= b:
            count +=1
            wisselgeld -=b
            if wisselgeld == 0:
                break
        geld_dict[b] += count

    for k in geld_dict.keys():
            if geld_dict[k] != 0:
                print('Het wisselgeld is:',geld_dict[k],'x',k)


bepaal_wissel(1, 6)   # 1x5
bepaal_wissel(4, 109) # 2x50, 1x5

