from pprint import pprint

from qgis.core import (
    QgsApplication,
    QgsFeature,
    QgsFeatureIterator,
    QgsFeatureRequest,
    QgsVectorLayer,
)

# Supply path to qgis install location default path =
# QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)
QgsApplication.setPrefixPath(r"C:\OSGeo4W\apps\Python312\python.exe", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding Shapefile
poly_shapefile = "G:/My Drive/GIS/vector_files/Ghana/district/Districts_Ghana.shp"
point_shapefile = "G:/My Drive/GIS/vector_files/Ghana/POI_Ghana.shp"

poly_layer = QgsVectorLayer(poly_shapefile, "District Capitals Shapefile", "ogr")
point_layer = QgsVectorLayer(point_shapefile, "District Capitals Shapefile", "ogr")


def select_district_by_name(layer: QgsVectorLayer, dist_name: str) -> list[QgsFeature]:
    selected_district = layer.selectByExpression(f"DISTRICT='{dist_name}'")

    return list(layer.getSelectedFeatures())


if poly_layer.isValid() and point_layer.isValid():

    # print(type(poly_layer))
    # print(poly_layer.name(), point_layer.name())

    # print(poly_layer.getFeature(1).attributeMap())
    # print(poly_layer.ge)

    selected_district = select_district_by_name(poly_layer, "Accra Metro")[0]

    get_bouding_box = selected_district.geometry().boundingBox()

    filter_request = QgsFeatureRequest().setFilterRect(get_bouding_box)  # .setLimit(10)

    # To return a subset of the selected fields by name
    # filter_request = filter_request.setSubsetOfAttributes(
    #     ["x", "y"], point_layer.fields()
    # )

    get_features = point_layer.getFeatures(filter_request)

    selected_features = [f.attributeMap() for f in get_features]  # type: ignore

    print(selected_district)
    print(get_bouding_box)
    print(filter_request)
    pprint(selected_features)
    pprint(len(selected_features))


else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
