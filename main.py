import threading
import startRando
import background
import variableManagment
import gui

# Create thread for background loop
exitEvent = threading.Event()
background_thread = threading.Thread(target=background.backgroundLoop, args=(exitEvent,))
startRando.background_thread = background_thread

# Start the GUI
gui.userGUILoop(startRando.startRando, background.change_saved_location)
exitEvent.set()
