import pickle

from preprocessing import transform_text


# -----------------------------
# Load model
# -----------------------------

with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# -----------------------------
# Load vectorizer
# -----------------------------

with open("vectorize.pkl", "rb") as file:
    vectorizer = pickle.load(file)


print("Model loaded successfully!")
print("Vectorizer loaded successfully!")


# -----------------------------
# Test message
# -----------------------------

message = "Congratulations! You have won a free prize!"


# Preprocess
transformed_message = transform_text(message)

print("Original message:")
print(message)

print("\nTransformed message:")
print(transformed_message)


# Vectorize
message_vector = vectorizer.transform([transformed_message])


# Convert sparse → dense
message_vector = message_vector.toarray()


# Prediction
prediction = model.predict(message_vector)


print("\nPrediction:")
print(prediction)