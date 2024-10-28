import pyads
from pyads.testserver import AdvancedHandler, PLCVariable, AdsTestServer, AmsHeader
from pyads import constants
import threading
import time

def start_server():
    handler = AdvancedHandler()

    test_var = PLCVariable(
        "Main.my_var", bytes(8), ads_type=constants.ADST_REAL64, symbol_type="LREAL"
    )
    handler.add_variable(test_var)

    # Start the server
    server = AdsTestServer(handler, port=48898, ip_address="127.0.0.1", logging=True)
    server.run()
    print("Test server started with AdvancedHandler on 127.0.0.1:48898")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        server.stop()
        print("Server stopped")

server_thread = threading.Thread(target=start_server)
server_thread.start()

time.sleep(1)

