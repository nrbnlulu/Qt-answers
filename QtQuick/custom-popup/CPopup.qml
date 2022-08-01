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
        ShaderEffect {id: _effect
            property real bend: 0
            property real minimize: 0
            property real side: root.toggled? 0: 0.8
            SequentialAnimation on bend {
                running: root.toggled
                NumberAnimation {
                    to: 0; duration: 300; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 600
                }
            }
            SequentialAnimation on bend {
                running: !root.toggled
                NumberAnimation {
                    to: 1; duration: 300; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 700
                }
            }
            SequentialAnimation on minimize {
                running: root.toggled
                NumberAnimation {
                    to: 0; duration: 300; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 700
                }
            }

            SequentialAnimation on minimize {
                running: !root.toggled
                NumberAnimation {
                    to: 1; duration: 300; easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 600
                }
            }
            mesh: Qt.size(10, 20)
            vertexShader: "./genie.vert.qsb"
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