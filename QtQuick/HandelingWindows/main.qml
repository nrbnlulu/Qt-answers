import QtQuick
import QtQuick.Controls

ApplicationWindow {
    id: mainFrame
    width: 640
    height: 480
    visible: true
    title: qsTr("Windows handeling in QML")
    
    StackView{id: stack_view
    initialItem: logginWin
        anchors.fill: parent;
        LoginWin{id: logginWin
            onLoggedIn: {
                stack_view.push("./OtherWin.qml")
                console.log("logged In")
            }
        }
    }
}
