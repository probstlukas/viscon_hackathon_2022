function deleteEvent(eventId) {
    fetch("/delete-event", {
      method: "POST",
      body: JSON.stringify({ eventId: eventId }),
    }).then((_res) => {
      window.location.href = "/user-events";
    });
}

function addInterest(eventId, foodName) {
    let number = document.getElementById('x'+eventId+foodName).textContent
    let i = parseInt(number)+1
    document.getElementById('x'+eventId+foodName).textContent = i.toString()
    console.log('eventId: ' + eventId + '; foodName: '+foodName)
    fetch("/add-interest", {
      method: "POST",
      body: JSON.stringify({ eventId: eventId, foodName: foodName }),
    }).then((_res) => {
        void(0)
        return null
        //window.location.href = "/";
    });
}

function saveChanges(eventId, foodName) {
    let newQuantity = document.getElementById(eventId+foodName).value
    document.getElementById(eventId+foodName).value=''
    console.log('eventId: ' + eventId + '; foodName: '+foodName+'; newQuantity: '+newQuantity)
    if (newQuantity=='') {
        console.log('escaping')
        void(0)
        return null
    }
    document.getElementById(eventId+foodName).placeholder=newQuantity
    fetch("/update-event", {
      method: "POST",
      body: JSON.stringify({ eventId: eventId, foodName: foodName, newQuantity: parseInt(newQuantity) }),
    }).then((_res) => {
        void(0)
        return null//window.location.href = "/user-events";
    });
}