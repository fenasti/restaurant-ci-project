const editButtons = document.getElementsByClassName("btn-edit");
const reservationText = document.getElementById("id_details"); 
const reservationForm = document.getElementById("reservationForm");
const submitButton = document.getElementById("submitButton");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated reservation's ID upon click.
* - Fetches the content of the corresponding reservation.
* - Populates the `reservationText` input/textarea with the reservation's details for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_reservation/{reservationId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reservationId = e.target.getAttribute("reservation_id");
    let reservationContent = document.getElementById(`reservation${reservationId}`).innerText;
    reservationText.value = reservationContent;
    submitButton.innerText = "Update";
    reservationForm.setAttribute("action", `edit_reservation/${reservationId}`);
    console.log("Reservation ID:", reservationId);
    console.log("Reservation Content:", reservationContent);
  });
}