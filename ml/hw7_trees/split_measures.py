import numpy as np


def evaluate_measures(sample):
    total_samples = len(sample)

    # Calculate Gini impurity
    unique_classes, class_counts = np.unique(sample, return_counts=True)
    gini = 1.0 - np.sum((class_counts / total_samples) ** 2)

    # Calculate Entropy
    entropy = -np.sum((class_counts / total_samples) *
                      np.log(class_counts / total_samples))

    # Calculate Classification Error
    majority_class_count = np.max(class_counts)
    error = 1.0 - (majority_class_count / total_samples)

    measures = {'gini': gini, 'entropy': entropy, 'error': error}
    return measures
