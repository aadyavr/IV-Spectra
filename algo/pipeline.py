class Pipeline:

    def __init__(self):
        print("Pipeline Initialized")

    def process(self, voltage, current):

        result = {

            "voltage": voltage,

            "current": current,

            "background": None,

            "residual": None,

            "noise": None,

            "telegraph": None,

            "step_indices": [],

            "transition_voltages": []

        }

        return resultv
