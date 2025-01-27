from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
# QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)
QgsApplication.setPrefixPath("C:/OSGeo4W/apps/Python312/python.exe", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding Shapefile
path_to_shapefile = "G:/My Drive/GIS/vector_files/Ghana/district/Districts_Ghana.shp"
# path_to_shapefile = "G:/My Drive/GIS/vector_files/Ghana/POI_Ghana.shp"

layer = QgsVectorLayer(path_to_shapefile, "District Capitals Shapefile", "ogr")


if layer.isValid():
    print(layer.name())

    # check type of geometry of the layer
    print(layer.geometryType().__dict__)

    features = layer.getFeatures()

    for feature in features:  # type: ignore
        # get geometry coordinates of each feature

        feature_geom = feature.geometry()
        # print(feature_geom)
        print(feature_geom.wkbType().__dict__)

        #  check if feature geometry is point
        if feature_geom.type() == 0:
            print("Point Coordinate: ", feature_geom.asPoint())

        # check if feature geometry is polygon
        if feature_geom.type() == 2:
            print("Area calculated: ", feature_geom.area())
else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
