# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 12:10:00 2024

"""
#//import
#import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
#//widgets
from kivy.uix.label import Label
from kivy.uix.button import Button


#//Main
class CounterApp(App):
    def build(self):
        
        self.count = 0
        
        self.window = GridLayout()
        self.window.cols = 1
        
        #//add widgets   
        #label
        self.greeting = Label(text="0", font_size=72)
        self.window.add_widget(self.greeting)
        
        self.button = Button(text="ADD")
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        return self.window
    
    def callback(self, instance):
        self.count += 1
        self.greeting.text = "" + str(self.count) + ""
        
#//Run    
CounterApp().run()