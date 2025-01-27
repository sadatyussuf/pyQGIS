from pprint import pprint

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


def display_selected_features(getSelectedFeatures):
    features = list(getSelectedFeatures)

    for feature in features:
        pprint(feature.attributeMap())

    print()

    pprint(f"{len(features)} features selected")


if layer.isValid():
    print(layer.name())

    # selecting all features in the layer
    # layer.selectAll()

    # Selecting features by experssion
    layer.selectByExpression("REGION='Western'")

    getSelectedFeatures = layer.getSelectedFeatures()

    # print(getSelectedFeatures, list(getSelectedFeatures))
    display_selected_features(getSelectedFeatures)

    # deselecting all features in the layer
    layer.removeSelection()

    print(
        "All Selected Features have been deselected", list(layer.getSelectedFeatures())
    )

else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
