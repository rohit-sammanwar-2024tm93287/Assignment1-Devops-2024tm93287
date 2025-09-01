# app/__init__.py

from .app import create_app  # re-export the factory for easy imports

__all__ = ["create_app"]
__version__ = "0.1.0"
