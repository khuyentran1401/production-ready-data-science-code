"""Main pipeline execution script."""

from data_pipeline.data import load_data, preprocess_data
from data_pipeline.data.processor import split_data
from data_pipeline.models import ModelTrainer
from data_pipeline.utils import format_results


def main():
    """Execute the complete data pipeline."""
    print("🚀 Starting Data Pipeline")
    print("=" * 40)

    # 1. Load data
    print("\n📊 Loading data...")
    data = load_data("sample_data.csv")

    # 2. Preprocess data
    print("\n🔧 Preprocessing data...")
    X, y = preprocess_data(data)

    # 3. Split data
    print("\n✂️  Splitting data...")
    X_train, X_test, y_train, y_test = split_data(X, y)
    print(f"Training set: {len(X_train)} samples")
    print(f"Test set: {len(X_test)} samples")

    # 4. Train model
    print("\n🤖 Training model...")
    trainer = ModelTrainer()
    trainer.train(X_train, y_train)

    # 5. Evaluate model
    print("\n📈 Evaluating model...")
    accuracy = trainer.evaluate(X_test, y_test)
    feature_importance = trainer.get_feature_importance()

    # 6. Display results
    print("\n" + "=" * 40)
    print(format_results(accuracy, feature_importance))
    print("\n✅ Pipeline completed successfully!")


if __name__ == "__main__":
    main()
