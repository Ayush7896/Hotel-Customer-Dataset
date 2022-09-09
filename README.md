# Hotel-Customer-Dataset
Part 1
Write a regex to extract all the numbers with orange color background from the below text in italics.

{"orders":[{"id":1},{"id":2},{"id":3},{"id":4},{"id":5},{"id":6},{"id":7},{"id":8},{"id":9},{"id":10},{"id":11},{"id":648},{"id":649},{"id":650},{"id":651},{"id":652},{"id":653}],"errors":[{"code":3,"message":"[PHP Warning #2] count(): Parameter must be an array or an object that implements Countable (153)"}]}

solution colab file : https://colab.research.google.com/drive/1lKDJDvNxcJHhZjZ1oUjZ5up_7G-Yv-DN?usp=sharing

Part 2 
Here is the data set that contains the history of customer booking in a hotel.

There are three sections in this part
1. Train a machine learning model (preferably with a neural network) that 
predicts the customer who is going to be checked in. Once done, please test 
the prediction with below test data.

2. Do a thorough analysis on the results and the dataset with visualizations (please feel free to add creative ways of visualization here).

3. Host/Deploy the results using any hosting service you want (streamlit/flask)

solution colab file - https://colab.research.google.com/drive/1lKDJDvNxcJHhZjZ1oUjZ5up_7G-Yv-DN?usp=sharing
Web app link: https://hotel3.herokuapp.com/

Bonus Questions
Ques 1 Write about any difficult problem that you solved. (According to us difficult - is something which 90% of people would have only 10% probability in getting a similarly good solution). 

Answer1 The project which I made called Sarcasm detection on Reddit Datset.Since the sarcasm is very subjective matter,the sarcasm for some peopl may not be sarcasm for another set of people.
I have achieved the accuracy of 0.77 using distilBERT. The accuracy most of the people is getting is less than 0.70
Blog link :-https://medium.com/@akwsir96/sarcasm-detection-using-reddit-dataset-951e87b37f04

Ques 2 Explain back propagation and tell us how you handle a dataset if 4 out of 30 parameters have null values more than 40 percentage
Answer 2 Backpropagation is an algorithm to update/fine-tune weights and improve the accuracy of the model.It computes the gradient of loss function with respect to the weigths of the network. There are 2 parts to this algorithm.
1. Forward Propagation
2. Backward Propagation

For the second part there are various methods we can implement:
1. If the dataset is large we can drop null values.
2. If the dataset is small we can impute using mean,median,mode.
3. We can also impute by model based imputaion using k means.

