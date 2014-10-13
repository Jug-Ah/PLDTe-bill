//define functions and global variables here...
var siteloc = "http://localhost/PLDT";
var scriptloc = "/scripts/";


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
              if (isNaN(res)){
                alert(res)
              }
              else {
                alert("OK")
              }
            }
    });
}
