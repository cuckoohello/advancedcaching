import QtQuick 1.0
import com.nokia.meego 1.0
import "uiconstants.js" as UI
import QtWebKit 1.0

Page {

    onStatusChanged: {
        if (status == PageStatus.Inactive && tabDetailsPageStack.depth == 1) {
            pageDescription.source = "";
        } 
        if (status == PageStatus.Active && currentGeocache) {
            currentGeocache.setViewed();
        }
    }

    Flickable {
        anchors.fill: parent
        id: flick
        boundsBehavior: Flickable.DragOverBounds
        
        GeocacheHeader{
            cache: currentGeocache
            id: header
        }
        
        Column {
            id: col1
            spacing: 16
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.leftMargin: 16
            anchors.rightMargin: 16
            anchors.top: header.bottom

            Label {
                font.pixelSize: UI.FONT_DEFAULT
                text: currentGeocache ? currentGeocache.title : "None selected"
                anchors.left: parent.left
                anchors.right: parent.right
                wrapMode: Text.Wrap
                id: title
            }

            Label {
                font.pixelSize: 20
                color: UI.COLOR_INFOLABEL
                text: "Last updated"
                id: labelUpdated
            }
            
            Label {
                id: updated
                text: currentGeocache.updated
                anchors.left: parent.left
                anchors.right: parent.right
                wrapMode: Text.Wrap
            }
            
            WebView {
                anchors.left: parent.left
                anchors.right: parent.right
                
                html: "<html><body style='background-color: #eeeeee; font-family: sans-serif; font-size: 24px; padding: 0px; margin: 0px;'>" + currentGeocache.desc + "</body></html>"
                settings.javascriptEnabled: false
                settings.javaEnabled: false
                preferredWidth: parent.parent.width
                settings.minimumFontSize: 20
                id: description
                onWidthChanged: {
                    reload.trigger();
                }
            }

            Label {
                font.pixelSize: 20
                color: UI.COLOR_INFOLABEL
                text: "Attributes"
                id: labelAttributes
            }

            Label {
                id: attributes
                text: currentGeocache.attributes.replace(/,/g, ", ") || "No Attributes"
                anchors.left: parent.left
                anchors.right: parent.right
                wrapMode: Text.Wrap
            }
            
            Label {
                font.pixelSize: 20
                color: UI.COLOR_INFOLABEL
                text: currentGeocache.hints ? "Drag for hints" : "No Hint"
                id: label
            }
            
            Label {
                id: hints
                text: currentGeocache.hints || "Really no Hint"
                anchors.left: parent.left
                anchors.right: parent.right
                wrapMode: Text.Wrap
            }
        }
        
        

        clip: true
        contentWidth: width
        contentHeight: title.height + 16 + label.height + 16 + labelUpdated.height + 16 + updated.height + 16 + description.height + header.height + 16 + labelAttributes.height + 16 + attributes.height + 8
        
    }

    function openMenu() {
        menu.open();
    }

    Menu {
        id: menu
        visualParent: parent

        MenuLayout {
            MenuItem { text: "Open Website"; onClicked: { Qt.openUrlExternally(currentGeocache.url); } }
            MenuItem { text: "Settings"; onClicked: { showSettings(); } }
        }
    }
}

