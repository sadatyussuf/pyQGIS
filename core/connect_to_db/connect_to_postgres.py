from qgis.core import QgsApplication, QgsDataSourceUri, QgsProject, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/OSGeo4W/apps/Python312/python.exe", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding PostGIS Layer
uri = QgsDataSourceUri()

uri.setConnection("localhost", "5432", "postgres", "postgres", "asyissah")

uri.setDataSource("public", "world", "geom")

vlayer = QgsVectorLayer(uri.uri(False), "World Map", "postgres")

print(vlayer)

if vlayer.isValid():
    print(vlayer.geometryType().__dict__)
    print("Layer is valid")
    features = vlayer.getFeatures()

    # for feature in features:  # type: ignore
    #     print(feature.attributes())

else:
    print("Layer is not valid")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
