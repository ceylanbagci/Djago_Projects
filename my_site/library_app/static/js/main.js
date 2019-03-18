// // Get the modal
// var modal = document.getElementById('myModal');
//
// // Get the button that opens the modal
// var btn = document.getElementById("myBtn");
//
// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];
//
// // When the user clicks the button, open the modal
// btn.onclick = function() {
//   modal.style.display = "block";
// }
//
// // When the user clicks on <span> (x), close the modal
// span.onclick = function() {
//   modal.style.display = "none";
// }
//
// // When the user clicks anywhere outside of the modal, close it
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }

// $(document).on("click", ".btn-book-update", function (e) {
//     e.stopImmediatePropagation();
//       openCustomerDetailsModal($(this).data("company_id"));
//   });

$(".btn-book-update").on("click", function(self){
  alert("The paragraph was clicked.");
  $.ajax({
    type: "GET",
    url: "/show_customer/",
  })
});




  // $(".btn-book-assignment").click( function () {
  //     // openCustomerAssignmentModal($(this).data("person_id"));
  //     console.log("buttonnnnn");
  //     alert("Hello! I am an alert box!");
  //
  //
  //   });
//}

// function openCustomerAssignmentModal(customer_id){
//   $.ajax({
//     type: "GET",
//     url: "/get_customer_assigment/",
//     data: {
//       customer_id: customer_id
//     },
//     success: function (returnValue) {
//       showModal(returnValue["partial"],"Uzman Görevlendirme", "common_modal_large");
//     }
//   }).done(function( data ) {
//     initMask();
//     regiCompanyInit();
//     initIcheckComponent();
//     dateTimeInit();
//   });
// }


// ++++++++++++++Customer Info++++++++++++++++

// var modal2 = document.getElementById('costomer_modal');
// var link = document.getElementById("get_customer_info");
// var span2 = document.getElementsByClassName("close_window")[0];
//
// link.onclick = function() {
//   modal2.style.display = "block";
// }
// span2.onclick = function() {
//   modal2.style.display = "none";
// }
// window.onclick = function(event) {
//   if (event.target == modal2) {
//     modal2.style.display = "none";
//   }
// }
