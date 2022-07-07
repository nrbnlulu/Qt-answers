import QtQuick 2.15
import QtQuick.Window 2.15
import QtQuick.Controls 2.15
import QtGraphicalEffects 1.15

ApplicationWindow {
    id: myApplicationWindow
    title: "Expandable ListView App"
    visible: true
    height: 400
    width: 400

    Rectangle {
        id: rootRectangle
        color: "grey"
        anchors.fill: parent

        Item {
            id: solutionFileListViewRoot
            anchors.fill: parent
            // ListModel {
            //     id: myNestedListModel
            //     ListElement {
            //         assetName: "Dummy Item"
            //         isCollapsed: true
            //         subItems: [ListElement {cellSize: "888"}]
            //     }
            // }
            ListView {
                id: myNestedListView
                anchors {
                    top: parent.top
                    left: parent.left
                    right: parent.right
                    bottom: parent.bottom
                    bottomMargin: 50
                }
                model: backendObjectInQML.model
                // model: myNestedListModel
                delegate: myAppListElementDelegate
                spacing: 6
                clip: true
                ScrollBar.vertical: ScrollBar {
                    active: true
                }
            }
        }

        Component {
            id: myAppListElementDelegate
            Column {
                id: listElementColumn
                width: myNestedListView.width
                Rectangle {
                    id: listElementRectangle
                    height: 30
                    anchors {
                        left: parent.left
                        right: parent.right
                        rightMargin: 15
                        leftMargin: 15
                    }
                    color: "yellow"
                    radius: 3
                    Text {
                        height: 24
                        width: 100
                        text: assetName
                        anchors {
                            verticalCenter: parent.verticalCenter
                            left: parent.left
                        }
                        horizontalAlignment: Text.AlignLeft
                        verticalAlignment: Text.AlignVCenter
                        color: "black"
                    }
                    Button {
                        id: expandButton
                        width: 70
                        height: 24
                        text: "Expand"
                        anchors {
                            right: parent.right
                            rightMargin: 20
                            verticalCenter: parent.verticalCenter
                        }
                        onClicked: {
                            myNestedListView.currentIndex = index
                            backendObjectInQML.model.collapseEditInputsMenu(index, "isCollapsed")
                            console.log("From QML isCollapsed:")
                            console.log(isCollapsed)
                        }
                    }
                }
                Loader {
                    id: subSolutionEditItemLoader
                    visible: !model.isCollapsed
                    property variant subEditItemModel: subItems
                    sourceComponent: model.isCollapsed ? null : subItemEditInputsDelegate
                    onStatusChanged: {
                        // console.log(subItems)
                        if(status == Loader.Ready) item.model = subEditItemModel
                    }
                }
            }
        }

        Component {
            id: subItemEditInputsDelegate

            Column {
                property alias model: subItemRepeater.model
                id: nestedListElementColumn
                width: myNestedListView.width
                anchors {
                    top: parent.top
                    topMargin: 3
                }
                spacing: 3

                Repeater {
                    id: subItemRepeater
                    width: parent.width
                    delegate: Rectangle {
                        id: nestedListElementRectangle
                        color: "blue"
                        height: 40
                        anchors {
                            left: parent.left
                            leftMargin: 30
                            right: parent.right
                            rightMargin: 30
                        }
                        radius: 5

                        Rectangle {
                            id: cellSizeBackground
                            height: 20
                            width: cellSizeLabel.implicitWidth
                            color: "#00000000"
                            anchors {
                                left: parent.left
                                leftMargin: 25
                                top: parent.top
                                topMargin: 10
                            }
                            Label {
                                id: cellSizeLabel
                                text: "Cell Size: "
                                anchors.fill: parent
                                verticalAlignment: Text.AlignVCenter
                                color: "#6e95bc"
                            }
                        }

                        Rectangle {
                            id: cellSizeTextInputBorder
                            height: 24
                            width: 120
                            color: "#00000000"
                            radius: 5
                            anchors {
                                left: cellSizeBackground.right
                                leftMargin: 10
                                verticalCenter: cellSizeBackground.verticalCenter
                            }
                            border.width: 1
                            border.color: "#12C56A"

                            TextInput {
                                id: cellSizeTextInput
                                text: cellSize
                                verticalAlignment: Text.AlignVCenter
                                anchors.fill: parent
                                color: "#6e95bc"
                                selectByMouse: true
                                leftPadding: 5
                                rightPadding: 5
                                clip: true

                                onEditingFinished: {
                                    console.log("cellSizeTextInput edited...")
                                }
                            }
                        }
                    }
                }
            }
        }

        Button {
            id: addListElementButton
            height: 24
            width: 70
            text: "Add"
            anchors {
                bottom: parent.bottom
                right: parent.right
            }
            onClicked: {
                backendObjectInQML.model.appendRow("Dummy Item", false)
            }
        }
    }
}