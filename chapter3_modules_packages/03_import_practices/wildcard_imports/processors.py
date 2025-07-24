

class SimpleImputer:
    """Custom SimpleImputer class for demonstration purposes."""

    def __init__(self, strategy="mean"):
        self.strategy = strategy
        self.fill_value_ = None

    def fit(self, X):
        """Learn the fill value from the data."""
        if self.strategy == "mean":
            self.fill_value_ = X.mean()
        elif self.strategy == "median":
            self.fill_value_ = X.median()
        elif self.strategy == "mode":
            self.fill_value_ = X.mode().iloc[0]
        return self

    def transform(self, X):
        """Fill missing values with the learned fill value."""
        return X.fillna(self.fill_value_)

    def fit_transform(self, X):
        """Fit and transform in one step."""
        return self.fit(X).transform(X)

    def __repr__(self):
        return f"processors.SimpleImputer(strategy='{self.strategy}')"


def custom_scaler(data):
    """Custom scaling function."""
    return (data - data.min()) / (data.max() - data.min())
