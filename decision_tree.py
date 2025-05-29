

import sys
import time
from pyspark.sql import SparkSession
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Parameter: random seed
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 42
input_file = sys.argv[2] if len(sys.argv) > 2 else "kdd.data.txt"

# Start Spark session
spark = SparkSession.builder.appName("DecisionTree").getOrCreate()

# Load and preprocess the data
df = spark.read.csv(input_file, header=False, inferSchema=True, sep=",")
df = df.toDF(*[f"_c{i}" for i in range(41)] + ["label"])

# Encode label column
df = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(df).transform(df)

# Assemble all features into a single vector
df = VectorAssembler(inputCols=[f"_c{i}" for i in range(41)], outputCol="features").transform(df)

# Split the dataset into training and testing sets
train, test = df.randomSplit([0.7, 0.3], seed=seed)

# Train the Decision Tree model and evaluate it
start = time.time()
model = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="features").fit(train)

# Evaluate on test set
pred = model.transform(test)
evaluator = MulticlassClassificationEvaluator(labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
test_acc = evaluator.evaluate(pred)

# Evaluate on training set
train_pred = model.transform(train)
train_acc = evaluator.evaluate(train_pred)

# Output the result
print(f"Decision Tree - Seed {seed} - Train Accuracy: {train_acc:.4f} - Test Accuracy: {test_acc:.4f} - Time: {time.time() - start:.2f} sec")