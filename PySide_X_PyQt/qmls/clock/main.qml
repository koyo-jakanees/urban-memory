import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 60
    title: qsTr("ClockApp")
    property string currTime: "00:00:00"
    property QtObject backend


    Rectangle{
        anchors.fill: parent 
            
        Image{
            anchors.fill: parent
            sourceSize.width: parent.width/2
            sourceSize.height: parent.height/2
            source: "./imgs/background.png"; //srcset="https://ik.imagekit.io/mfitzp/tutorials/qml-qtquick-python-application/background.png?tr=w-100 100w, https://ik.imagekit.io/mfitzp/tutorials/qml-qtquick-python-application/background.png?tr=w-200 200w, https://ik.imagekit.io/mfitzp/tutorials/qml-qtquick-python-application/background.png?tr=w-400 400w, https://ik.imagekit.io/mfitzp/tutorials/qml-qtquick-python-application/background.png?tr=w-600 600w" loading="lazy" width="564" height="1003"
            fillMode: Image.PreserveAspectCrop
        }
        Rectangle {
            anchors.fill: parent
            color: "transparent"
            Text {
                anchors {
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime
                font.pixelSize: 24
                color: "white"
            }
        }
    }
    Connections {
        target: backend

        function onUpdated(msg) {
            currTime = msg;
        }
    }

}