from prodraw.shapes import Shape


class Add:
    """Handles the addition of shape objects to a list."""

    @staticmethod
    # Returns an event handler to append a valid shape to the figures list
    def add(obj, figures: list):

        # Appends the shape object to the list when the event triggers
        def add_shape(event):
                if obj['obj'].end_x is not None and obj['obj'] is not None:
                    figures.append(obj['obj'])
        
        return add_shape