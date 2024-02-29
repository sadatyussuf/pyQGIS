from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding GPX
path_to_gpx = "D:/GIS/shapefiles/data/bennevis.gpx|layername=route_points"
layer = QgsVectorLayer(path_to_gpx, "GPX file", "ogr")


if layer.isValid():
    print(layer.name())
else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
