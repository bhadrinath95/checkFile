'''
Created on 02-Jul-2020

@author: BHADRINATH
'''
import os, time, configparser, csv, logging 

def checkForFile(dirName, outputfile):
    logging.debug(f'Checking files within folder {dirName}')
    listOfFile = os.listdir(dirName)
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            checkForFile(fullPath, outputfile)
        else:
            extension = os.path.splitext(entry)[1]
            outputfile.writerow([dirName,entry,extension,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(fullPath))),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(fullPath)))]) 
            logging.info(f'File {entry} found within folder {dirName}')
            
logging.basicConfig(filename=os.path.join(os.getcwd(),'reportLog.log'), format='%(asctime)s %(name)s %(levelname)s %(message)s', filemode='w') 
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
logger.info("Project checkfile execution is started") 
fields = ['Directory Path','File Name','Extension','Created Date','Modified Date']
config = configparser.RawConfigParser()
config.read(os.path.join(os.getcwd(),'config.properties'))
path = config.get('ConfigurationSection', 'directory.path');
if os.path.exists(os.path.join(config.get('ResultantSection', 'output.path'),config.get('ResultantSection', 'output.filename'))):
    os.remove(os.path.join(config.get('ResultantSection', 'output.path'),config.get('ResultantSection', 'output.filename')))
csvfile = open(os.path.join(config.get('ResultantSection', 'output.path'),config.get('ResultantSection', 'output.filename')), 'a', newline='')
outputfile = csv.writer(csvfile) 
outputfile.writerow(fields) 
checkForFile(path, outputfile)