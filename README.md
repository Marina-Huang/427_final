
# Decision Tree Classification with PySpark

This project implements a Decision Tree classifier using PySpark on the KDD dataset. It is designed to evaluate the model’s performance (accuracy and runtime) across different random seeds to assess its robustness and stability.

---

## Files

- `decision_tree.py`: Python script that trains and evaluates a Decision Tree classifier using PySpark.  
- `run_10_times.sh`: Bash script to run `decision_tree.py` 10 times with different random seeds.  
- `decision_tree_results.csv`: Output file recording the accuracy and runtime for each run.

---

## Environment & Dependencies

- Spark 3.5.1
- Python 3.9+
- Run on ECS Hadoop/Spark cluster at Victoria University of Wellington

---
## Dataset

The dataset used is `kdd.data.txt`, uploaded to HDFS:
```
hdfs dfs -mkdir -p /user/<your_username>/427_final/input
hdfs dfs -put kdd.data.txt /user/<your_username>/427_final/input/
```
---

## Input Data

The model expects a CSV file in HDFS at the following path:

```
hdfs:///user/huangjixu/427_final/input/kdd.data.txt
```

Make sure the file exists before running the scripts:

```bash
hdfs dfs -ls /user/huangjixu/427_final/input
```

---

## How to Run

### 1. Make the shell script executable

```bash
chmod +x run_10_times.sh
```

### 2. Run the script

```bash
./run_10_times.sh
```

This will:
- Execute `decision_tree.py` 10 times using seeds from 1 to 10.  
- Append each run's accuracy and runtime to `decision_tree_results.csv`.

---

## Output Example

The program outputs the accuracy and runtime of the Decision Tree model for each of the 10 runs using different random seeds. Each line of output includes:

Seed value

Training accuracy

Testing accuracy

Time taken for that run (in seconds):

```
Seed,TrainAccuracy,TestAccuracy,Time
1,0.9470,0.9455,4.08
...

...
```

---

## Model Details

- **Model**: `DecisionTreeClassifier` from PySpark MLlib  
- **Feature Handling**:  
  - Input file is read with `inferSchema=True`  
  - `StringIndexer` encodes the class label  
- **Train/Test Split**: 70/30 (controlled by seed)  
- **Evaluation Metric**: Accuracy  
- **Performance Metric**: Execution time (in seconds)  

---

## Results Summary (based on 10 seeds)

| Metric         | Value        |
|----------------|--------------|
| Avg. Accuracy  | ~94.45%      |
| Max Accuracy   | ~94.60%      |
| Min Accuracy   | ~94.30%      |
| Avg. Runtime   | ~3.45 sec    |

---
## Summary Statistics
After all 10 runs, you can compute summary statistics (min, max, average, std) using a Python script or pandas.

## Notes
- Ensure Spark and Hadoop are correctly set up on the cluster

- Set executable permissions for .sh files using chmod +x run_10_times.sh
"""
```
readme_path = Path("/mnt/data/README.md")
readme_path.write_text(readme_content)
readme_path
```
## Observations

- Accuracy remains stable across seeds, suggesting good generalisability.  
- Runtime is efficient — Spark handles the dataset well in distributed mode.  
- No parameter tuning yet — further improvement is possible.

---



