class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_more(self, expected, actual, message=None):
        if expected > actual:
            self._add_error(message if message is not None else f"Expected: {expected}, Actual: {actual}")


    def assert_less(self, expected, actual, message=None):
        if expected < actual:
            self._add_error(message if message is not None else f"Expected: {expected}, Actual: {actual}")



    def assert_equal(self, expected, actual, message=None):
        if expected != actual:
            self._add_error(message if message is not None else f"Expected: {expected}, Actual: {actual}")

    def assert_true(self, condition, message=None):
        if not condition:
            self._add_error(message if message is not None else "Condition is not True")

    def assert_false(self, condition, message=None):
        if condition:
            self._add_error(message if message is not None else "Condition is not False")

    def _add_error(self, error_message):
        self.errors.append(error_message)

    def assert_all(self):
        if self.errors:
            error_message = "\n".join(self.errors)
            raise AssertionError("SoftAssert errors:\n" + error_message)
