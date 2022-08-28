
// getting csrf token function
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }


// table search
function myfun(){
    var input, filter, table, tr, td, i, txtValue, norec;
    input = document.getElementById("txt_name");
    norec = document.getElementById("notfound");
    filter = input.value.toUpperCase();
    table = document.getElementById("member_table");
    tr = table.getElementsByTagName("tr");
    for (i = 0; i < tr.length; i++) {
         td = tr[i].getElementsByTagName("td")[0];
        if (td) {
            txtValue = td.textContent || td.innerText;
            if (txtValue.toUpperCase().indexOf(filter) > -1) {
                tr[i].style.display = "";
            } 
            else {
                tr[i].style.display = "none";
            }
        }    
    }
}




// To CSV

function export2csv() {
  let data = "";
  const tableData = [];
  const rows = document.querySelectorAll("table tr");
  for (const row of rows) {
    const rowData = [];
    for (const [index, column] of row.querySelectorAll("th:not(:nth-child(9)), td:not(:nth-child(9))").entries()) {
      // To retain the commas in the "Description" column, we can enclose those fields in quotation marks.
      if ((index + 1) % 3 === 0) {
        rowData.push('"' + column.innerText + '"');
      } else {
        rowData.push(column.innerText);
      }
    }
    tableData.push(rowData.join(","));
  }
  data += tableData.join("\n");
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([data], { type: "text/csv" }));
  a.setAttribute("download", "LuzYouthMemberDetails.csv");
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}


// To Print
function printit() {
    var divToPrint=document.getElementById("member_table");
    newWin= window.open("");
    newWin.document.write("<style> td:nth-child(9){display:none;} </style>");
    newWin.document.write("<style> th:nth-child(9){display:none;} </style>");
    newWin.document.write(divToPrint.outerHTML);
    newWin.print();
    newWin.close();
}


$(document).ready(function() {

  /* ADD CHURCH MOTO */
  $("#church-moto-submit").click(function() {
    var church_moto = $("#church-moto").val();
    var church_moto_json = {"church_moto":church_moto}
    add_church_moto(church_moto_json);
  });


  /* ADD OFFICE HISTORY  */
  $("#office-history-submit").click(function() {
    var office_history_json = {
      "short_history": $(".short-history").val(),
      "church_office": $("#church-office-no").val(),
      "church_mobile": $("#church-mobile-no").val(),
    }
    add_office_history_moto(office_history_json);
  });


});
