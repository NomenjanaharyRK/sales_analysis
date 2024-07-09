class CorrrelationAnalyzer:
    def __init__(self, data):
        self.data = data

    def calculate_correlation(self):
        correlation_matrix = self.data.corr()
        return correlation_matrix