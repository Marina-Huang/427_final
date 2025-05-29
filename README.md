
# Decision Tree Classification with PySpark

This project implements a Decision Tree classifier using PySpark on the KDD dataset. It is designed to evaluate the model’s performance (accuracy and runtime) across different random seeds to assess its robustness and stability.

---

## Files

- `decision_tree.py`: Python script that trains and evaluates a Decision Tree classifier using PySpark.  
- `run_10_times.sh`: Bash script to run `decision_tree.py` 10 times with different random seeds.  
- `decision_tree_results.csv`: Output file recording the accuracy and runtime for each run.

---

## Environment & Dependencies

- **Apache Spark 3.5.1**  
- **Python 3.x**  
- PySpark (should be available with Spark)  
- HDFS (Hadoop) access to input file  

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

Example content of `decision_tree_results.csv`:

```
Seed,Accuracy,Time
1,0.9447,3.43
2,0.9453,3.41
3,0.9440,3.38
4,0.9449,3.51
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

## bservations

- Accuracy remains stable across seeds, suggesting good generalisability.  
- Runtime is efficient — Spark handles the dataset well in distributed mode.  
- No parameter tuning yet — further improvement is possible.

---



