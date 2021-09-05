# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 23:08:53 2020

@author: DELL
"""

import requests
import pprint

endpoint = "http://127.0.0.1:5000/Citation"

req = requests.get(endpoint)

pprint.pprint(req.json())