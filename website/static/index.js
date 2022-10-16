function deleteEvent(eventId) {
    fetch("/delete-event", {
      method: "POST",
      body: JSON.stringify({ eventId: eventId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}

function addInterest(eventId, foodName) {
    console.log('eventId: ' + eventId + '; foodName: '+foodName)
    fetch("/add-interest", {
      method: "POST",
      body: JSON.stringify({ eventId: eventId, foodName: foodName }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function saveChanges(eventId, foodName) {
    let newQuantity = document.getElementById(eventId+foodName).value
    console.log('eventId: ' + eventId + '; foodName: '+foodName+'; newQuantity: '+newQuantity)
    if (newQuantity=='') {
        console.log('escaping')
        return null
    }
    fetch("/update-event", {
      method: "POST",
      body: JSON.stringify({ eventId: eventId, foodName: foodName, newQuantity: parseInt(newQuantity) }),
    }).then((_res) => {
      window.location.href = "/user-events";
    });
}