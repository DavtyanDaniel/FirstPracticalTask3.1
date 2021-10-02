import configparser

config = configparser.ConfigParser()
config.read('input.ini')
FILE_NAME = config['USER']['FileName']

try:
    RA = float(config['USER']['ra'])
    DEC = float(config['USER']['dec'])
    FOV_H = float(config['USER']['fov_h'])
    FOV_V = float(config['USER']['fov_v'])
    N = int(config['USER']['n'])

except ValueError as error:
    raise Exception('invalid variable' + str(error))

# column indexes in data file

RA_INDEX = 5
DEC_INDEX = 6
ID_INDEX = 7
MAG_INDEX = 22





