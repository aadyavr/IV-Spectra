class Pipeline:

    def __init__(self):
        pass

    def process(self, voltage, current):

        results = {
            "voltage": voltage,
            "current": current,
            "background": None,
            "residual": None,
            "noise": None,
            "telegraph": None,
            "step_indices": None,
            "transition_voltages": None
        }

        return results
