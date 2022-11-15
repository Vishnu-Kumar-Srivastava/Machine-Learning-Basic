#This code is made by Vishnu Kumar Srivastava
# Roll no. 102118066.

import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

number_of_classes=int(input("Enter number of classes "))
dataset_size=int(input("Enter size of dataset "))
actual= np.random.randint(0,number_of_classes,dataset_size)
print(actual)
print("Generating random predictions....")
predicted=np.random.randint(0,number_of_classes,dataset_size)
print(predicted)

zero_matrix=[[0 for a in range(number_of_classes)] for a in range(number_of_classes)]
for i,j in zip(actual,predicted):
        if i==j :
            zero_matrix[i][j] = zero_matrix[i][j]+1
        else:
            zero_matrix[j][i] = zero_matrix[j][i]+1           

cm=pd.DataFrame(zero_matrix,index=[i for i in range(number_of_classes)],columns=[i for i in range(number_of_classes)])
plt.figure(figsize=(10,7))
sn.heatmap(cm,annot=True,cmap="viridis",linewidths=1)
plt.xlabel("Actual Value")
plt.ylabel("Predicted value")
plt.suptitle("Note: Predictions are randomly generated, hence this confusion matrix do not resemble actual scenerio.",fontsize=10)
plt.title("Confusion Matrix")
plt.show()

preci_sion=0 #
reca_ll_score_=0 #
for class_number in range(number_of_classes):
    tp=zero_matrix[class_number][class_number]

    fn_list=[]
    for i in range(number_of_classes):
        if(i != class_number):
            fn_list.append(zero_matrix[i][class_number])
    fn=sum(fn_list)

    fp_list=[]
    for i in range(number_of_classes):
        if(i != class_number):
            fp_list.append(zero_matrix[class_number][i])
    fp=sum(fp_list)
    
    tn=dataset_size-tp-fp-fn
    accuracy=float(tp+tn/dataset_size)
    print(f"The accuracy of class {class_number} is ",accuracy)

    try:
        precision=float(tp/tp+fp)
        preci_sion=precision
        print(f"The precision of class {class_number} is ",precision)
    except ZeroDivisionError :
        print(f"Precision of class {class_number} is not defined (Division by zero!)")

    try:
        recall_score=float(tp/tp+fn)
        reca_ll_score_=recall_score
        print(f"The recall_score of class {class_number} is ",recall_score)
    except ZeroDivisionError:
        print(f"Recall of class {class_number} is not defined (Division by zero!)")

    try:
        f1_score=float((2*preci_sion*reca_ll_score_)/(preci_sion+reca_ll_score_))
        print(f"The f1_score of class {class_number} is ",f1_score)
    except ZeroDivisionError:
        print(f"F1 score of class {class_number} is not defined (Division by zero!)")
    print("")

print("--------------END---------------")








