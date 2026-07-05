from prodraw.shapes import Shape


class Add:
    """Handles the addition of shape objects to a list."""

    @staticmethod
    # Returns an event handler to append a valid shape to the figures list
    def add(obj, figures: list):

        # Appends the shape object to the list when the event triggers
        def add_shape(event):
            if abs(obj["obj"].end_y-obj["obj"].start_y)>5 and abs(obj["obj"].end_x-obj["obj"].start_x)>5:
                figures.append(obj['obj'])

        return add_shape
