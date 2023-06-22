import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing, feature_selection, decomposition
import warnings
warnings.filterwarnings('ignore') # ignores warning about too small number of bins in feature selection


file_path = 'glass+identification/glass.data'
df = pd.read_csv(file_path, header=None)
header = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']
df.columns = header


def divide_data():
    values = df.drop('Type', axis=1)
    labels = df['Type']
    train_values, test_values, train_labels, test_labels = train_test_split(values, labels, test_size=0.14, random_state=42)
    return train_values, test_values, train_labels, test_labels


def create_data_processings():
    processings = [
        ('normalization', preprocessing.MinMaxScaler()),
        ('standarization', preprocessing.StandardScaler()),
        ('discretization', preprocessing.KBinsDiscretizer(n_bins=10, encode='ordinal')),
        ('feature_selection', feature_selection.SelectKBest(feature_selection.chi2, k=1)),
        ('PCA', decomposition.PCA(n_components=1)),
        ('no_processing', None)
    ]
    return processings


def process_data(train_values, test_values, processing):
    if processing != None:
        return processing.fit_transform(train_values), processing.transform(test_values)
    else:
        return train_values, test_values


def process_data_feature_selection(train_values, test_values, train_labels, processing):
    return processing.fit_transform(train_values, train_labels), processing.transform(test_values)


def train_decision_tree(train_values, train_labels):
    decision_tree_model = DecisionTreeClassifier(min_impurity_decrease=0.0, max_depth=5, min_samples_leaf=3)
    decision_tree_model.fit(train_values, train_labels)
    return decision_tree_model


def test_decision_tree(train_values, test_values, train_labels, test_labels):
    for processing_name, processing in create_data_processings():
        if processing_name == 'feature_selection':
            train_values_processed, test_values_processed = process_data_feature_selection(
                train_values, test_values, train_labels, processing)
        else:
            train_values_processed, test_values_processed = process_data(train_values, test_values, processing)
        
        print('decision tree - ' + processing_name + '; score: ', end='')
        decision_tree_model = train_decision_tree(train_values_processed, train_labels)
        predicted_labels = decision_tree_model.predict(test_values_processed)
        score = accuracy_score(test_labels, predicted_labels)
        print(score)


def train_naive_bayes(train_values, train_labels):
    naive_bayes = GaussianNB()
    naive_bayes.fit(train_values, train_labels)
    return naive_bayes


def test_naive_bayes(train_values, test_values, train_labels, test_labels):
    for processing_name, processing in create_data_processings():
        if processing_name == 'feature_selection':
            train_values_processed, test_values_processed = process_data_feature_selection(
                train_values, test_values, train_labels, processing)
        else:
            train_values_processed, test_values_processed = process_data(train_values, test_values, processing)
        
        print('naive bayes - ' + processing_name + '; score: ', end='')
        naive_bayes = train_naive_bayes(train_values_processed, train_labels)
        predicted_labels = naive_bayes.predict(test_values_processed)
        score = accuracy_score(test_labels, predicted_labels)
        print(score)


if __name__ == '__main__':
    train_values, test_values, train_labels, test_labels = divide_data()
    test_naive_bayes(train_values, test_values, train_labels, test_labels)
    test_decision_tree(train_values, test_values, train_labels, test_labels)
