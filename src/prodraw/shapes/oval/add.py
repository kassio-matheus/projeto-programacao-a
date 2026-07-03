from prodraw.shapes import Shape


class Add:

    @staticmethod
    def add(obj, figures: list):

        def add_shape(event):
                if obj['obj'].end_x is not None and obj['obj'] is not None:
                    figures.append(obj['obj'])
        

        
        return add_shape
    
