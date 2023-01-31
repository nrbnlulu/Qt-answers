import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

Item {
    id: root
    property real minimize: 0
    property real bend: 0
    anchors.fill: parent
    property bool toggled: false
    signal toggle
    onToggle: {
        toggled = !toggled;
    }

    Rectangle {
        id: _shader
        anchors.fill: parent
        color: "black"
    }

    Rectangle {
        id: theItem
        height: parent.height * 0.8
        width: parent.width / 2
        color: "red"
        z: parent.z + 1
        anchors {
            verticalCenter: parent.verticalCenter
            horizontalCenter: parent.horizontalCenter
        }
        Button {
            text: "close popup"
            anchors.centerIn: parent
            onClicked: {
                root.toggle();
            }
        }

        layer.enabled: true
        layer.effect: ShaderEffect {
            id: _effect
            property real bend: root.bend
            property real minimize: root.minimize
            property real side: root.toggled ? 0 : 1
            mesh: Qt.size(10, 20)
            vertexShader: "./genie.vert.qsb"
        }
    }
    states: [
        State {
            name: "opened"
            when: toggled
            PropertyChanges {
                target: root
                opacity: 1
                bend: 0
                minimize: 0
            }
            PropertyChanges {
                target: _shader
                opacity: 0.3
            }
        },
        State {
            name: "closed"
            when: !toggled
            PropertyChanges {
                target: root
                opacity: 0
                bend: 1
                minimize: 1
            }
        }
    ]
    transitions: [
        Transition {
            from: "closed"
            to: "opened"
            PropertyAnimation {
                properties: "opacity"
                easing.type: Easing.InOutQuad
            }
            SequentialAnimation {
                PropertyAnimation {
                    properties: "bend, minimize"
                    duration: 300
                    easing.type: Easing.InOutSine
                }
                PauseAnimation {
                    duration: 600
                }
            }
        },
        Transition {
            from: "opened"
            to: "closed"
            ParallelAnimation {
                PropertyAnimation {
                    properties: "opacity"
                    easing.type: Easing.InOutQuad
                }
                SequentialAnimation {
                    PropertyAnimation {
                        properties: "bend, minimize"
                        duration: 300
                        easing.type: Easing.InOutSine
                    }
                    PauseAnimation {
                        duration: 600
                    }
                }
            }
        }
    ]
}
