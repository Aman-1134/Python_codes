cities = {}
cities = {
    'Kathmandu': {

     'City of temples':  {'Capital of nepal': 'Never been slave'},
    },
    'Dhaka': {
        'Rich in natural beauty':' Capital of Bhutan',
    },
    'Islamabad': {
        'Islam religion place':'Capital of Pakistan',
    },
    'New Delhi': {
        'Modi is the prime minister':'Capital of India',
                      },
    'Cairo':      'Capital of Egypt',
    'Prince au port': 'Capital of haiti',
    'Washingon':     'Capital of US',
}

#cities['pohkara']='not a captal city'
#cities['Kathmandu']['polluted'] = 'dhulo'
#for i,j in cities.items():
#    print('{} : {}'.format(i,j))

#print(cities['Kathmandu']['City of temples'])


cities.update({'India': 'In south East Asia'})
#print(cities.get('Kathmandu'))
#print(cities.get('India'))
cities.pop('India')
for i in sorted(cities):
    print(i, ':', cities[i])
