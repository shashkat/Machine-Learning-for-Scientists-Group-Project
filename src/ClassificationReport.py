import numpy as np

# Create a class to handle all the metrics for our classification tasks
class ClassificationMetrics:
    def __init__(self, true_labels, pred_labels):
        self.true_labels = true_labels  # Keep track of the real labels
        self.pred_labels = pred_labels  # And what our model predicted
        # Get all unique classes involved to ensure our matrix covers everything
        self.classes = np.unique(np.concatenate([self.true_labels, self.pred_labels]))

        # Automatically build the confusion matrix when we make a new object
        self.cm = self.confusion_matrix()  

    # Calculate precision, which helps us see the accuracy of the positive predictions
    def calculate_precision(self, tp, fp):
        if (tp + fp) > 0:  # Make sure we don't divide by zero!
            return tp / (tp + fp)
        else:
            return 0 

    # Calculate recall to check how many actual positives were caught
    def calculate_recall(self, tp, fn):
        if (tp + fn) > 0:  # Again, avoiding division by zero
            return tp / (tp + fn)
        else:
            return 0

    # F1 score combines precision and recall into a single metric
    def calculate_f1_score(self, precision, recall):
        if (precision + recall) > 0:  # We need positive precision and recall to calculate F1
            return 2 * (precision * recall) / (precision + recall)
        else:
            return 0  # F1 is zero if either precision or recall is zero

    # Accuracy tells us the overall performance across all classes
    def calculate_accuracy(self):
        correct_predictions = np.sum(self.true_labels == self.pred_labels)
        return correct_predictions / len(self.true_labels)

    def confusion_matrix(self):
        class_index = {k: i for i, k in enumerate(self.classes)}  # Map each class to an index
        # Start with an all-zero matrix
        matrix = np.zeros((len(self.classes), len(self.classes)), dtype=int)
        for true, pred in zip(self.true_labels, self.pred_labels):
            # Fill in the matrix based on predictions
            matrix[class_index[true]][class_index[pred]] += 1
        return matrix

    # Generate a report based on the metrics
    def report(self):
        print(f"{'Class':<30}{'Precision':<10}{'Recall':<10}{'F1-Score':<10}")
        for i, class_name in enumerate(self.classes):
            tp = self.cm[i, i]  # True positives are diagonal elements of the matrix
            fp = np.sum(self.cm[:, i]) - tp  # False positives are the column sums minus TP
            fn = np.sum(self.cm[i, :]) - tp  # False negatives are the row sums minus TP
            # Calculate metrics for each class
            precision = self.calculate_precision(tp, fp)
            recall = self.calculate_recall(tp, fn)
            f1_score = self.calculate_f1_score(precision, recall)
            # Output each class's metrics
            print(f"{class_name:<30}{precision:<10.2f}{recall:<10.2f}{f1_score:<10.2f}")
        # Print the overall accuracy of the model
        print(f"\n{'Overall Accuracy:':<30}{self.calculate_accuracy():.2f}")