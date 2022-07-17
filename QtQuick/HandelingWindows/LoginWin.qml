import QtQuick
import QtQuick.Controls
Rectangle{id: root
    anchors.fill: parent;
    color: "grey"
    signal loggedIn;

    TextArea{id: input_
        placeholderText: "Enter password"
        anchors.centerIn: parent
        background: Rectangle{
            color: "red"
        }
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