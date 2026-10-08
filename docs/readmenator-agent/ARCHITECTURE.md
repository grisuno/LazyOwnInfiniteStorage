# Architecture

## Internal Dependencies

- `skill_lazyown_infinitestorage/tools.py` -> `lazyown_infinitestorage.py`
- `tests/test_error_correction.py` -> `lazyown_infinitestorage.py`
- `tests/test_frames.py` -> `lazyown_infinitestorage.py`
- `tests/test_integration.py` -> `lazyown_infinitestorage.py`
- `tests/test_protocols.py` -> `lazyown_infinitestorage.py`
- `tests/test_security.py` -> `lazyown_infinitestorage.py`
- `wsgi_app.py` -> `lazyown_infinitestorage.py`

## External Imports

- `lazyown_infinitestorage.py` -> PyQt5.QtCore, PyQt5.QtWidgets, argparse, binascii, cv2, flask, hashlib, json, math, numpy, os, random, re, shutil, struct, subprocess, sys, tempfile, typing
- `skill_lazyown_infinitestorage/tools.py` -> os, selenium, selenium.webdriver.chrome.service, selenium.webdriver.common.by, selenium.webdriver.support, selenium.webdriver.support.ui, subprocess, sys, time, typing
- `tests/test_error_correction.py` -> pytest
- `tests/test_frames.py` -> numpy, pytest
- `tests/test_integration.py` -> hashlib, io, os, pytest, random, subprocess, tempfile
- `tests/test_protocols.py` -> pytest
- `tests/test_security.py` -> os, pytest
- `wsgi_app.py` -> os
