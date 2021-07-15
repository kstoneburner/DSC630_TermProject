# This is a consorted list of all the models for ease of access.
# Included are some cleaning methods also


def cat_input():
    from sklearn.model_selection import train_test_split
    print ("Naive Bayes: https://scikit-learn.org/stable/modules/naive_bayes.html")
    from sklearn import naive_bayes 
    
    print("See Also:\nFeature Selection:\nhttps://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_selection",
      "See Also: Chi-square test (p value or top N variables)\nCHAID tree stump using Chi-square test (p value or top N variables)\nAssociation Rules (Confidence, Support).")

    
def cat_output():
    print ("MLPClassifier: https://scikit-learn.org/stable/modules/neural_networks_supervised.html#multi-layer-perceptron")
    from sklearn.neural_network import MLPClassifier
    
    
def numerics():
    print ("OrdLeastSq: https://scikit-learn.org/stable/modules/linear_model.html#ordinary-least-squares")
    from sklearn import linear_model
    print ("MLPRegressor: https://scikit-learn.org/stable/modules/neural_networks_supervised.html#multi-layer-perceptron")
    from sklearn.neural_network import MLPRegressor
    print ("SVM: https://scikit-learn.org/stable/modules/svm.html#regression")
    from sklearn import svm
    print("Tree, 'clf' call: https://scikit-learn.org/stable/modules/tree.html#regression")
    from sklearn import tree
    clf = tree.DecisionTreeRegressor()
    clf = clf.fit(X, y)
    clf.predict()

    """
    # Still working on this one
    from sklearn.pipeline import make_pipeline
    est = make_pipeline(StandardScaler(), SGDClassifier())
    est.fit(X_train)
    est.predict(X_test)
    
    # Note:
    Also, implement GridSearch from sci-kit
    Also, learn gpu assist
    """