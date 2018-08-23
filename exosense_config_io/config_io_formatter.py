#!/usr/bin/env python3
import json
import datetime
import os

class Formatter:

    def __init__(self, channels):
        self.channels = channels

    @property
    def channelsConfig(self):
        return self.channels

    @channelsConfig.setter
    def channelsConfig(self, channels):
        self.channels = channels

    def saveFile(self, filename):
        with open(filename, 'w') as f:
            f.write(json.dumps(self.channels))
    
    def __str__(self):
        return json.dumps(self.channels)

class DataConfig:

    def __init__(self):
        self.configContent = {}
    
    def loadConfig(self, filePath):
        with open(filePath, 'r') as f:
            self.configContent = json.load(f)

    @property
    def config(self):
        return self.configContent

def handle_data_type(dataConfig):   
    typeList=[]
    index=0
    for t in dataConfig['type']:
        for k in t:
            print("{}. {}".format(index,k))
            index+=1
            typeList.append(k)

    while True:
        sel = int(input('select one of the above data type by index:'))
        try:
            return typeList[sel]    
        except:
            print("please select right index!!!")

def handle_data_unit(dataConfig, dataType):
    for t in dataConfig['type']:
        for k,v in t.items():
            if k == dataType:
                if v != None:
                    print("Possible unit:\n{}".format("\n".join(v)))
    
    return input('data unit(optional, enter to leave empty to ignore it):')



def get_channels_setting(dataConfig):
    channels = {}
    channels['last_edited']=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    channels['last_editor']='device'
    channels['meta'] = {'description':'create the config file by the Python script'}

    channelsVal = {}
    yesFormat = {'yes','y','ye'}
    while True:
        channelName = input('channel name:')
        channelVal = {}
        channelVal['display_name'] = input('display name:')
        channelVal['description'] = input('description:')
        properties = {}

        properties['data_type'] = handle_data_type(dataConfig)

        unit = handle_data_unit(dataConfig, properties['data_type'])

        if not unit == "":
            properties['data_unit'] = unit

        properties['min'] = int(input('min:'))
        properties['max'] = int(input('max:'))
        properties['percision'] = int(input('percision:'))

        channelVal['properties'] = properties

        #protocolConfig = {}

        #applicatoin = input("application(enter to leave empty to ignore the setting):")

        #if applicatoin !="":
            
        channelsVal[channelName] = channelVal

        isContinue = input('Do you have more channels(yes/NO)?').lower()
        if not isContinue in yesFormat:
            break
        else:
            os.system('clear')
        
        print(channelsVal)

    channels['channels'] = channelsVal

    return channels

if __name__ == '__main__':
    os.system('clear')
    dataConfig = DataConfig()
    dataConfig.loadConfig('data_type.json')
    formatter = Formatter(get_channels_setting(dataConfig.config))
    print(formatter)
    formatter.saveFile(input('Output filename:'))