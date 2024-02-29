from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.
layer_path = "D:/GIS_Files/shapefiles/districtCapitals"

layer = QgsVectorLayer(layer_path, "District Capitals Shapefile", "ogr")

if layer.isValid():
    features = layer.getFeatures()

    for feature in features:
        # print(feature.attributeMap())
        # print(feature.attributes(), feature.attributeCount())
        print(feature.attribute("DISTRICT"), feature.hasGeometry(), feature.geometry())
    print("valid")

else:
    print("error found")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
