import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

Item{id: root
    anchors.fill: parent;
    property bool toggled: false
    signal toggle;
    visible: false
    onToggle: {
        toggled = !toggled
        _fader.start()
    }

    Rectangle{id: _shader
        anchors.fill: parent;
        color: "black"
        opacity: 0

    }
    OpacityAnimator {id: _fader;
        target: _shader;
        from: toggled? 0: 0.3;
        to: toggled? 0.3: 0;
        duration: 500
        onStarted: {
            root.visible = true
        }
        onFinished:{ if (!root.toggled){root.visible = false;}}
    }

    // ShaderEffectSource {
    //     id: theSource
    //     sourceItem: theItem
    // }

    Rectangle{id: theItem
        height: parent.height * 0.8;
        width: parent.width / 2;
        color: "red"
        visible: root.toggled
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

    }


//     ShaderEffect {
//         width: 160
//         height: 160
//         //! [properties]
//         property variant source: theSource
//         property real bend: 0
//         property real minimize: 0
//         property real side: genieSlider.value
//         SequentialAnimation on bend {
//         loops: Animation.Infinite
//         NumberAnimation {
//             to: 1; duration: 700; easing.type: Easing.InOutSine
//         }
//         PauseAnimation {
//             duration: 1600
//         }
//         NumberAnimation {
//             to: 0; duration: 700; easing.type: Easing.InOutSine
//         }
//         PauseAnimation {
//             duration: 1000
//         }
//     }
//     SequentialAnimation on minimize {
//     loops: Animation.Infinite
//     PauseAnimation {
//         duration: 300
//     }
//     NumberAnimation {
//         to: 1; duration: 700; easing.type: Easing.InOutSine
//     }
//     PauseAnimation {
//         duration: 1000
//     }
//     NumberAnimation {
//         to: 0; duration: 700; easing.type: Easing.InOutSine
//     }
//     PauseAnimation {
//         duration: 1300
//     }
// }
// //! [properties]
// //! [vertex]
// mesh: Qt.size(10, 10)
// vertexShader: "./genie.vert.qsb"
// //! [vertex]
// Slider {
//     id: genieSlider
//     anchors.left: parent.left
//     anchors.right: parent.right
//     anchors.bottom: parent.bottom
//     anchors.leftMargin: 4
//     anchors.rightMargin: 4
//     height: 40
// }
// }

}