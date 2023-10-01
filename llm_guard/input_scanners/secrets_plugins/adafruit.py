"""
This plugin searches for Adafruit keys
"""
import re

from detect_secrets.plugins.base import RegexBasedDetector


class AdafruitKeyDetector(RegexBasedDetector):
    """Scans for Adafruit keys."""

    secret_type = "Adafruit API Key"

    denylist = [
        re.compile(
            r"""(?i)(?:adafruit)(?:[0-9a-z\-_\t .]{0,20})(?:[\s|']|[\s|"]){0,3}(?:=|>|:{1,3}=|\|\|:|<=|=>|:|\?=)(?:'|\"|\s|=|\x60){0,5}([a-z0-9_-]{32})(?:['|\"|\n|\r|\s|\x60|;]|$)"""
        ),
    ]
