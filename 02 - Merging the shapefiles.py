outputMergefn = 'C://Users//Desktop//kml-shapefile//rodovias.shp'
directory = "C://Users//Desktop//kml-shapefile//"
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

iface.addVectorLayer('C://Users//Desktop//kml-shapefile//rodovias.shp', 'rodovias','ogr')
