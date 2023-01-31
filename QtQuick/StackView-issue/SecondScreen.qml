import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

Item {
    id: login_item
    anchors.fill: parent

    signal search

    Rectangle {
        id: rectangle
        color: "green"
        anchors.fill: parent
        Button {
            onClicked: {
                login_item.search();
            }
        }
    }
}
