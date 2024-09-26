sokolates1 = [155, 77, 141, 73, 90, 192, 181, 149, 148, 77, 168, 143,
100, 72, 149, 195, 124, 193, 102, 186, 165, 141, 135, 189,
81, 130, 183, 99, 108, 139, 143, 138, 169, 160, 156, 72, 93,
156, 124, 166, 76, 122, 104, 174, 173, 91, 177, 143, 104, 183,
97, 125, 177, 155, 152, 175, 192, 155, 80, 109, 82, 174, 176, 76,
165, 96, 87, 115, 72, 112, 169, 184, 172, 95, 104, 137, 183, 160,
131, 188, 98, 113, 88, 91, 127, 123, 95, 183, 137, 75, 72, 113, 75,
127, 128, 142, 196, 115, 131, 70]

sokolates2 = [134, 160, 178, 97, 86, 79, 88, 176, 107, 146, 179, 115, 149, 139, 192, 188, 100, 167,
191, 184, 194, 95, 120, 107, 85, 118, 84, 181, 120, 159, 81,131, 136, 189, 117, 153, 121, 
155, 123, 165, 199, 98, 198, 143, 177, 110, 76, 94, 147, 126, 82, 72, 112, 138, 121, 147,
151, 185, 87, 134, 146, 75,180, 200, 160, 146, 142, 94, 178, 134, 164, 146, 162, 143, 104,
121, 102, 164, 143, 123, 102, 112, 129, 71, 142, 187, 195, 198, 164, 132, 137, 164,138, 96, 
138, 101, 177, 189, 123, 166]

sokolates3 = [147, 161, 156, 100, 103, 196, 76, 150, 122, 183, 116, 193, 162, 107, 177, 157, 177, 116, 181, 89, 96, 134, 98,
159, 155, 150, 92, 106, 108, 172, 183, 160, 78, 102, 89, 107, 157, 198, 82, 109, 77, 164, 97, 190, 112, 103, 76,
164, 178, 152, 128, 123, 143, 145, 195, 77, 177, 83, 85, 75, 117, 126, 85, 76, 185, 116, 173, 137, 197, 142, 74,
138, 134, 153, 173, 177, 78, 131, 115, 168, 78, 161, 109, 150, 97, 109, 107, 181, 196, 153, 104, 178, 113, 76,
135, 174, 166, 106, 108, 166]




kerdos = 0
def find_faulty(sokolates):
    faulty =[]
    for soko in sokolates:
        if soko <90 or soko>170:
           faulty.append(soko)

    return len(faulty),faulty


def find_ticket(sokolates):
    ticket = []
    for soko in sokolates:
        if soko>150 and soko<=170:
            ticket.append(soko)

    ticket.sort(reverse = True)
    return ticket

def find_good(sokolates):
    good=[]
    for soko in sokolates:
        if soko >=90 and soko<=150:
           good.append(soko)

    kerdos = len(good)*1.50
    a = f"Το κέρδος απότις σοκολάτες που είναι για την βιτρίνα {kerdos}"
    return kerdos,good


def organize(faulty, good, ticket):
    dict = {
        'faulty' : faulty,
        'good' : good,
        'ticket' : ticket
        }
    return dict


#sokolates1
faulty1 = find_faulty(sokolates1)
ticket1 = find_ticket(sokolates1)
good1 = find_good(sokolates1)
organized1 = organize(faulty1[1],  good1[1], ticket1)

#sokolates2
faulty2 = find_faulty(sokolates2)
ticket2 = find_ticket(sokolates2)
good2 = find_good(sokolates2)
organized2 = organize(faulty2[1],  good2[1], ticket2)

#sokolates3
faulty3 = find_faulty(sokolates3)
ticket3 = find_ticket(sokolates3)
good3 = find_good(sokolates3)
organized3 = organize(faulty3[1],  good3[1], ticket3)




