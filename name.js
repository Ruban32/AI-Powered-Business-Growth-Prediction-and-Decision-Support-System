function predictSales(){

    let expenses = parseInt(document.getElementById("expenses").value);
    let customers = parseInt(document.getElementById("customers").value);

    if(isNaN(expenses) || isNaN(customers)){
        alert("Please enter all values");
        return;
    }

    let predictedSales = expenses + (customers * 350);

    let healthScore = Math.min(
        100,
        Math.max(50, Math.round((customers / 3) - (expenses / 5000) + 80))
    );

    let recommendation;

    if(healthScore >= 85){
        recommendation = "Business growth is excellent. Consider expansion.";
    }
    else if(healthScore >= 70){
        recommendation = "Business performance is stable. Focus on marketing.";
    }
    else{
        recommendation = "Reduce expenses and improve customer acquisition.";
    }

    document.getElementById("result").style.display = "block";

    document.getElementById("sales").innerHTML =
        "Predicted Sales: ₹" + predictedSales;

    document.getElementById("health").innerHTML =
        "Health Score: " + healthScore + "%";

    document.getElementById("recommendation").innerHTML =
        recommendation;
}
