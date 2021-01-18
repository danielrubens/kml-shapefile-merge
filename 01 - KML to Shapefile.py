import os.path
from qgis._core import*
from qgis.gui import*
from PyQt5.QtCore import *
import os, sys, ogr
from osgeo import*
			
projeto = QgsProject.instance()
projetoPath = os.path.dirname(projeto.fileName())
crs = QgsCoordinateReferenceSystem("EPSG:4674")

caminhos = [os.path.join('C://Users//Desktop//kml-shapefile', nome) for nome in os.listdir('C://Users//Desktop//kml-shapefile')]
arquivos = [arq for arq in caminhos if os.path.isfile(arq)]
kmls = [arq for arq in arquivos if arq.lower().endswith(".kml")]
				
fileroute = ''
fKML = []

for nome in kmls:

			
	vlayer = QgsVectorLayer(nome, "line", "ogr")
	writer = QgsVectorFileWriter.writeAsVectorFormat(vlayer, nome[0:len(nome) -3] + 'shp', "utf-8", crs, "ESRI Shapefile")
	displayName =  nome[0:len(nome) -4].split('\\')[len(nome[0:len(nome) -4].split('\\')) - 1]
	filename = QgsVectorLayer(fileroute,displayName,"ogr")
	#QgsMapLayerRegistry.instance().addMapLayer(filename,False)
	limite = "C://Users//Desktop//kml-shapefile//" + displayName +".shp"
	iface.addVectorLayer(limite, " " + displayName, "ogr")
