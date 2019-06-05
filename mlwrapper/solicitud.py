class XGBModel:
    def __init__(self, booster, imputer, scaler, feature_importance):
        self.booster = booster
        self.imputer = imputer
        self.scaler = scaler
        self.feature_importance = feature_importance