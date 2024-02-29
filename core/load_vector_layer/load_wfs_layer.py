from qgis.core import QgsApplication, QgsVectorLayer

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()


# ? Adding WFS
path_to_wfs = "https://mrdata.usgs.gov/services/wfs/active-mines?srsname=EPSG:4326&typename=ms:mineplant&request=GetFeature&service=WFS"
layer = QgsVectorLayer(path_to_wfs, "WFS file", "WFS")

if layer.isValid():
    print(layer.name())
else:
    print("can't load layer")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
