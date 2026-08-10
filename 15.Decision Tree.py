from sklearn.tree import DecisionTreeClassifier

X = [[20], [25], [30], [35], [40]]
Y = [0, 0, 1, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, Y)

age = int(input("Enter Age: "))

result = model.predict([[age]])

print("Prediction:", result[0])
