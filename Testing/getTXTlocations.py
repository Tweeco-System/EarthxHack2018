import json
from geopy.geocoders import Nominatim
geolocator = Nominatim()

tweetLocations = []
'''
with open('OUTPUTgetSearchData.json') as jsonFile:
    data = json.load(jsonFile)
    for info in data['tweets']:
        tweetLocations+=[[info['text'], info['location']]]     

def getCoordinates(tweetsList):
    coorList = []
    for tweet in tweetLocations:

        try:
            #print('inside try')
            results = [geolocator.geocode(tweet[1]).latitude, geolocator.geocode(tweet[1]).longitude]
            coorList += [[results[0], results[1], tweet[0]]]
            #print(coorList)
        except:
            #print('inside exception')
            print()  

    return coorList

coors = getCoordinates(tweetLocations)
print(coors)

data = {}
data['tweets'] = []


for tweet in coors:
    data['tweets'].append({
        'text': coors[2],
        'latitude' : coors[0],
        'longitude' : coors[1]
    })

    
with open('OUTPUTcoordinates.json', 'w') as outfile:
    json.dump(data, outfile)
'''

def getCoorsFunc():
    tweetLocations = []
    
    with open('OUTPUTgetSearchData.json') as jsonFile:
        data = json.load(jsonFile)
        for info in data['tweets']:
            tweetLocations+=[[info['text'], info['location']]]     
    
    def getCoordinates(tweetsList):
        coorList = []
        for tweet in tweetLocations:
    
            try:
                #print('inside try')
                results = [geolocator.geocode(tweet[1]).latitude, geolocator.geocode(tweet[1]).longitude]
                coorList += [[results[0], results[1], tweet[0]]]
                print(coorList[-1])
            except:
                #print('inside exception')
                print()  
    
        return coorList
    
    coors = getCoordinates(tweetLocations)
    #print(coors)
    
    data = {}
    data['tweets'] = []
    
    
    for tweet in coors:
        data['tweets'].append({
            'text': coors[2],
            'latitude' : coors[0],
            'longitude' : coors[1]
        })
    
        
    with open('OUTPUTcoordinates.json', 'w') as outfile:
        json.dump(data, outfile)
    
