import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    data_root = "D:\pre"
    train = pd.read_csv("%s/user.csv"%data_root)

    # Process data into feature and label arrays
    #print("Processing {} samples with {} attributes".format(len(frame.index), len(frame.columns)))
    #X_train, X_test, y_train, y_test = get_features_and_labels(frame)
    
    # Evaluate multiple classifiers on the data
    #print("Evaluating classifiers")
    #results = list(evaluate_classifier(X_train, X_test, y_train, y_test))

    # Display the results

    # summarize the data
    #print (train.describe())

    # 查看每一列的标准差
    train.boxplot(column="education")
    plt.show()
    # 频率表，表示prestige与admin的值相应的数量关系
    #print (pd.crosstab(train['label'], train['creativeID'], rownames=['label']))
 
    # plot all of the columns
    #train.hist()
    #plt.plot()
    #plt.show()

    #print("Plotting the results")
    #plot(results)