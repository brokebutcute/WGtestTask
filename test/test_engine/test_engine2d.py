import pytest
from twoDEngine.src.Engine2D import Engine2D
from twoDEngine.src.model.Color import Color
from twoDEngine.src.model.Canvas import Canvas
from twoDEngine.src.model.shapes.Shape import Shape


# Mock Shape class for testing
class MockShape(Shape):

    def draw(self, canvas):
        pass


# Define a fixture to create an Engine2D instance with default values
@pytest.fixture
def engine():
    return Engine2D()


# Test the initialization of Engine2D with default values
def test_engine2d_init_default(engine):
    assert engine.current_color.__eq__(Color(0, 0, 0))
    assert engine.current_canvas.get_size() == (100, 100)


# Test the initialization of Engine2D with custom values
def test_engine2d_init_custom():
    custom_color = Color(255, 0, 0)
    custom_canvas = Canvas(200, 150)
    engine = Engine2D(custom_canvas, custom_color)
    assert engine.current_color.__eq__(custom_color)
    assert engine.current_canvas == custom_canvas


def test_engine2d_draw(engine, mocker):
    # Mock Canvas and add a mock shape
    mock_canvas = mocker.Mock(spec=Canvas)
    mock_canvas.get_shapes_list.return_value = [MockShape(100, 100, Color(0, 0, 0))]
    engine.current_canvas = mock_canvas

    # Mock the Shape's draw method
    mocker.patch.object(MockShape, 'draw')

    engine.draw(mock_canvas)

    # Verify that draw was called on the mock shape
    MockShape.draw.assert_called_once_with(engine, mock_canvas)
    mock_canvas.clear_canvas.assert_called_once()


# Test the set_color method
def test_engine2d_set_color(engine):
    new_color = Color(0, 255, 0)
    engine.set_color(new_color)
    assert engine.current_color.__eq__(new_color)

