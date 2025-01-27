from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
# QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)
QgsApplication.setPrefixPath("C:\OSGeo4W\apps\Python312\python.exe", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding Shapefile
path_to_shapefile = "G:/My Drive/GIS/vector_files/Ghana/district/Districts_Ghana.shp"

layer = QgsVectorLayer(path_to_shapefile, "District Capitals Shapefile", "ogr")


if layer.isValid():
    print(layer.name())
    #     QgsProject.instance().addMapLayer(vlayer)

    # layers = QgsProject().instance().mapLayers()
    # # print(layers)

    # l = [layer.name() for layer in QgsProject.instance().mapLayers().values()]
    # # print(l)

    # root = QgsProject.instance().layerTreeRoot()
    # childern = root.children()
    # print(root)
    # print(childern, type(childern[0]))
else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
