#! /usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Tyempo.
#
# Tyempo is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# any later version.
#
# Tyempo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Tyempo; If not, see <http://www.gnu.org/licenses/>.

import xml.etree.ElementTree
import urllib
from gi.repository import Gtk

from predicciones import Lugar
from gui import GUI

if __name__ == '__main__':
    print "Tyempo 0.1"
    print "(c) 2012, rafael1193"
    print "Este programa se encuentra bajo los terminos de la licencia GPLv3+"
    print ""
    
idLocalidad = "28079"
try:
    fil = open("idLocalidad", "r")
    idLocalidad = fil.readline()[:-1]
    fil.close()
    descargado = urllib.urlopen("http://www.aemet.es/xml/municipios/localidad_" + idLocalidad + ".xml").read()
    pueblo = Lugar(descargado)
    
    win = GUI(pueblo)
    win.connect("delete-event", Gtk.main_quit)
    Gtk.main()
except Exception, e:
    print "¡Error!"
