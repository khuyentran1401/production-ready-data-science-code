# Chapter 11: Data Version Control

Transform your data science projects with reproducible data management and ML pipelines using DVC.

← [Back to Main README](../README.md)

## Setup

```bash
# From project root
uv sync --group chapter11
```

## Complete DVC Workflow

This chapter demonstrates a complete customer churn prediction project using DVC for:
- **Data versioning**: Track and switch between dataset versions
- **Remote storage**: Share large datasets efficiently  
- **Reproducible pipelines**: Automate ML workflows
- **Experiment tracking**: Compare model performance across runs


## Tutorial: Customer Churn Prediction with DVC

### 1. Initialize the Project

```bash
# Initialize DVC (run once per project)
uv run dvc init
git add .dvc/
git commit -m "Initialize DVC"

# Track initial dataset
uv run dvc add data/raw/customer_churn.csv
git add data/raw/customer_churn.csv.dvc .gitignore
git commit -m "Add customer churn dataset"
```

**What just happened?**
- DVC created `.dvc/` directory with configuration
- `customer_churn.csv.dvc` contains metadata about your dataset
- `data/raw/` was added to `.gitignore`
- Git tracks only metadata, not the actual large files

### 2. Build Reproducible ML Pipeline

Our pipeline has 4 stages: prepare → featurize → train → evaluate

```bash
# Run the complete pipeline
uv run dvc repro
```

**Pipeline benefits:**
- Only modified stages re-run (smart caching)
- All outputs automatically tracked and versioned
- Reproducible across different machines

### 3. Work with Data Versions

**Scenario**: Your team receives updated customer data with additional features.

```bash
# Simulate new data arrival (example)
# In practice, you'd receive new data files
echo "customer_id,age,tenure,monthly_charges,total_charges,churn
1001,25,12,65.5,786.0,0
1002,45,24,89.2,2140.8,1
1003,32,6,45.0,270.0,0" > data/raw/customer_churn_v2.csv

# Replace with new version
cp data/raw/customer_churn_v2.csv data/raw/customer_churn.csv

# Track new version
uv run dvc add data/raw/customer_churn.csv
git add data/raw/customer_churn.csv.dvc
git commit -m "Update to customer data v2"

# Re-run pipeline with new data
uv run dvc repro
```

**Switch between data versions:**
```bash
# Go back to version 1
git checkout HEAD~1
uv run dvc checkout

# Return to version 2  
git checkout main
uv run dvc checkout
```

### 4. Remote Storage and Team Collaboration

**Setup local remote storage (for testing):**
```bash
# Configure remote storage
mkdir /tmp/dvc-storage
uv run dvc remote add -d storage /tmp/dvc-storage
git add .dvc/config
git commit -m "Configure DVC remote"

# Push data to remote
uv run dvc push
```

**Team member workflow:**
```bash
# New team member joins
git clone <repository>
cd chapter11_data_version_control

# Install dependencies
uv sync --group chapter11

# Pull data from remote
uv run dvc pull

# Reproduce results
uv run dvc repro
```

### 5. Experiment with Parameters

**Modify hyperparameters** in `params.yaml`:
```yaml
model:
  n_estimators: 200  # changed from 100
  max_depth: 10      # changed from 5
```

**Run experiment:**
```bash
uv run dvc repro
```

**Compare results:**
```bash
uv run dvc metrics show
uv run dvc metrics diff HEAD~1
```

### 6. Pipeline Management

**Useful DVC commands:**
```bash
# Visualize pipeline
uv run dvc dag

# Check pipeline status
uv run dvc status

# Force re-run specific stage
uv run dvc repro --force train
```

## Advanced: Cloud Storage (Optional)

**AWS S3 setup:**
```bash
# Configure AWS credentials first
aws configure

# Add S3 remote
uv run dvc remote add -d s3remote s3://my-dvc-bucket/dvc-store
git add .dvc/config
git commit -m "Add S3 remote"

# Push to S3
uv run dvc push
```

## Key Benefits Demonstrated

1. **Reproducibility**: Anyone can recreate exact results
2. **Efficiency**: Smart caching prevents unnecessary recomputation  
3. **Collaboration**: Team members work with identical data
4. **Experimentation**: Easy parameter testing and comparison
5. **Storage**: Keep Git repository lightweight while tracking large datasets

---

## Why This Matters

Data version control eliminates reproducibility nightmares, enables efficient data pipeline management, and ensures teams can collaborate confidently with large datasets while maintaining Git repository performance.