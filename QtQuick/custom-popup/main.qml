import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    id: mainFrame
    width: 640
    height: 480
    visible: true
    title: qsTr("Windows handeling in QML")
    Material.theme: Material.Dark
    Rectangle{
        anchors.fill: parent
        color: "green";
    Button{
        anchors.centerIn: parent
        text: "open popup"
        onClicked:{
           _popup.toggle()
        }
    }
    CPopup{id: _popup
        anchors.fill: parent;
        z: parent.z + 1
    }
    }


}
