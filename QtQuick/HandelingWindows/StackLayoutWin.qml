import QtQuick
import QtQuick.Controls
import QtQuick.Layouts
import QtQuick.Controls.Material 2.15

Item{id: root
    signal returnToLogginWin;
    anchors.fill: parent;
    Button{id: return_to_StackView
        x: parent.width - width;
        y: tab_bar.y
        text: "return to login page"
        onClicked: {
            root.returnToLogginWin()
        }
    }
    ColumnLayout{
        anchors.fill: parent;
        TabBar {
            id: tab_bar
            TabButton {
                width: 100
                text: qsTr("foo")
            }
            TabButton {
                width: 100
                text: qsTr("bar")
            }
            TabButton {
                width: 100
                text: qsTr("Loader")
            }
        }


        StackLayout {
            id: stack_layout
            currentIndex: tab_bar.currentIndex
            Rectangle {
                color: 'teal'
                Label{
                    anchors.centerIn: parent
                    text: "Page " + stack_layout.currentIndex
                }
                implicitWidth: 200
                implicitHeight: 200
            }
            Rectangle {
                color: 'plum'
                implicitWidth: 300
                implicitHeight: 200
                Label{
                    anchors.centerIn: parent
                    text: "Page " + stack_layout.currentIndex
                }
            }
            JustALoader{

            }
        }

    }
}