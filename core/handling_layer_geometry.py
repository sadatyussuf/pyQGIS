from qgis.core import (
    QgsApplication,
    QgsCoordinateReferenceSystem,
    QgsVectorLayer,
    QgsWkbTypes,
)

# Supply path to qgis install location default path =
# QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)
QgsApplication.setPrefixPath(r"C:\OSGeo4W\apps\Python312\python.exe", True)


# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding Shapefile
# path_to_shapefile = "G:/My Drive/GIS/vector_files/Ghana/district/Districts_Ghana.shp"
path_to_shapefile = "G:/My Drive/GIS/vector_files/Ghana/POI_Ghana.shp"

layer = QgsVectorLayer(path_to_shapefile, "District Capitals Shapefile", "ogr")

#################### Put your main code below ####################


if layer.isValid():
    print(layer.name())
    # ======================================================
    # SECTION: Checking CRS of the Layer
    # ======================================================

    # print(layer.crs().authid())  # e.g., 'EPSG:4326'
    # print(layer.crs().description())  # e.g., 'WGS 84'
    # print(layer.crs().isGeographic())  # True if geographic coordinate system
    # print(layer.crs().isValid())  # True if the CRS is valid

    # ======================================================
    # SECTION: Reprojecting CRS of the Layer
    # ======================================================

    # new_crs = QgsCoordinateReferenceSystem("EPSG:4326")
    # layer.setCrs(new_crs)
    # print("Layer CRS set to:", layer.crs().authid())

    # ======================================================
    # SECTION: Get Features of the Layer
    # ======================================================

    features = layer.getFeatures()
    for feature in features:  # type: ignore
        # print(feature)

        # ======================================================
        # SECTION: Feature Geometry
        # ======================================================

        feature_geom = feature.geometry()

        # print(feature_geom.type())

        # print(QgsWkbTypes.displayString(feature_geom.wkbType()))

        # print(QgsWkbTypes.isMultiType(feature_geom.wkbType()))

        # if feature_geom.isEmpty():
        #     print("Feature has no geometry.")

        # if feature_geom.wkbType() in [QgsWkbTypes.NoGeometry, QgsWkbTypes.Unknown]:
        #     print("This layer has no geometry or an unknown type.")

        # if feature_geom.isGeosValid():
        #     print("Geometry is valid")

else:
    print("can't load layer")

#################### Put your main code above ####################


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
