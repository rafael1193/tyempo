# -*- coding: utf-8 -*-

import xml.etree.ElementTree
from datetime import datetime
import locale

class Lugar:     
    def __init__(self, xmltext):
        self._rawxml = xmltext
        #self._printsource()
        self.dias = []
        self._obtenerdatos(xml.etree.ElementTree.fromstring(xmltext))
        

    def MostrarPrediccion(self, index):
        locale.setlocale(locale.LC_TIME, '')
        
        if index is None:
            for dia in self.dias:
                print "=================================="
                print dia.fecha.strftime("%A, %d de %B de %Y")
                print "----------------------------------"
                
                print "Temperatura:"
                print """    Minima: """ + dia.pred_temp_extr["minima"] + """ºC    Maxima: """ + dia.pred_temp_extr["maxima"] + "ºC"
                
                print "Probabilidad de lluvia: "
                for lluv in dia.pred_lluvia:
                    print """    """ + str(lluv.periodo) + " : " + str(lluv.probabilidad) + " %"
                
                print "Cota de nieve:"
                for niev in dia.pred_nieve:
                    if niev.cota is None:
                        print """    """ + str(niev.periodo) + " : ninguna"
                    else:
                        print """    """ + str(niev.periodo) + " : " + str(niev.cota) + " m"
                
                print ""
        else:
            dia = self.dias[index]
            print "=================================="
            print dia.fecha.strftime("%A, %d de %B de %Y")
            print "----------------------------------"
            
            print "Temperatura:"
            print """    Minima: """ + dia.pred_temp_extr["minima"] + """ºC    Maxima: """ + dia.pred_temp_extr["maxima"] + "ºC"
            
            print "Probabilidad de lluvia: "
            for lluv in dia.pred_lluvia:
                print """    """ + str(lluv.periodo) + " : " + str(lluv.probabilidad) + " %"
            
            print "Cota de nieve:"
            for niev in dia.pred_nieve:
                if niev.cota is None:
                    print """    """ + str(niev.periodo) + " : ninguna"
                else:
                    print """    """ + str(niev.periodo) + " : " + str(niev.cota) + " m"
            
            print ""

    def _obtenerdatos(self, xmlElTree):
        self.nombre = xmlElTree.find("nombre").text
        self.provincia = xmlElTree.find("provincia").text
        diasxml = xmlElTree.find("prediccion").findall("dia")
        self.dias = []
        for diaxml in diasxml:
            d = Dia(diaxml.get("fecha")) 
            
            #lluvia
            for per in diaxml.findall("prob_precipitacion"):
                intervalo = per.get("periodo")
                if intervalo is None:
                    intervalo = "00-24"
                idSimb = ""
                for est in diaxml.findall("estado_cielo"):
                    if est.get("periodo") == intervalo:
                        idSimb = est.text
                d.pred_lluvia.append(Lluvia(intervalo, per.text, idSimb))
                
            #nieve
            for per in diaxml.findall("cota_nieve_prov"):
                intervalo = per.get("periodo")
                if intervalo is None:
                    intervalo = "00-24"
                idSimb = ""
                for est in diaxml.findall("estado_cielo"):
                    if est.get("periodo") == intervalo:
                        idSimb = est.text
                d.pred_nieve.append(Nieve(intervalo, per.text, idSimb))
                
            #temperatura
            tempxml = diaxml.find("temperatura")
            d.pred_temp_extr["minima"] = tempxml.find("minima").text
            d.pred_temp_extr["maxima"] = tempxml.find("maxima").text
            
            #anadir a la lista el nuevo dia
            self.dias.append(d)
        
    def _printsource(self):
        print "----------------------------------------"
        print self._rawxml
        print "----------------------------------------"


class Dia:
    def __init__(self, fecha):
        self.fecha = datetime.strptime(fecha, "%Y-%m-%d")
        self.pred_lluvia = []
        self.pred_nieve = []
        self.pred_temp = []
        self.pred_temp_extr = {}
        pass


class Temperatura:
    def __init__(self, periodo, prob): 
        self.periodo = periodo
        self.probabilidad = prob


class Lluvia:
   
    def __init__(self, periodo, prob, idSimb): 
        self.idSimbolo = idSimb
        self.periodo = periodo
        self.probabilidad = prob

       
class Nieve:
    def __init__(self, periodo, cota, idSimb):
        self.idSimbolo = idSimb
        self.periodo = periodo
        self.cota = cota
