import QtQuick
import com.example.app 1.0

Window {
    visible: true
    width: 1000
    height: 700
    title: "Portmod"

    Rectangle {
        color: App.enumValue == Enums.Status.Connected ? "green" : "red"
        anchors.fill: parent
    }
}
