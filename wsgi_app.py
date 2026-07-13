"""WSGI entry point for LazyOwnInfiniteStorage web server."""

import os
from lazyown_infinitestorage import LazyOwnInfiniteStorage, LazyOwnConfig


def get_wsgi_app():
    """Factory function returning a gunicorn-compatible Flask application."""
    config = LazyOwnConfig()
    storage = LazyOwnInfiniteStorage(config)
    runner = storage.create_web_runner()
    runner.run_setup()
    os.makedirs(config.WEB_UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(config.WEB_DOWNLOAD_FOLDER, exist_ok=True)
    return runner._app


application = get_wsgi_app()
app = application