"""
Configuration file management for the application. See example-config.xml for details
"""

# config/config.py
from pathlib import Path

# Always relative to this file's location
BASE_DIR = Path(__file__).parent
CONFIG_PATH = BASE_DIR / "config.xml"