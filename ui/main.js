function getData(){
    var data = document.getElementById("stock_name").value
    eel.get_data(data)(display_result)
}

function display_result(result){
    console.log(result)
    document.getElementById("output").innerHTML = result
}