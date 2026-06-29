from model import predict_diabetes

# sample input
sample = [2, 150, 70, 30, 100, 35.5, 0.5, 40]

result, probability = predict_diabetes(sample)

print("Prediction:", result)
print("Risk %:", probability)
