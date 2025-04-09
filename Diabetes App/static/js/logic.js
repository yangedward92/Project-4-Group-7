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
        url: "/diabetes_predML",
        contentType: 'application/json;charset=UTF-8',
        data: JSON.stringify({ "data": payload }),
        success: function(returnedData) {
            // print it
            console.log(returnedData);
            let prob = parseFloat(returnedData["prediction"]);

            if (prob > 0.5) {
                $("#output").text(`You Survived with probability ${prob}!`);
            } else {
                $("#output").text(`You did not survive with probability ${prob}, sorry. :(`);
            }

        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert("Status: " + textStatus);
            alert("Error: " + errorThrown);
        }
    });

}
