from preprocess import read_data, create_samples, split_data
import numpy as np

# HYPERPARAMETERS
input_size = 50 #size of each word vector
output_size = 2 #number of classes
hidden_layer_size = 
learning_rate = 
number_of_epochs = 
path = "./data" #use relative path like this




def activation_function(layer):
	pass
 

def derivation_of_activation_function(signal):
	pass


def loss_function(true_labels, probabilities):
	pass


# the derivation should be with respect to the output neurons
def derivation_of_loss_function(true_labels, probabilities):
	pass


# softmax is used to turn activations into probability distribution
def softmax(layer):
	pass



def forward_pass(data):
	pass



#should change the strings into word vectors. Should not be effected by the backpropagation
def embedding_layer(samples):
	pass



# [hidden_layers] is not an argument, replace it with your desired hidden layers 
def backward_pass(input_layer, [hidden_layers] , output_layer, loss): 
	pass



def train(train_data, train_labels, valid_data, valid_labels):

	for epoch in range(number_of_epochs):
		index = 0

		#for each batch
		for data, labels in zip(train_data, train_labels):
			# Same thing about [hidden_layers] mentioned above is valid here also
			predictions, [hidden_layers] = forward_pass(data)
			loss_signals = derivation_of_loss_function(labels, predictions)
			backward_pass(data, [hidden_layers], predictions, loss_signals)
			loss = loss_function(labels, predictions)

			if index%20000 == 0: # at each 20000th sample, we run validation set to see our model's improvements
				accuracy, loss = test(valid_data, valid_labels)
				print("Epoch= "+str(epoch)+", Coverage= %"+ str(100*(index/len(train_data))) + ", Accuracy= "+ str(accuracy) + ", Loss= " + str(loss))

			index += 1

	return losses





def test(test_data, test_labels):

	avg_loss = 0
	predictions = []
	labels = []

	#for each batch
	for data, label in zip(test_data, test_labels):
		prediction, _, _ = forward_pass(data)
		predictions.append(prediction)
		labels.append(label)
		avg_loss += np.sum(loss_function(label, prediction))

	#turn predictions into one-hot encoded 
	one_hot_predictions = np.zeros(shape=(len(predictions), output_size))
	for i in range(len(predictions)):
		one_hot_predictions[i][np.argmax(predictions[i])] = 1

	predictions = one_hot_predictions
	accuracy_score = accuracy(labels, predictions)

	return accuracy_score,  avg_loss / len(test_data)




def accuracy(true_labels, predictions):
	true_pred = 0

	for i in range(len(predictions)):
		if np.argmax(predictions[i]) == np.argmax(true_labels[i]): # if 1 is in same index with ground truth
			true_pred += 1

	return true_pred / len(predictions)







 
if __name__ == "__main__":


	#PROCESS THE DATA
	words, labels = read_data(path)
	sentences = create_samples(words, labels)
	train_x, train_y, test_x, test_y = split_data(sentences)


	# creating one-hot vector notation of labels. (Labels are given numeric)
	# [0 1] is PERSON
	# [1 0] is not PERSON
	new_train_y = np.zeros(shape=(len(train_y), output_size))
	new_test_y = np.zeros(shape=(len(test_y), output_size))

	for i in range(len(train_y)):
		new_train_y[i][int(train_y[i])] = 1

	for i in range(len(test_y)):
		new_test_y[i][int(test_y[i])] = 1

	train_y = new_train_y
	test_y = new_test_y


	# Training and validation split. (%80-%20)
	valid_x = np.asarray(train_x[int(0.8*len(train_x)):-1])
	valid_y = np.asarray(train_y[int(0.8*len(train_y)):-1])
	train_x = np.asarray(train_x[0:int(0.8*len(train_x))])
	train_y = np.asarray(train_y[0:int(0.8*len(train_y))])

	train(train_x, train_y, valid_x, valid_y)
	print("Test Scores:")
	print(test(test_x, test_y))


