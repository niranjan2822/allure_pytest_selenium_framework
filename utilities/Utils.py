import configparser
import os


def readconfigdata(section, key):
    cfg_filename = os.path.join(os.path.dirname(__file__), '..', 'resources', 'config.cfg')
    cp = configparser.RawConfigParser()
    cp.read(cfg_filename)
    return cp.get(section, key)

