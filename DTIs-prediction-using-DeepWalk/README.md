# Predicting drug-target interactions(DTIs)

The diagnosis of drug-target interaction is an important step in the discovery of drugs. In this project, we do this by using the DeepWalk algorithm. The data collection we used in this experiment is DrugBank. This database contains 7721 drugs and 4960 targets which give us much information about the chemical structure of drugs and other elements and their connections.

## Download Dataset
* We downloaded drugBank dataset from https://www.drugbank.ca/releases/latest

## Prepare data
* Since the dataset is an XML file, we had to extract information about drugs from it. To do this, we extracted our data by using parse.ipynb file.

* We need only two columns of this CSV file that contains drug_id and uniprot_id. Each drug has a unique uniprot_id, while it isn't a number. We generated numbers for each drug_id and uniprot_id. Then, we added a fixed amount(equal to the count of drugs) to each of the numbers determined for targets. Finally, we generated negative label data equal to the number of main data.

## Apply Deepwalk algorithm
* In this step, we applied the deepWalk algorithm to the data. This algorithm is used to represent our network in a lower space (in this case, 64-dimensional). The output file is derived from some of representative vectors.  

## Create dataset
In this step, we used one of the items below to convert two vectors(one for drug and another for the related target) of each row to one vector:
- Summation
- Average
- Concatenation

 We used Summation operator to add two vectors. Thus we created our dataset. Each row contains drug _id, target _id, label and the result vector.
 
## Use SVM as a classifier
* In the final step, we used SVM(Support Vector Machine) for classifying DTIs. Initial precision without adjusting SVM hyperparameters is 63%.
# DTIs-prediction-by-DeepWalk-on-DrugBank
