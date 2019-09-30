import requests
from tkinter import *
from webbrowser import open
from os import path

def writeHTML():
    ofile = open("deleteme.html","w")
    ofile.write("<h1>" + datajson['city'] + "</h1>")
    ofile.write("<p>" + datajson['country'] + "</p>")
    ofile.write("<link rel='stylesheet' href='https://unpkg.com/leaflet@1.4.0/dist/leaflet.css'/>")
    ofile.write("<script src='https://unpkg.com/leaflet@1.4.0/dist/leaflet.js'></script>")
    ofile.write("<div id='map' style='width:100%; height:500'></div>")
    ofile.write("<script>")
    ofile.write("map = new L.Map('map');")
    ofile.write("osmUrl='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';")
    ofile.write("osmAttrib='OpenStreetMap';")
    ofile.write("osm = new L.TileLayer(osmUrl, {minZoom: 8, maxZoom: 20, attribution: osmAttrib});")
    ofile.write("map.setView(new L.LatLng(43,-79),13);")
    ofile.write("map.addLayer(osm);")
    ofile.write("</script>")
    ofile.write("")
    ofile.close()

def getAPI():
    myrequest  = requests.get("https://geo-info.co/43,-79")
    datajson = myrequest.json()
    b2 = Button(win,text="complete - view your file",command=open('file://' + path.realpath('deleteme.html')))
    b2.grid(row=1,column=0)
    

win = Tk()
b1 = Button(win,text="click me",command=getAPI)
b1.grid(row=0,column=0)
