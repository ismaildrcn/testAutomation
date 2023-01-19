import pytest
from pytestqt.qtbot import QtBot
from PyQt5.QtCore import Qt

import mainWindow

@pytest.fixture
def app(qtbot: QtBot):
    window = mainWindow.Ui()
    window.show()
    qtbot.addWidget(window)

    return window

"""def test_label(app):
    assert app.labelFailOrSuccess.text() == "Fail Status","""

def test_label_after_click(app, qtbot):
    qtbot.mouseClick(app.pushButtonTestIt, Qt.LeftButton)
    assert app.labelFailOrSuccess.text() == "20"
