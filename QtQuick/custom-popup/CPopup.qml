import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

Item{id: root
    anchors.fill: parent;
    property bool toggled: false
    signal toggle;
    onToggle: {
        toggled = !toggled
    }

    Rectangle{id: _shader
        anchors.fill: parent;
        color: "black"
    }
    


    Rectangle{id: theItem
        height: parent.height * 0.8;
        width: parent.width / 2;
        color: "red"
        z: parent.z + 1
        anchors{
            verticalCenter: parent.verticalCenter;
            horizontalCenter: parent.horizontalCenter;
        }
        Button{
            text: "close popup";
            anchors.centerIn: parent;
            onClicked: {
                root.toggle()
            }
        }

    
        layer.enabled: true;
        layer.effect:
        ShaderEffect {
            width: theItem.width;
            height: theItem.height;
            //! [properties]
            property variant source: theItem
            property real bend: 0
            property real minimize: 0
            property real side: 5
            SequentialAnimation on bend {
                NumberAnimation {
                    to: 1; duration: 700; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 1600
                }
                NumberAnimation {
                    to: 0; duration: 700; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 1000
                }
            }
            SequentialAnimation on minimize {
                NumberAnimation {
                    to: 1; duration: 700; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 1000
                }
                NumberAnimation {
                    to: 0; duration: 700; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 1300
                }
            }
            //! [properties]
            //! [vertex]
            mesh: Qt.size(10, 20)
            vertexShader: "./genie.vert.qsb"
            //! [vertex]

        }

    }
    states: [
        State{
            name: "opened"
            when: toggled;
            PropertyChanges{
                target: root;
                opacity: 1
            }
            PropertyChanges{
                target: _shader
                opacity: 0.3
            }
        },
        State{
            name: "closed"
            when: !toggled;
            PropertyChanges{
                target: root;
                opacity: 0
            }
        }
        
    ]
    transitions: [
        Transition{
            from: "closed"; to: "opened";
            PropertyAnimation{
                properties: "opacity";
                easing.type: Easing.InOutQuad 
            }
        },
        Transition{
            from: "opened"; to: "closed";
            PropertyAnimation{
                properties: "opacity";
                easing.type: Easing.InOutQuad 
            }
        }
    ]
}