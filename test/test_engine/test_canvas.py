import pytest

from unittest.mock import Mock
from twoDEngine.src.model.Canvas import Canvas
from twoDEngine.src.model.Color import Color


def test_canvas_init_default():
    canvas = Canvas(100, 100)
    assert canvas.get_size() == (100, 100)
    assert canvas.get_color().__eq__(Color(255, 255, 255))


def test_canvas_init_custom_color():
    custom_color = Mock()
    canvas = Canvas(100, 100, custom_color)
    assert canvas.get_color() == custom_color


def test_canvas_add_shape():
    canvas = Canvas(100, 100)
    mock_shape = Mock()
    canvas.add_shape(mock_shape)
    assert mock_shape in canvas.get_shapes_list()


def test_canvas_clear_canvas():
    canvas = Canvas(100, 100)
    mock_shape = Mock()
    canvas.add_shape(mock_shape)
    canvas.clear_canvas()
    assert len(canvas.get_shapes_list()) == 0
