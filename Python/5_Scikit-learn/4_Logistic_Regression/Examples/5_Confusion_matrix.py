import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

y_test = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
y_pred = np.array([0, 1, 0, 0, 0, 0, 0, 1, 1, 1])

confusion_matrix = confusion_matrix(y_test, y_pred)

print 'confusion matrix:\n', confusion_matrix

table = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predictions'])
print 'crosstab:\n', table

Cmap = plt.get_cmap('Blues', 4) # hot, jet, Blues, 4 discrete values

plt.matshow(confusion_matrix, cmap = Cmap) #to plot matrix value in color map
#plt.matshow(table, cmap = Cmap) #to plot matrix value in color map
plt.title('Confusion matrix')
plt.colorbar().set_ticks([1,2,3,4])
plt.ylabel('True label')
plt.xlabel('Predicted label')

plt.savefig('Confusion_matrix.png')
plt.show()

#The confusion matrix indicates that there were four true negative predictions, three
#true positive predictions, two false negative predictions, and one false positive
#prediction.