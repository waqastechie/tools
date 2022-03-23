



$("#yt_kr_search_btn").click(function (event) {
    if ($("#keyword").val() != '') {

        var keyword = $("#keyword").val();
        // $.ajax({
        //     type: "GET",
        //     async: true,
        //     url: 'yt-q-explorer',
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
            url: 'yt-q-explorer?keyword=' + keyword,
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

                var table = $('#ytq_keywords_table').DataTable({
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

        /////////////////////////////////////////////
        // $.ajax({
        //     type: "GET",
        //     async: true,
        //     url: 'yt-p-explorer',
        //     dataType: 'json',

        //     data: {
        //         "keyword": keyword
        //     },

        //     success: function (response) {
        //         console.log(response)
        //         var dataSet = response
        //     },
        //     error: function (response) {
        //         console.log(response)
        //     }
        // })
        $.ajax({
            url: 'yt-p-explorer?keyword=' + keyword,
            type: 'GET',
            async: true,
            beforeSend: function () {
                $("#poverlay").fadeIn(100);
            },
            complete: function () {
                
                    $("#poverlay").fadeOut(100);
               
            },

            success: function (data) {
                var table = $('#ytp_keywords_table').DataTable({
                    'processing': true,

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
        ////////////////////////////////////////////////
        // $.ajax({
        //     type: "GET",
        //     async: true,
        //     url: 'yt-c-explorer',
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
            url: 'yt-c-explorer?keyword=' + keyword,
            type: 'GET',

            async: true,
            beforeSend: function () {
                $("#coverlay").fadeIn(100);
            },
            complete: function () {
                
                    $("#coverlay").fadeOut(100);
               
            },
            success: function (data) {
                var table = $('#ytc_keywords_table').DataTable({
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
        ////////////////////////////////////////////////
        // $.ajax({
        //     type: "GET",
        //     async: true,
        //     url: 'yt-alpha-explorer',
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
            url: 'yt-alpha-explorer?keyword=' + keyword,
            type: 'GET',

            async: true,
            beforeSend: function () {
                $("#alphaoverlay").fadeIn(100);
            },
            complete: function () {
                
                    $("#alphaoverlay").fadeOut(100);
               
            },
            success: function (data) {
                var table = $('#ytalpha_keywords_table').DataTable({
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


    }
    else {
        alert("Enter a Keyword")
    }


})













