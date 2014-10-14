//define functions and global variables here...
var siteloc = "http://localhost/PLDT";
var scriptloc = "/scripts/";

$(document).ready(function () {
	
	document.getElementById("#pldt-acc-display").innertext = "Paragraph changed!";
	//$("#pldt-acc-display").attr("innerhtml","asds");
	$('#form-input').validate({
        rules: {
            PLDTaccountnumber: {                
                required: true                
            },
			BANKaccountnumber: {
				required: true,
				
			},			
        },
      
        highlight: function (element) {
            $(element).closest('.controls').addClass('has-error');
        },
        success: function (element) {
            $(element).closest('.controls').removeClass('has-error');
        }
    });
});
  

function getBill()
{  	
	$.ajax({
      url: siteloc + scriptloc + "getbill.py",
      data: {pldtNum:$("#PLDTaccountnumber").val()},
      dataType: 'json',
	  async: true,
      success: function (res) {
      			
      			accountnumdisplay = ' <h3 id="pldt-acc-display" class="panel-title">PLDT Account Number: ';
				accountnumdisplay += res[0][0];
				accountnumdisplay += '</h3>';	
				$("#pldtnum").html(accountnumdisplay);		
				$("#current-bill").html("Bill: " + res[0][1]);
				
				
            }
    });
	$("#bill-page").attr("class","tab-pane fade in active");
	$("#inputpage").attr("class","tab-pane fade");	
}

function paybill()
{
	$.ajax({
      url: siteloc + scriptloc + "paybill.py",
      data: {accountno:$("#BANKaccountnumber").val(),pldtacct:$("#PLDTaccountnumber").val(),amount:$("#amount-input").val()},
      dataType: 'json',
	  async: true,
      success: function (res) {					
				$("#pldt-acc-display").val("hey");
				
            }
    });
}