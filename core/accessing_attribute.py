from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
# QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)
QgsApplication.setPrefixPath(r"C:\OSGeo4W\apps\Python312\python.exe", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding Shapefile
path_to_shapefile = "G:/My Drive/GIS/vector_files/Ghana/district/Districts_Ghana.shp"

layer = QgsVectorLayer(path_to_shapefile, "District Capitals Shapefile", "ogr")


if layer.isValid():
    print(layer.name())
    fields = layer.fields()
    for field in fields:
        print(field.name(), " | ", field.typeName())
    # features = layer.getFeatures()
    # for feature in features:  # type: ignore

    #     # # Getting attribute as a dictornary
    #     # print(feature.attributeMap())

    #     # # Getting attribute values as a list
    #     # print(feature.attributes())

    #     # Getting attribute values by name
    #     print(feature["REGION"], " | ", feature["CAPITAL"], " | ", feature["DISTRICT"])

    #     # # Getting attribute values by index
    #     # print(feature[10], " | ", feature[1], " | ", feature[5])
else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
