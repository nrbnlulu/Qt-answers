import QtQuick
import QtQuick.Controls
import QtQuick.Templates as T


T.Popup{id: root;
    implicitWidth: Math.max(implicitBackgroundWidth + leftInset + rightInset,
    contentWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(implicitBackgroundHeight + topInset + bottomInset,
    contentHeight + topPadding + bottomPadding)
    parent: Overlay.overlay
    padding: 6
    property real bend_
    property real minimize_
    property string loader_source;
    property var loader_component: undefined;


    background: Rectangle {id: _popup;
        color: "grey"
        radius: 2
        Loader{
            anchors.fill: parent;
            source: root.loader_source;
            sourceComponent: root.loader_component;
        }
        layer.enabled: true;
        layer.effect:
        ShaderEffect {id: _effect
            property real bend: root.bend_
            property real minimize: root.minimize_
            property real side: root.activeFocus? 0: 1
            mesh: Qt.size(10, 10)
            vertexShader: "./genie.vert.qsb"
        }
    }

    T.Overlay.modal: Rectangle {
        color: Qt.rgba(192, 192, 192, 0.3)
    }

    T.Overlay.modeless: Rectangle {
        color: Qt.rgba(192, 192, 192, 0.3)

    }

    enter: Transition {
        // grow_fade_in
        ParallelAnimation{

            NumberAnimation {
                property: "opacity"; from: 0.0; to: 1.0; easing.type: Easing.OutCubic; duration: 400
            }
            SequentialAnimation{
                PropertyAnimation {
                    properties: "bend_, minimize_"
                    from: 1; to: 0;  easing.type: Easing.InOutSine;
                    duration: 200;
                }
                PauseAnimation {
                    duration: 500
                }
            }
        }
    }

    exit: Transition {
        // shrink_fade_out
        ParallelAnimation{
            NumberAnimation {
                property: "opacity"; from: 1.0; to: 0.0; easing.type: Easing.OutCubic; duration: 400
            }
            SequentialAnimation{
                PropertyAnimation {
                    properties: "bend_, minimize_"
                    from: 0; to: 1; easing.type: Easing.InOutSine;
                    duration: 200;
                }
                PauseAnimation {
                    duration: 500
                }
            }
        }
    }

}