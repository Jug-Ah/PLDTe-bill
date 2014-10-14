//define functions and global variables here...
var siteloc = "http://localhost/PLDTe-bill";
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
				$("#current-bill").html("Latest Bill: P" + res[0][1]);
				
				
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
                accountnumdisplay = ' <h3 id="pldt-acc-display" class="panel-title">PLDT Account Number: ';
                accountnumdisplay += res[0][0];
                accountnumdisplay += '</h3>'; 
                $("#pldtnum").html(accountnumdisplay);    
                $("#current-bill").html("Latest Bill: P" + res[0][1]);
              }
            }
    });
  makereceipt();
}

function makereceipt()
{
  $.ajax({
      url: siteloc + scriptloc + "addreceipt.py",
      data: {receipt_no:sessionStorage.receipt},
      dataType: 'json',
      async: true,
      success: function (res) {
          console.log("Receipt created");
              }
    });
}

function printreceipt()
{
  $.ajax({ 
      url: siteloc + scriptloc + "addreceipt.py",
      data: {receipt_no:sessionStorage.receipt},
    dataType: 'json',
      async: true,
      success: function (res) {
          var receiptNo = res[0][0];
                  var timedate = res[0][1];
          var amount = res[0][2];


                  $("#receiptNo").html(receiptNo);
                  $("#timedate").html(timedate);
          $("#amount").html(amount);
              }
    });
}