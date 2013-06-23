#!/usr/bin/python

#Copyright (C) Nial Peters 2013
#
#This file is part of AvoPlot.
#
#AvoPlot is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#AvoPlot is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with AvoPlot.  If not, see <http://www.gnu.org/licenses/>.

"""
This module contains the main script for running AvoPlot.
"""

import wx
import optparse
import warnings

import avoplot
import avoplot.plugins
from avoplot.gui import artwork, main

def __parse_cmd_line():
    """
    Function parses the command line input and returns a tuple 
    of (options, args).
    """
    usage = ("Usage: %prog [options]")
        
    parser = optparse.OptionParser(usage)

    (options, args) = parser.parse_args()

    return (options, args)



def display_warning(message, category, filename, *args):
    """
    Displays a warning message in a wx.MessageBox. This is designed to 
    override the warnings module's show_warning function.
    """
    wx.MessageBox(str(message), avoplot.PROG_SHORT_NAME, wx.ICON_ERROR)



if __name__ == '__main__':
    
    #parse any command line args
    options, args = __parse_cmd_line()
        
    app = wx.PySimpleApp()
    
    #setup warnings module to display messages in a wx.MessageBox
    warnings.showwarning = display_warning
    
    #register our art provider to serve the AvoPlot icons
    wx.ArtProvider.Insert(artwork.AvoplotArtProvider())
    
    #load all available plugins
    avoplot.plugins.load_all_plugins()
    
    #launch the GUI!
    main.MainFrame()
       
    app.MainLoop()
