#!/bin/bash

# Run the Spark program 10 times with seeds 1-10
# Save accuracy and runtime output to CSV

SCRIPT="decision_tree.py"
INPUT_PATH="hdfs:///user/huangjixu/427_final/input/kdd.data.txt"

OUTPUT_FILE="decision_tree_results.csv"

# Header
echo "Seed,Train_Accuracy,Test_Accuracy,Time" > "$OUTPUT_FILE"

# Loop 10 times
for SEED in {1..10}
do
  echo "========== Running seed $SEED =========="
  
 
  FULL_OUTPUT=$(spark-submit "$SCRIPT" "$SEED" "$INPUT_PATH")
  echo "$FULL_OUTPUT"

  
  RESULT=$(echo "$FULL_OUTPUT" | grep "Decision Tree")

  
  TRAIN_ACC=$(echo "$RESULT" | awk -F'Train Accuracy: ' '{print $2}' | awk -F' -' '{print $1}')
  TEST_ACC=$(echo "$RESULT" | awk -F'Test Accuracy: ' '{print $2}' | awk -F' -' '{print $1}')
  TIME=$(echo "$RESULT" | awk -F'Time: ' '{print $2}' | awk -F' sec' '{print $1}')

  echo "$SEED,$TRAIN_ACC,$TEST_ACC,$TIME" >> "$OUTPUT_FILE"
done

echo "All runs complete. Results saved in $OUTPUT_FILE"

