#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:25:31 2021

@author: smahesh
"""

import izhikevich_cells as izh

class chatCell(izh.izhCell):
    """  chattering cell is a sub-class of izhCell"""
    def __init__(self, stimVal):
        super().__init__(stimVal)
        """these are the defined parameters for chattering cell"""
        self.celltype='Chattering'
        self.C = 50
        self.vr = -60
        self.vt = -40
        self.k = 1.5
        self.a = 0.03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25
        self.stimVal = stimVal
        
myCell = chatCell(4000)
myCell.simulate()

if __name__=='__main__':
    """if True, it calls the pltting function in izhikevich_cells"""
    izh.plotMyData(myCell)      