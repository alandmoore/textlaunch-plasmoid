PLASMOID_NAME=textlaunch

zip -r ../$PLASMOID_NAME.plasmoid . -x '*.git/*'
plasmapkg -r $PLASMOID_NAME
plasmapkg -i ../$PLASMOID_NAME.plasmoid

sleep 4 
plasmoidviewer $PLASMOID_NAME
