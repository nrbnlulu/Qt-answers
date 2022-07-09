import QtQuick 2.12
import QtQuick.Controls 2.14
 import Qt.labs.qmlmodels 1.0
import QtQuick.Layouts 1.14

ApplicationWindow {id: root
    visible: true
    width: 600
    height: 500
    title: "HelloApp"
    property var currentIndex;


Rectangle {
    anchors.fill: parent;
  //I added this button
  Button {
    x:179
    y:235
    text: "Button"
    z: 1
    onClicked: {
      //There's no use here!

      table_model.rows[0].name = "fdsafsd";
      console.log(table_model.rows[0].name)
      t1.model.dataChanged(currentIndex, currentIndex)
    }
  }
  // Button End

  TableView {
    id: t1
    anchors.fill: parent
    columnSpacing: 1
    rowSpacing: 1
    clip: true

    model: TableModel {id: table_model
      TableModelColumn {
        display: "name"
      }
      TableModelColumn {
        display: "color"
      }

      rows: [{
          "name": "cat",
          "color": "black"
        }, {
          "name": "dog",
          "color": "brown"
        }, {
          "name": "bird",
          "color": "white"
        }]
    }

    delegate: Rectangle {
        property bool selected: false;
        implicitWidth: 100
        implicitHeight: 50
        border.width: 1
        color: selected? "red": "green"
        MouseArea{
            anchors.fill: parent;
            onClicked:{
                root.currentIndex =table_model.index(model.row, model.column)
                console.log(root.currentIndex)
            } 
        }
      Text {
        text: display
        anchors.centerIn: parent
      }
    }
  }
}
}