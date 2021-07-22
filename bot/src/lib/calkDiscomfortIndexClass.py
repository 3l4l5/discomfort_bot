class CalcDiscomfotIndexClass:
    def __init__(self, temp_dict):
        self.T = temp_dict["temp"][0]
        self.H = temp_dict["humidity"][0]

    def calk(self):
        return 0.81*self.T + 0.01*self.H * (0.99*self.T - 14.3) + 46.3