from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding DXF
path_to_dxf = (
    "D:/GIS_Files/VML_Sample/sample.dxf|layername=entities|geometrytype=Point25D"
)
layer = QgsVectorLayer(path_to_dxf, "DXF file", "ogr")


if layer.isValid():
    print(layer.name())
else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
