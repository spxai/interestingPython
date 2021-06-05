#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#2-8-3-1.py
import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("hello,world")],     # Part 2 - The Layout
            [sg.Text("你好，世界")],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('hello world', layout)      # Part 3 - Window Defintion


# Display and interact with the Window
event, values  = window.read()                   # Part 4 - Event loop or Window.read call


# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window