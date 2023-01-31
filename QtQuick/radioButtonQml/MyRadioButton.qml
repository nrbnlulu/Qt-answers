import QtQuick 2.15
import QtQuick.Controls 2.15

RadioButton {
    id: btn
    onClicked: App.set_current_rb_text(btn.text)
}
