import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 
import com.example.model 1.0
ApplicationWindow {
    width: 640
    height: 480
    visible: true
    TableView {
        anchors.fill: parent;
        id: tv
        columnSpacing: 1
        rowSpacing: 1
        clip: true
        flickDeceleration: 5000

        model: PyModel

        selectionModel: ItemSelectionModel {id: selection_model
            model: tv.model
        }
        SelectionRectangle {
            target: tv
        }

        delegate: Rectangle {
            implicitWidth: 100
            implicitHeight: 30
            color: selected ? "blue" : "lightgray"

            required property bool selected

            Text { text: display }
        }
    }
}