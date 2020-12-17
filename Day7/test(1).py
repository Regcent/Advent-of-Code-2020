# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 09:07:03 2020

@author: VAH1SO
"""

import re
import time



with open('input.txt','r') as file:
    data = file.read()
    
t = time.time()
d = {}
for line in data.split('\n'):
    baginfo, bagcontent = line.split('contain')    
    bagcolor = baginfo.split(' bag')[0]
    
    elements = []
    for bag in bagcontent.split(','):        
        infos = bag.split(' bag')[0].split(' ')        
        nb = infos[1]
        b = ' '.join(infos[2:])
        elements.append((nb,b))
            
    d[bagcolor] = elements
    

def count_number(color):
    
    elements = d[color]
    
    total = 1
    for e in elements:
        
        (number, bag) = e
        if number=='no':
            break
        
        number = int(number)
        total += number * count_number(bag)
    
    return total
    

print(count_number('shiny gold')-1)

print(time.time()-t)