$(document).ready(function () {
    $("#cwv_search_btn").click(function (event) {

        var url = $("#url").val();
        var category=$("#category option:selected").val();
        var device=$("#device option:selected").val();
        
        $.ajax({
            type: "GET",
            async: true,
            url: 'cwv-engine',
            dataType: 'json',

            data: {
                "url": url,
                "category":category,
                "device":device

            },

            success: function (response) {
                console.log(response)
            },
            error: function (response) {
                console.log(response)
            }
        })        
        




    })





})


