# -*- coding: utf-8 -*-
import xml.etree.ElementTree
import urllib
from gi.repository import Gtk

from predicciones import Lugar

class GUI(Gtk.Window):
    simb = {"0" : "dialog-error" ,        
            "11" : "weather-clear", "11n" : "weather-clear-night", 
            "12" : "weather-few-clouds", "12n" : "weather-few-clouds-night",
            "13" : "weather-few-clouds", "13n" : "weather-few-clouds-night",
            "14" : "weather-overcast", "14n" : "weather-overcast",
            "15" : "weather-overcast", "15n" : "weather-overcast",
            "16" : "weather-overcast", "16n" : "weather-overcast",
            "17" : "weather-few-clouds", "17n" : "weather-few-clouds-night",
            "23" : "weather-showers-scattered", "23n" : "weather-showers-scattered", 
            "43":"weather-showers-scattered", "43n":"weather-showers-scattered",
            "45" : "weather-showers-scattered", "45n" : "weather-showers-scattered",
            "46" : "weather-showers-scattered", "46n" : "weather-showers-scattered"}
    
    def __init__(self, lugar):
        Gtk.Window.__init__(self, title = "Tyempo 0.1")
        
        builder = Gtk.Builder()
        builder.add_from_file("gui.glade")
        
        #nombre ciudad
        self.labelCiudad = builder.get_object("labelCiudad")
        self.labelCiudad.set_text(lugar.nombre)
        
        #prob precipitacion por dias
        self.labelprob = builder.get_object("labelProbHoy12")
        self.labelprob.set_text(lugar.dias[0].pred_lluvia[0].probabilidad + " %")
        self.labelprob = builder.get_object("labelProbHoy24")
        self.labelprob.set_text(lugar.dias[0].pred_lluvia[1].probabilidad + " %")
        
        self.labelprob = builder.get_object("labelProbManana12")
        self.labelprob.set_text(lugar.dias[1].pred_lluvia[0].probabilidad + " %")
        self.labelprob = builder.get_object("labelProbManana24")
        self.labelprob.set_text(lugar.dias[1].pred_lluvia[1].probabilidad + " %")
        
        self.labelprob = builder.get_object("labelProbPasado12")
        self.labelprob.set_text(lugar.dias[2].pred_lluvia[0].probabilidad + " %")
        self.labelprob = builder.get_object("labelProbPasado24")
        self.labelprob.set_text(lugar.dias[2].pred_lluvia[1].probabilidad + " %")
        
        #simb precipitacion por dias
        self.image = builder.get_object("imageHoy12")
        self.image.set_from_icon_name  (GUI.simb[lugar.dias[0].pred_lluvia[0].idSimbolo], 48)
        self.image = builder.get_object("imageHoy24")
        self.image.set_from_icon_name  (GUI.simb[lugar.dias[0].pred_lluvia[1].idSimbolo], 48)
        
        self.image = builder.get_object("imageManana12")
        self.image.set_from_icon_name  (GUI.simb[lugar.dias[1].pred_lluvia[0].idSimbolo], 48)
        self.image = builder.get_object("imageManana24")
        self.image.set_from_icon_name  (GUI.simb[lugar.dias[1].pred_lluvia[1].idSimbolo], 48)
        
        self.image = builder.get_object("imagePasado12")
        self.image.set_from_icon_name  (GUI.simb[lugar.dias[2].pred_lluvia[0].idSimbolo], 48)
        self.image = builder.get_object("imagePasado24")
        self.image.set_from_icon_name  (GUI.simb[lugar.dias[2].pred_lluvia[1].idSimbolo], 48)
        
        #temperatura por dias
        self.labelprob = builder.get_object("labelTempHoyMin")
        self.labelprob.set_text(lugar.dias[0].pred_temp_extr["minima"] + " ºC")
        self.labelprob = builder.get_object("labelTempHoyMax")
        self.labelprob.set_text(lugar.dias[0].pred_temp_extr["maxima"] + " ºC")
        
        self.labelprob = builder.get_object("labelTempMananaMin")
        self.labelprob.set_text(lugar.dias[1].pred_temp_extr["minima"] + " ºC")
        self.labelprob = builder.get_object("labelTempMananaMax")
        self.labelprob.set_text(lugar.dias[1].pred_temp_extr["maxima"] + " ºC")
        
        self.labelprob = builder.get_object("labelTempPasadoMin")
        self.labelprob.set_text(lugar.dias[2].pred_temp_extr["minima"] + " ºC")
        self.labelprob = builder.get_object("labelTempPasadoMax")
        self.labelprob.set_text(lugar.dias[2].pred_temp_extr["maxima"] + " ºC")
        
        window = builder.get_object("gui")
        window.show_all()
        
