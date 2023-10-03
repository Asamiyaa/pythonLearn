'''
machineLearn

Scikit-learn：** 用于机器学习和数据挖掘，提供各种算法和工具。
TensorFlow 和 PyTorch：** 用于深度学习和神经网络开发。

机器学习流程：https://zhuanlan.zhihu.com/p/25761248
'''


# 导入必要的库
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 加载示例数据集（这里使用鸢尾花数据集）
iris = datasets.load_iris()
X = iris.data
y = iris.target

# 数据集划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 特征标准化（很多机器学习模型都受益于特征标准化）
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 创建SVM分类器
svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)  # 这里使用线性核函数

# 在训练集上训练模型
svm_classifier.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = svm_classifier.predict(X_test)

# 计算准确性
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')
