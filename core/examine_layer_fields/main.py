from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.
path_to_shapefile = "D:/GIS_Files/shapefiles/districtCapitals"

layer = QgsVectorLayer(path_to_shapefile, "District Capitals Shapefile", "ogr")

if layer.isValid():
    fields = layer.fields()
    for field in fields:
        print(f"Field name: {field.name()} | Type: {field.typeName()}")

else:
    print("Layer failed to load!")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
