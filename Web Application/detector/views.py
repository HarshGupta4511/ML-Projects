import pickle

from django.shortcuts import render

from preprocessing import transform_text


# Load ML model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


# Load vectorizer
with open("vectorize.pkl", "rb") as file:
    vectorizer = pickle.load(file)


def home(request):

    result = None

    if request.method == "POST":

        # Get message entered by the user
        message = request.POST.get("message", "")

        if message.strip():

            # Step 1: Preprocess the message
            transformed_message = transform_text(message)

            # Step 2: Convert text into numerical features
            message_vector = vectorizer.transform(
                [transformed_message]
            )

            # Step 3: Convert sparse matrix to dense
            message_vector = message_vector.toarray()

            # Step 4: Prediction
            prediction = model.predict(message_vector)[0]
            print("Message:", message)
            print("Processed:", transformed_message)
            print("Prediction:", prediction)
            print("Model classes:", model.classes_)

            # Step 5: Convert prediction into readable result
            if prediction == 1:
                result = "SPAM"
            else:
                result = "NOT SPAM"

    return render(
        request,
        "detector/index.html",
        {
            "result": result
        }
    )