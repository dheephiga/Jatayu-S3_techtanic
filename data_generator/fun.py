import datetime
import random

#calculate Time category
def tcategory(t):
    stime = t.time()
    if stime.hour in range(0, 1):
        return 'Late Fringe'
    elif stime.hour in range(1, 2):
        return 'Post Late Fringe'
    elif stime.hour in range(2, 6):
        return 'Overnight'
    elif stime.hour in range(6, 10):
        return 'Early Morning'
    elif stime.hour in range(10, 16):
        return 'Daytime'
    elif stime.hour in range(16, 18):
        return 'Early Fringe'
    elif stime.hour in range(18, 23):
        return 'Prime Time'
    elif stime.hour == 23:
        return 'Late News'
#calculate total time
def totaltime(t,dur):
    tchange = datetime.timedelta(minutes=dur)
    t = t + tchange
    return t

#set duration
def duration(typ):
    if typ == 'AD':
        dur = random.choices([.45,.60])
        return dur[0]
    elif typ == 'On Demand':
        return 23
    elif typ == 'Live':
        return 60

#set category
def cat(typ):
    if typ == 'AD':
        c = random.choice(['telecom','pharma','food'])
        return c
    else:
        c = 'program'
        return c

#set name
def name(typ):
    if typ == 'telecom':
        n = random.choice(['AT&T','Verizon'])
        return n
    elif typ == 'pharma':
        n = random.choice(['Vicks Vaporub','AccuCheck','Xarelto'])
        return n
    elif typ == 'food':
        n = random.choice(['Jello','Chocos','Yoghurt','Snickers'])
        return n
    elif typ == 'program':
        n = random.choice(['Weather', 'Politics', 'Headlines', 'Economics'])
        return n

#assign same id for names
def assign_same_id_for_name(program):
    name_ids = {}
    for entry in program:
        if entry['type']=='AD':
            name = entry['name']
            if name in name_ids:
                entry['id'] = name_ids[name]
            else:
                name_ids[name] = entry['id']
    return program

def premium(typ):
    if typ == 'AD':
        return random.choice([0,1])
    else:
        return 0