$(function(){
    $("#article_rewriter_submit_btn").click(function (event) {
        if ($("#long_text").val() != '') {
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            var long_text = $("#long_text").val();
            $.ajax({
                type: "POST",
                async: true,
                url: 'rewriter',
                headers: {'X-CSRFToken': csrftoken},
                dataType: 'json',

                data: {
                    "long_text": long_text
                },

                success: function (response) {
                    $("#rewriter-output").show()
                    $("#rewriter-output").html(response)
                },
                error: function (response) {
                    console.log(response)
                }
            })
        
            


        }
        else {
            alert("Enter Text")
        }


    })


})












