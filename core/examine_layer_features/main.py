from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:\\OSGeo4W\\apps\\qgis\\python", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.
layer_path = "C:\\Users\\anwur\\Downloads\\korle_kottery\\korle_reprojeced.shp"

layer = QgsVectorLayer(layer_path, "District Capitals Shapefile", "ogr")

if layer.isValid():
    features = layer.getFeatures()

    for feature in features:  # type: ignore
        #     print(feature.attribute("DISTRICT"), feature.hasGeometry(), feature.geometry())
        print(
            feature.attributeMap(),
            #     feature.attributes(),
            #     feature.attribute("DISTRICT"),
            #     feature.attributeCount(),
            #     feature.hasGeometry(),
            #     feature.geometry(),
        )
    print("valid")

else:
    print("error found")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
