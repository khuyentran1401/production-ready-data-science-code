from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, train_test_split


def train_model(X, y):
    """Train a model and return model with test data."""
    print("Training model...")
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print(f"Model trained on {len(X_train)} samples")
    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    """Evaluate the model and return accuracy."""
    print("Evaluating model...")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model accuracy: {accuracy:.3f}")
    return accuracy


def cross_validate(model, X, y, cv=5):
    """Perform cross-validation on the model."""
    print(f"Performing {cv}-fold cross-validation...")
    scores = cross_val_score(model, X, y, cv=cv)
    mean_score = scores.mean()
    std_score = scores.std()
    print(f"Cross-validation scores: {scores}")
    print(f"Mean CV accuracy: {mean_score:.3f} (+/- {std_score * 2:.3f})")
    return mean_score, std_score
