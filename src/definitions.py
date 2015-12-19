

class Definitions:

    STREAM_SOURCE_FILE = "streams.source"
    STREAM_SELECTION_FILE = "streams.selection"
    DEFAULT_CONFIG_FILE = "default.conf"
    SHUTDOWN_COMMAND = "shutdown -h now"
    RC_HOST = "localhost:8080"
    HTTP_SRC = ""
    HTTP_HOST = "localhost:80"
    HTTP_PASSWORD = "admin"
    HTTP_PORT = "80"
    VLC = "cvlc"
    VLC_START_COMMAND = (VLC +
                         " -I http"
                         " --extraintf rc "
                         " --rc-host " +RC_HOST+
                         " --http-src "+ HTTP_SRC +
                         " --http-password "+HTTP_PASSWORD+
                         " --http-host "+HTTP_HOST+
                         " --http-port "+HTTP_PORT)
