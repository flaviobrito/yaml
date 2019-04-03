#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 19:38:54 2019
Code to dump and load instances of a Class using YAML
@author: flaviobrito
"""

#Imports 
import sys
import ruamel.yaml

# Dataflow Class
class Dataflow(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.yarn_pool = YarnPool().yarn_pool

# YarnPool Class
class YarnPool(object):
    def __init__(self):
        self.yarn_pool = {'name':'pool_80',
                          'pool':'80'}, \
                          {'name':'pool_60',
                          'pool':'60'}

# IInstantiate an object of type Dataflow with values       
obj = Dataflow('BI_Dataflow', 'Business Intelligence Dataflow')

#create Yaml object
yaml = ruamel.yaml.YAML()

#Register Class 
yaml.register_class(Dataflow)

# Print Dataflow object to stdout
yaml.dump(obj, sys.stdout)

# Serialize Dataflow object to yaml file
with open('metadata.yaml', 'w') as yaml_file:
        yaml.dump(obj, yaml_file)
        
# Read Dataflow object from yaml file         
with open("metadata.yaml", 'r') as yaml_file:
    try:
        dtf = yaml.load(yaml_file)
    except yaml.YAMLError as exc:
        print(exc)        