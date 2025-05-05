$(document).ready(function () {

    // Siri text animation
    $('.text').textillate({
        loop: true,
        sync: true,
        in: { effect: 'bounceIn' },
        out: { effect: 'bounceOut' }
    });

    // Siri wave
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: 0.30,
        autostart: true
    });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: { effect: 'fadeInUp', sync: true },
        out: { effect: 'fadeOutUp', sync: true }
    });

    // Mic button click
    $("#MicBtn").click(function () {
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.playAssistantSound();
        eel.allCommands(); // Corrected this line
    });

    document.addEventListener("keyup", (e) => {
        if (e.key.toLowerCase() === 'j' && e.metaKey) {
            try {
                eel.playAssistantSound();
                $("#Oval").attr("hidden", true);
                $("#SiriWave").attr("hidden", false);
                eel.allCommands()(); // Assuming this returns a function
            } catch (error) {
                console.error("Eel function call failed:", error);
            }
        }
    });
    
});
