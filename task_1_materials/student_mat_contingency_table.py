import matplotlib.pyplot as plt
import pandas as pd


colnames=['school','sex','age', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences','G1','G2','G3']
d = pd.read_csv('/Users/ben-malik/Downloads/task_1_materials/student/student-mat.csv',names=colnames,sep=';')

# initialization of parameters
discriminator_feature = 'G3'
target_class = "studytime"
threshold = 10.0

prediction = []
values = d.values

# prediction
for i in range(1,len(values)):
	if float(values[i][colnames.index(discriminator_feature)]) >= threshold: # colnames.index(discriminator_feature) gives index of feature
		prediction.append([target_class,values[i][31]])
	else:
		prediction.append(["other",values[i][31]])

print(prediction)

# tp = 0
# fp = 0
# tn = 0
# fn = 0

# # Calculating value of contingency table cells
# for i in range(len(prediction)):
# 	if prediction[i][0] == 'other' and (prediction[i][1] != target_class):
# 		tn += 1
# 	elif prediction[i][0] == 'other' and (prediction[i][1] == target_class):
# 		fn += 1
# 	elif prediction[i][0] == target_class and (prediction[i][1] == target_class):
# 		tp += 1
# 	elif prediction[i][0] == target_class and (prediction[i][1] != target_class):
# 		fp += 1
# print('Handling contingencies')

# # Cool printing
# print(str("\n   ")+str(1)+  "  |"  +str("  ")+str(  0))
# print(str(1)+ "| " +str(tp) +str("   ")+  str(fn))
# print(str(0)+ "| " +str(fp) + str("   ")+  str(tn))

# jaccard_coefficient = tp/(fp+tp+fn)

# print("\nJaccard Coefficient: ",jaccard_coefficient)


# # An easier way to do the things above
# table = pd.crosstab(d[discriminator_feature]<threshold, d['Species']==target_class, margins=True)
# print("\n",table)

# jaccard_coefficient = table.values[1][1]/(table.values[0][1]+table.values[1][1]+table.values[1][0])
# print("\nJaccard Coefficient: ",jaccard_coefficient)