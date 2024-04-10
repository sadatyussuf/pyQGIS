from pathlib import Path

from qgis.core import QgsApplication, QgsVectorLayer

BASEDIR = Path(__file__).cwd()


# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.


# Path to the point layer
layer_path = BASEDIR / "data/random_points.gpkg|layername=random_points"

# Load point layer
layer = QgsVectorLayer(str(layer_path), "Random Points Layer", "ogr")


# Check if the layer is valid
if layer.isValid():
    # Define output CSV file
    csv_path = BASEDIR / "data/random_points.csv"

    fields = layer.fields()

    # Get field names
    field_names = [field.name() for field in fields]
    field_names.extend(["x", "y"])
    print(field_names)

    # Write CSV header
    with open(csv_path, "w") as csv_file:
        csv_file.write(",".join(field_names) + "\n")

        # Write attribute values
        features = layer.getFeatures()

        for feature in features:
            x_coords = feature.geometry().asPoint().x()
            y_coords = feature.geometry().asPoint().y()

            extra = [str(x_coords), str(y_coords)]

            values = [str(feature[field.name()]) for field in layer.fields()]
            print(values)
            values.extend(extra)
            print(values)
            csv_file.write(",".join(values) + "\n")

    # print(f"Point attributes exported to: {csv_path}")
else:
    print("Invalid layer.")


# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
