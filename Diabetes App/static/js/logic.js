$(document).ready(function() {
    console.log("Page Loaded");

    $("#filter").click(function() {
        // alert("button clicked!");
        makePredictions();
    });
});


// call Flask API endpoint
function makePredictions() {
    let Pregnancies = $("#Pregnancies").val();
    let Glucose = $("#Glucose").val();
    let BloodPressure = $("#BloodPressure").val();
    let SkinThickness = $("#SkinThickness").val();
    let Insulin = $("#Insulin").val();
    let BMI = $("#BMI").val();
    let DiabetesPedigreeFunction = $("#DiabetesPedigreeFunction").val();
    let Age = $("#Age").val();

    // check if inputs are valid

    // create the payload
    let payload = {
        "Pregnancies": Pregnancies,
        "Glucose": Glucose,
        "BloodPressure": BloodPressure,
        "SkinThickness": SkinThickness,
        "Insulin": Insulin,
        "BMI": BMI,
        "DiabetesPedigreeFunction": DiabetesPedigreeFunction,
        "Age": Age
    }

    // Perform a POST request to the query URL
    $.ajax({
        type: "POST",
        url: "/makePredictions",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // Log the returned data for debugging
            console.log(returnedData);

            // Parse the prediction probability from the returned data
            let prob = parseFloat(returnedData["prediction"]).toFixed(2); // Format to 2 decimal places

            // Display the result based on the probability
            if (prob > 0.5) {
                $("#output").text(`The model predicts a high risk of diabetes with a probability of ${prob}.`);
            } else {
                $("#output").text(`The model predicts a low risk of diabetes with a probability of ${prob}.`);
            }
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            // Display error messages in a user-friendly way
            $("#output").text(`An error occurred: ${textStatus}. Please try again later.`);
            console.error("Error details:", errorThrown);
        }
    });

}
