# Write a program with a class definition called 'UAV'.  The constructor should take in
# arguments for latitude, longitude, altitude, speed, and heading.  These data items 
# should be placed in a dictionary inside the object.  The class must also have a
# method called 'printUAV', which prints out the contents of the object.

# A main program section must create a list of three UAV objects, prompting the user for
# the arguments listed above for each aircraft.  The main section then needs to 
# iterate through the list of UAV objects, calling printUAV for each one of them in turn.

class UAV:
    def __init__(self):
        '''These data items should be placed in a dictionary inside the object.'''
        # self.data_dict = {(0,1,2):(3, 4)}

    def flying_object(self, latitude, longitude, altitude, speed, heading):
        self.__dict__.update({(latitude, longitude, altitude):(speed, heading)})

    def printUAV(self):
        print(self.__dict__)

#instantiate the class
uav = UAV()
# print(uav.__repr__)#no representation of the print out needed, I think
print('press ctrl+c to exit anytime')#user handling

while True:
    prompt = input('Would you like to VIEW the UAVs or enter the data for a NEW input? enter: VIEW or NEW or exit ')#sort of error handling
    if prompt == 'NEW':
        '''sorry no error handling, thinking on the fly here'''
        lat = input('please enter latitude: ')    
        long = input('please enter longitude: ')
        alt = input('please enter altitude: ')
        spd =input('please enter speed: ')
        heading_1 = input('please enter heading: ')
        uav.flying_object(lat, long, alt, spd, heading_1)
    elif prompt == 'VIEW':
        uav.printUAV()
    elif prompt == 'exit':
        break
    else:
        print('Command not recognized ')