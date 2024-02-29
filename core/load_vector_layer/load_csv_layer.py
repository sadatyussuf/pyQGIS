from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding CSV
path_to_csv = "file:///D:/GIS/shapefiles/data/test.csv?xField=longitude&yField=latitude&crs=EPSG:4326"
layer = QgsVectorLayer(path_to_csv, "CSV file", "delimitedtext")


if layer.isValid():
    print(layer.name())
else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
