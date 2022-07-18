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

    StackView{id: stack_view
        initialItem: logginWin
        anchors.fill: parent;
        Component{id: logginWin
            LoginWin{
                onLoggedIn: {
                    stack_view.push(stack_le)
                    console.log("logged In")
                }
            }
        }
        Component{id: stack_le
            StackLayoutWin{
                onReturnToLogginWin:{
                    stack_view.pop()
                }
            }
        }
    }
}
