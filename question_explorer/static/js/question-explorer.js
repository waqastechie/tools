$(function(){
    $("#qe_search_btn").click(function (event) {
        $("section").show()   
        $(".card-text").empty()
        // $(".card-div").hide()
        var keywords = $("#keywords").val();
        var country=$("#qs-country option:selected").val();
        var lang=$("#qs-lang option:selected").val();
        $.ajax({
            type: "GET",
            async: true,
            url: 'q-explorer',
            dataType: 'json',

            data: {
                "keywords": keywords,
                "country":country,
                "lang":lang
            },

            success: function (response) {

                for (res in response) {
                    if ($("#" + res).length) {
                        
                        //$("#" + res+"_card_div").show()                      
                        
                        // $("#" + res).append("<h5 class='card-title' id='" + res + "_title'>" + res +  "</h5>")

                        for (ques in response[res]) {
                            
                            $("#" + res).append("<p class='card-text'>" + response[res][ques]+"</p> ")

                           
                        }

                    }

                }

            },
            error: function (response) {
                console.log(response)
            }
        })

        /////////////////////////////////////////////
        $.ajax({
            type: "GET",
            async: true,
            url: 'p-explorer',
            dataType: 'json',

            data: {
                "keywords": keywords,
                "country":country,
                "lang":lang
            },

            success: function (response) {
                

                for (res in response) {
                    if ($("#" + res+"_p").length) {

                        

                        //$("#" + res+"_p").append("<h5 class='card-title' id='" + res + "_title'>" + res + "</h5>")

                        for (ques in response[res]) {

                            $("#" + res+"_p").append("<p class='card-text'>" + response[res][ques] + "</p> ")


                        }

                    }

                }
            },
            error: function (response) {
                console.log(response)
            }
        })
        ////////////////////////////////////////////////
        $.ajax({
            type: "GET",
            async: true,
            url: 'c-explorer',
            dataType: 'json',

            data: {
                "keywords": keywords,
                "country":country,
                "lang":lang
            },

            success: function (response) {
                
                for (res in response) {
                    if ($("#c_" + res).length) {

                        //$("#" + res + "_card_div").show()

                        // $("#" + res).append("<h5 class='card-title' id='" + res + "_title'>" + res + "</h5>")

                        for (ques in response[res]) {
                           
                            $("#c_" + res).append("<p class='card-text'>" + response[res][ques] + "</p> ")


                        }

                    }

                }
            },
            error: function (response) {
                console.log(response)
            }
        })
        ////////////////////////////////////////////////
        $.ajax({
            type: "GET",
            async: true,
            url: 'alpha-explorer',
            dataType: 'json',

            data: {
                "keywords": keywords,
                "country":country,
                "lang":lang
            },

            success: function (response) {
               for (res in response) {
                    if ($("#" + res).length) {

                        //$("#" + res + "_card_div").show()

                        // $("#" + res).append("<h5 class='card-title' id='" + res + "_title'>" + res + "</h5>")

                        for (ques in response[res]) {

                            $("#" + res).append("<p class='card-text'>" + response[res][ques] + "</p> ")


                        }

                    }

                }
            },
            error: function (response) {
                console.log(response)
            }
        })




    })





})


