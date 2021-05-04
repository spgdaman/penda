import pandas as pd
import csv
import os
from io import BytesIO
from datetime import datetime
from .models import CallLogs

path = 'callcenter/RawData.csv'
path2 = 'callcenter/CallVolumes.csv'

class DataEntry:
    '''
        This is where the object will be created!
    '''

    path = 'callcenter/RawData.csv'
    path2 = 'callcenter/CallVolumes.csv'

    def __init__(self, calltime, callerid, destination, status, ringing, talking, reason, totals):
        self.calltime = calltime
        self.callerid = callerid
        self.destination = destination
        self.status = status
        self.ringing = ringing
        self.talking = talking
        self.reason = reason
        self.totals = totals

def call_volumes_cleanup(file):

    collection = []
    with open(path2,'w+', newline='') as cdr2:
        data2 = csv.writer(cdr2, delimiter=',')

        with open(path) as cdr:
            data = csv.reader(cdr)
            for data in data:
                collection.append(data)

        counter = 0

        for items in collection:
            if items[0] != '':
                data2.writerow(items)
                counter += 1
            elif items[0] == '': # Fills in the gaps with dates from row above it
                #item = items
                items[0] = collection[counter-1][0]
                data2.writerow(items)
                # print(items[0])
                counter += 1


def read_raw_data(file):

    # writing the uploaded data to RawData.csv
    data = open(path,"w+")
    write = data.write(file)
    data.close()

    data = pd.read_csv(path)
    data = pd.DataFrame(data)
    col_header = data.iloc[4] # get column header
    data = data[5:] # select data body
    data = data.rename(columns=col_header) # rename data columns
    data = data.iloc[:-2] # remove bottom 2 rows

    # Delete unnecessary columns
    del data['Cost'] # delete cost column
    data.dropna() #drop empty columns
    data = data[['Call Time', 'Caller ID','Destination', 'Status', 'Ringing', 'Talking', 'Totals', 'Reason', 'Play']] # replace columns
    del data['Totals'] #delete totals column
    data.rename(columns = {'Play': 'Totals'}, inplace=True) # rename play column
    # print(data[['Destination','Status','Ringing','Talking']])
    data['Caller ID'] = data['Caller ID'].apply(str) 

    ###################################################

    df_items = [x for x in data['Caller ID']]
    df_items_2 = [x for x in data['Destination']]
    new_df_items = list()
    new_df_items_2 = list()

    for items in df_items:
        if items[0] == '2':
            items = '+' + items
            new_df_items.append(items)
        elif items[0] == '7':
            items = '+254' + items
            new_df_items.append(items)
        elif items[0] == '1':
            items = '+254' + items
            new_df_items_2.append(items)
        else:
            new_df_items.append(items)

    for items in df_items_2:
        if items[0] == '2':
            items = '+' + items
            new_df_items_2.append(items)
        elif items[0] == '7':
            items = '+254' + items
            new_df_items_2.append(items)
        elif items[0] == '1':
            items = '+254' + items
            new_df_items_2.append(items)
        else:
            new_df_items_2.append(items)

    data['Caller ID'] = new_df_items
    data['Destination'] = new_df_items_2

    #########################

    data.to_csv(path, index=False)

    collection = []
    with open(path2,'w+', newline='') as cdr2:
        data2 = csv.writer(cdr2, delimiter=',')

        with open(path) as cdr:
            data = csv.reader(cdr)
            for data in data:
                collection.append(data)

        counter = 0

        for items in collection:
            if items[0] != '':
                data2.writerow(items)
                counter += 1
            elif items[0] == '': # Fills in the gaps with dates from row above it
                #item = items
                items[0] = collection[counter-1][0]
                data2.writerow(items)
                # print(items[0])
                counter += 1


    data = pd.read_csv(path2)
    data2 = data['Call Time']
    data2['CallTime'] =data2
    # data2['CallTime'] = data2.to_string()
    # print(data2.head())
    data2 = data2['CallTime'].str.split(' ', expand=True)
    data2['Date'] = data2[0]
    data2['Time'] = data2[1]
    data2['AM/PM'] = data2[2]
    del data2[0]
    del data2[1]
    del data2[2]

    data2['Date'].to_string()
    data2.dropna()
    print(data2['Date'])

    standard_dates = []

    # for dates in data2['Date']:
    #     if dates[4:5] == "-":
    #         new_dates = f"{dates[9:10]}/{dates[5:7]}/{dates[:4]}"
    #         standard_dates.append(new_dates)
    #     else:
    #         new_dates = f"{dates}"
    #         standard_dates.append(new_dates)
    
    # data2['Date'] = standard_dates

    standard_time = []

    for i in data2['Time']:
        str(i)
    
    zipped = zip(data2['Time'],data2["AM/PM"])
    
    for times, meridiem in zipped:
        suffixes = datetime.strptime(times,"%H:%M:%S").strftime("%I:%M:%S %p")[-2:]
        if meridiem == None:
            new_time = datetime.strptime(times,"%H:%M:%S").strftime("%I:%M:%S %p")
            standard_time.append(new_time)
        else:
            new_time = times + " " + meridiem
            standard_time.append(new_time)

    data2['Time'] = standard_time
    print(data2['Time'])
    
    collection = []

    with open(path2) as cleaned_data:
        clean = csv.reader(cleaned_data)
        for line in clean:
            collection.append(line)

    

    ########################################

    # collection = collection[1:]
    # objects = []
    # # data_entry = DataEntry()

    # for items in collection:
    #     obj = CallLogs(call_time=items[0], caller_id=items[1], destination=items[2], status=items[3], ringing=items[4], talking=items[5], reason=items[6], totals=items[7])
    #     obj.save()
    #     objects.append(obj)

    # for i in objects:
    #     print(i.callerid)
 