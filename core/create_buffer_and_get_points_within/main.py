from qgis.core import (
    QgsApplication,
    QgsFeatureRequest,
    QgsGeometry,
    QgsPointXY,
    QgsVectorLayer,
)

# Supply path to qgis install location default path =
QgsApplication.setPrefixPath("C:/Program Files/QGIS 3.22.11/apps/qgis-ltr", True)

# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Write your code here to load some layers, use processing
# algorithms, etc.
path_to_shapefile = "D:/GIS_Files/shapefiles/districtCapitals"

layer = QgsVectorLayer(path_to_shapefile, "District Capitals Shapefile", "ogr")

if layer.isValid():
    # This part creates a QgsPointXY object, which represents a 2D point in space.
    point = QgsPointXY(205603.72367, 205603.72367)

    # This part takes the QgsPointXY object created above and converts it into a QgsGeometry object.
    reference_point = QgsGeometry.fromPointXY(point)

    # Buffer distance in meters,
    buffer_distance = 600000

    # Create a buffer around the reference point of the specified distance
    buffer_point = reference_point.buffer(distance=buffer_distance, segments=0)

    # The boundingBox() method is used to obtain the bounding box coordinates of the buffer_point. The bounding box is a rectangle that encloses the entire buffered area.
    boundary_box_around_buffer_point = buffer_point.boundingBox()

    # QgsFeatureRequest is used to create a request for features from a vector layer. The setFilterRect(...) method is used to set a spatial filter based on a rectangle. In this case, it sets the spatial filter to the bounding box of the buffer.
    filter_request = QgsFeatureRequest().setFilterRect(boundary_box_around_buffer_point)

    # This part retrieves features from the layer based on the specified QgsFeatureRequest. It returns an iterator over the features that falls within the boundary of our buffered point
    get_features = layer.getFeatures(filter_request)

    selected_features = [{f.id(): f.attribute("DISTRICT")} for f in get_features]

    print(
        f"Points within {buffer_distance} units of the reference point: {selected_features}"
    )

else:
    print("Layer failed to load!")

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()