#        grid = Gtk.Grid()
#        self.add(grid)
#        
#        self.titulo = Gtk.Label(label ="Tyempo 0.1")
#        
#        self.buttonHoy = Gtk.Button(label = "Hoy")
#        self.buttonHoy.connect("clicked", self.on_button_clicked, "hoy")
#        self.buttonManana = Gtk.Button(label = "Mañana")
#        self.buttonManana.connect("clicked", self.on_button_clicked, "manana")
#        self.buttonPasado = Gtk.Button(label = "Pasado mañana")
#        self.buttonPasado.connect("clicked", self.on_button_clicked, "pasado")
#        
#        grid.attach(self.titulo,0,0,3,1)
#        grid.attach(self.buttonHoy,0,1,1,1)
#        grid.attach(self.buttonManana,1,1,1,1)
#        grid.attach(self.buttonPasado,2,1,1,1)
#        
#        self.diaCell = Gtk.VBox() #Sec titulo
#        self.tituloDiaCell = Gtk.Label(label="Hoy")
#        self.diaCell.pack_start(self.tituloDiaCell,True,True,0)
#        
#        self.contDiaCell = Gtk.VBox() #Sec contenido
#        self.diaCell.pack_end(self.contDiaCell,True,True,0)
#        
#        self.precipContDiaCell = Gtk.HBox(True,10) #Sec precipitaciones
#        
#        self.periodoPrecipContDiaCell = [Gtk.VBox(),Gtk.VBox()] #Sec periodos concretos del dia
#        
#        #periodo 0-12
#        self.periodoPrecipContDiaCell[0].pack_start(Gtk.Label(lugar.dias[0].pred_lluvia[0].periodo + " h"),True,True,0)
#        self.periodoPrecipContDiaCell[0].pack_start(Gtk.Image.new_from_file("weather_rain.png"),True,True,0)
#        self.periodoPrecipContDiaCell[0].pack_start(Gtk.Label(lugar.dias[0].pred_lluvia[0].probabilidad + " %"),True,True,0)
#        
#        #periodo 12-24
#        self.periodoPrecipContDiaCell[1].pack_start(Gtk.Label(lugar.dias[0].pred_lluvia[1].periodo + " h"),True,True,0)
#        self.periodoPrecipContDiaCell[1].pack_start(Gtk.Image.new_from_file("weather_snow.png"),True,True,0)
#        self.periodoPrecipContDiaCell[1].pack_start(Gtk.Label(lugar.dias[0].pred_lluvia[1].probabilidad + " %"),True,True,0)
#        
#        self.precipContDiaCell.pack_start(self.periodoPrecipContDiaCell[0],True,True,0)
#        self.precipContDiaCell.pack_start(self.periodoPrecipContDiaCell[1],True,True,0)
#        
#        self.contDiaCell.pack_end(self.precipContDiaCell,True,True,0)
#        
#        grid.attach(self.diaCell,0,2,1,1)
        
#        self.button = Gtk.Button(label="Ver prediccion")
#        self.button.connect("clicked", self.on_button_clicked)
#        self.add(self.button)



