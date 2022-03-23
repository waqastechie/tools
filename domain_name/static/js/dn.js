$(document).ready(function () {
    $("#dn-form").submit(function (event) {
        event.preventDefault();  
        var domain_name = $("#domain_name").val();
        $.ajax({
            type: "GET",
            async: true,
            url: 'dn-checker-generator',
            dataType: 'json',

            data: {
                "domain_name": domain_name
            },

            success: function (response) {

                $("#domain_result").empty()
                $(".card-text").empty()
                $("#details").empty()

                $("#result").show()
                $("#suggetions").show()
                
                $("#domain_name_result").html(domain_name)
                
                
                if(response.domain_info_dict != false){
                    $("#domain_name_result").removeClass("bg-success")
                    $("#domain_name_result").addClass("bg-danger")
                    $("#domain_result").html("Domain is Already Registered! Try other one <button type='button' class='btn btn-info' data-bs-toggle='collapse'  data-bs-target='#details'>Show Info</button>")
                    
                    for(details in response.domain_info_dict){
                        
                        $("#details").append("<li class='list-group-item'><span class='label label-default text-uppercase font-weight-bold'>"+details+": "+"</span>"+response.domain_info_dict[details]+"</li>")
                    }
                    
                }
                else{
                    $("#domain_name_result").removeClass("bg-danger")
                    $("#domain_name_result").addClass("bg-success")
                    $("#domain_result").html("Domain is Available")
                }
                if(response.generated_domains_dict){
                      for (domain_type in response.generated_domains_dict) {
                        for (domain in response.generated_domains_dict[domain_type]){
                            $("#"+domain_type).append("<li class='list-group-item'>"+response.generated_domains_dict[domain_type][domain]+"</li>")
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


