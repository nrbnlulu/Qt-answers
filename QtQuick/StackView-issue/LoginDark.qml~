import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

Item {
    id: root
    anchors.fill: parent

    signal loggedIn()

    Rectangle {
        id: rectangle
        color: "red"
        anchors.fill: parent
        Button {
            onClicked:{
                root.loggedIn()
            }
        }
    }
}
