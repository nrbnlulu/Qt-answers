import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import com.example.model 1.0

ApplicationWindow {
    visible: true
    width: 1000
    height: 700
    title: "Portmod"

    TableView {
        id: installedPkgsTable
        anchors.fill: parent
        columnSpacing: 1
        rowSpacing: 1
        clip: true

        model: InstalledPkgsModel

        selectionModel: ItemSelectionModel {
            model: installedPkgsTable.model
        }

        delegate: Rectangle {
            implicitWidth: 300
            implicitHeight: 50
            required property bool selected
            color: selected ? "blue" : "lightgray"

            Text {
                text: display + "; index is ->" + index
            }
        }
        // SelectionRectangle {
        //     target: installedPkgsTable
        // }
    }
}
