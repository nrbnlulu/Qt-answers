import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle{
    anchors.fill: parent;
    RangeSlider{id: range_slider
        anchors.fill: parent;
        first.onMoved: function(){SomeNameForPythonBridge.set_from(range_slider.first.value)}
        second.onMoved: function(){SomeNameForPythonBridge.set_to(range_slider.second.value)}

    }
}