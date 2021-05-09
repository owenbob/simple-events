"""
Run  application instance or instances.
"""

from events import events_app

if __name__ == '__main__':
    events_app.run(port=5000)
