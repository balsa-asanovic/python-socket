# A simple Python/Flask Websocket using SocketIO

This is a simple implementation of a websocket using Flask/Python and SocketIO, which sends a randomized value to a React app (found [here](https://github.com/balsa-asanovic/3d-rotation)) through a websocket.

## Code

The server has a couple of socket actions:

* Connect: The moment the user connects to the socket, emitting starts.
* Disconnect: When the user disconnects, the emitting is stopped.
* Frequency: Used to adjust the frequency of emitting.
* Stop: Used to stop the emitter while still being connected.

## Getting Started

To run the project locally:

1. Clone this repository.
2. Navigate to the project directory in your terminal.
3. Make sure you have Python 3+ installed.
4. Install dependencies from the `requirements.txt` file.
5. Run `python server.py` command.


Please let me know if you have any further suggestions or if there's anything else I can help with!
