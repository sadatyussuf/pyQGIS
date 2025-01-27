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


# ----------- Main Code: Accessing Fields ----------------


if layer.isValid():

    print("*" * 27)
    print(layer.name())
    print("*" * 27)

    fields = layer.fields()

    print(
        "{:<20} {:<15} {:<10} {:<10} {:<10}".format(
            "Field Name", "Type Name", "Length", "Precision", "Read Only"
        )
    )
    print("-" * 68)

    fields = layer.fields()
    for field in fields:
        print(
            "{:<20} {:<15} {:<10} {:<10} {:<10}".format(
                field.name(),
                field.typeName(),
                field.length(),
                field.precision(),
                field.isReadOnly(),
            )
        )
else:
    print("can't load layer")


# ----------- Main Code: Accessing Fields ----------------


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
