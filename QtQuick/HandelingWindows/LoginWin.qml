import QtQuick
import QtQuick.Controls
import QtQuick.Controls.Material 2.15

Item{id: root
    anchors.fill: parent;
    signal loggedIn;

    TextArea{id: input_
        placeholderText: "Enter password"
        anchors.centerIn: parent
    }
    Button{
        text: "Login";

        anchors {
            horizontalCenter: parent.horizontalCenter;
            top: input_.bottom
        }
        onClicked: {
            console.log(input_.text)

            if(input_.text == "12345")
            {
                root.loggedIn()
            }
            else{
                input_.text = "Wrong password"
            }
        }
    }
}