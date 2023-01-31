import QtQuick
import QtQuick.Controls
import QtMultimedia
import com.myapp.components
import QtQuick.Controls.Material

ApplicationWindow {
    id: mainFrame
    Material.theme: Material.Dark
    width: 640
    height: 480
    visible: true
    title: qsTr("Cam Test")

    Cv2Capture {
        id: bridge
        onImageAnalayized: function (res) {
            console.log(res);
        }
    }

    Rectangle {
        id: rect
        width: 640
        height: 400

        MediaDevices {
            id: mediaDevices
        }

        CaptureSession {
            imageCapture: ImageCapture {
                id: capture
                onImageCaptured: function (req_id, preview) {
                    bridge.receive(req_id, preview);
                }
            }
            camera: Camera {
                id: camera
            }
            videoOutput: output
        }

        VideoOutput {
            id: output
            anchors.fill: parent
        }

        Button {
            id: startCamButton
            text: "Start Cam"
            anchors.top: output.bottom
            anchors.left: output.left
            onClicked: {
                camera.start();
                camImage.opacity = 0;
            }
        }

        Button {
            id: takePicButton
            text: "take pic"
            anchors.top: output.bottom
            anchors.left: startCamButton.right
            onClicked: {
                capture.capture();
                camImage.opacity = 1;
            }
        }

        Image {
            id: camImage
            anchors.fill: parent
            source: capture.preview
        }
    }
}
