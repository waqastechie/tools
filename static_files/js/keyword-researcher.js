$(document).ready(function () {
    $("#kr_search_btn").click(function (event) {
        
        $("#keyword_div").show()
        var keyword = $("#keyword").val();

        // $.ajax({
        //     type: "GET",
        //     url: 'researcher',
        //     dataType: 'json',

        //     data: {
        //         "keyword": keyword
        //     },

        //     success: function (response) {
        //         console.log(response)
        //     },
        //     error: function (response) {
        //         console.log(response)
        //     }
        // })

        $.ajax({
            url: 'researcher?keyword=' + keyword,
            type: 'GET',
            retrieve: true,
            async: true,
            beforeSend: function () {
                $("#qoverlay").fadeIn(100);
            },
            complete: function () {
                
                    $("#qoverlay").fadeOut(100);
               
            },
            success: function (data) {

                var table = $('#keywords_table').DataTable({
                    destroy: true,
                    data: data,
                    columns: [
                        { "data": "suggestion" },

                        // { "targets": -1, "data": null, "defaultContent": "<button class= 'btn btn-success'>View Details</button>" }
                    ],
                    responsive: true,
                });
                // $('#yt_keywords_table').on('click', 'button', function (e) {
                //     e.preventDefault;
                //     var rows = table.row($(this).parents('tr')).data(); //Get Data Of The Selected Row
                //     console.log(rows)
                // });
            }
        });



    })

})


