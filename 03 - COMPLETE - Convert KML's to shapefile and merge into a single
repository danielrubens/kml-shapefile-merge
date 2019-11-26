import os.path
from qgis._core import*
from qgis.gui import*
from PyQt5.QtCore import *
import os, sys, ogr
from osgeo import*
			
projeto = QgsProject.instance()
projetoPath = os.path.dirname(projeto.fileName())
crs = QgsCoordinateReferenceSystem("EPSG:4674")

caminhos = [os.path.join('C://Users//Daniel//Desktop//kml-shapefile', nome) for nome in os.listdir('C://Users//Daniel//Desktop//kml-shapefile')]
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
	limite = "C://Users//Daniel//Desktop//kml-shapefile//" + displayName +".shp"
	iface.addVectorLayer(limite, " " + displayName, "ogr")


outputMergefn = 'C://Users//Daniel//Desktop//kml-shapefile//rodovias.shp'
directory = "C://Users//Daniel//Desktop//kml-shapefile//"
fileStartsWith = 'rod'
fileEndsWith = '.shp'
driverName = 'ESRI Shapefile'
geometryType = ogr.wkbLineString

out_driver = ogr.GetDriverByName( driverName )
out_ds = out_driver.CreateDataSource(outputMergefn)
out_layer = out_ds.CreateLayer(outputMergefn, geom_type=geometryType)

fileList = os.listdir(directory)




for file in fileList:
    if file.startswith(fileStartsWith) and file.endswith(fileEndsWith):
         print (file)
         ds = ogr.Open(directory+file)
         lyr = ds.GetLayer()
         for feat in lyr:
            out_feat = ogr.Feature(out_layer.GetLayerDefn())
            out_feat.SetGeometry(feat.GetGeometryRef().Clone())
            out_layer.CreateFeature(out_feat)
            out_feat = None
            out_layer.SyncToDisk()

iface.addVectorLayer('C://Users//Daniel//Desktop//kml-shapefile//rodovias.shp', 'rodovias','ogr')
