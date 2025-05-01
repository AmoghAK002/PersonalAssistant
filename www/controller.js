$(document).ready(function () {

    eel.expose(DisplayMessage);
    function DisplayMessage(message) {
        // Display the message in the Siri message area
        $('.siri-message').text(message);
        $('.siri-message').textillate('start'); // Start the animation
    }

    //Display Hood
    eel.expose(ShowHood);
    function ShowHood() {
        $("#Oval").attr("hidden", false);
        $("#SiriWave").attr("hidden", true);
       
    }
});