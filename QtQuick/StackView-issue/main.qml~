import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

ApplicationWindow {
    id: root
    width: 500
    height: 500
    title: qsTr("Dr. T");
    visible: true
    Material.theme: Material.Dark

    StackView {
        id: stack_view;
        initialItem: loginWin;
        anchors.fill: parent;


        Component{ id: loginWin;
            LoginDark {
                onLoggedIn: {
                    console.log("to search_screen");
                    stack_view.push(search_screen);
                }
            }
        }


        Component{ id: search_screen;
            SecondScreen {
                onSearch: {
                    console.log("Test signal Invoked")
                    stack_view.push(interface_)
                }
            }
        }

            Component{ id: interface_;
            InterfaceDark {
                onAnalyzeReport: {
                    stack_view.pop()
                }
            }
        }
    }
}
