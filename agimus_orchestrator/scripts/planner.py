class PlannerParameters:
    """Class for defining parameters of the planner."""
    pass

class Planner:
    def __init__(self, param: PlannerParameters):
        """Initialize the planner."""
        self.param = param  # Store the parameters passed during initialization
