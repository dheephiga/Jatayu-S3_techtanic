import random
import datetime as dt
import json
import fun


class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (dt.date, dt.time)):
            return obj.isoformat()
        return super().default(obj)


program = []
t = dt.datetime(2023, 1, 1, 0, 0, 0)

id_counter = 1  # Initialize ID counter

end_time = None  # Initialize end_time variable
while t <= dt.datetime(2023, 1, 7, 0, 0, 0):
    program.append({
        'id': id_counter,  # Set 'id' using the ID counter
        'channel_id': '',
        'channel_name': '',
        'channel_genre': '',
        'type': '' if id_counter % 5 == 1 else '',
        'category': None,
        'name': None,
        'date': dt.datetime.strptime(t.strftime("%d-%m-%y"), "%d-%m-%y").date(),
        'start_time': end_time.strftime('%H:%M:%S') if end_time else t.strftime('%H:%M:%S'),
        'end_time': None,
        'program_duration': None,
        'region': [],  # Initialize region as a list
        'time_category': fun.tcategory(t),
        'premium': None
    })
    program[-1]['category'] = fun.cat(program[-1]['type'])
    program[-1]['name'] = fun.name(program[-1]['category'])
    program[-1]['program_duration'] = fun.duration(program[-1]['type'])
    program[-1]['end_time'] = dt.datetime.combine(program[-1]['date'], dt.datetime.strptime(program[-1]['start_time'],
                                                                                            "%H:%M:%S").time()) + dt.timedelta(
        minutes=program[-1]['program_duration'])
    program[-1]['end_time'] = program[-1]['end_time'].time()

    id_counter += 1  # Increment the ID counter

    end_time = program[-1]['end_time']  # Set end_time for the next program
    program[-1]['premium'] = fun.premium(program[-1]['type'])


    # Add all the states in America to the region key of the specific program
    for state in ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                  'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                  'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                  'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico',
                  'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                  'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
                  'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']:
        maximum = random.randint(1, 40)
        minimum = random.randint(1, maximum)
        avg = (maximum + minimum) / 2

        program[-1]['region'].append({
            'state': state,
            'max_viewership': maximum,
            'min_viewership': minimum,
            'avg_viewership': avg,
        })
    t = fun.totaltime(t,program[-1]['program_duration'])

# Write the dictionary to a JSON file using the custom encoder
with open('news.json', 'w') as f:
    json.dump(program, f, indent=4, cls=CustomEncoder)