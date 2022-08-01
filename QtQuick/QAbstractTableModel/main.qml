import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    TableView {
        anchors.fill: parent;
        id: installedPkgsTable
        columnSpacing: 1
        rowSpacing: 1
        clip: true
        flickDeceleration: 5000

        model: PyModel

        selectionModel: ItemSelectionModel {
            model: installedPkgsTable.model
        }

        delegate: Rectangle {
            implicitWidth: 300
            implicitHeight: 50
            color: selected ? "blue": "lightgray"

            required property bool selected
    
            Text {
                text: model.display
            }
        }
    }
}