#!/bin/env python3

if __name__ == '__main__':
    from server.constants import SERVER_PORT
    from server.app import app
    from server.global_data import GLOBAL_DATA
    import atexit
    GLOBAL_DATA.reload_from_file("data.json")
    atexit.register(lambda: GLOBAL_DATA.to_file('data.json'))
    app.run(host="0.0.0.0", port=SERVER_PORT)
