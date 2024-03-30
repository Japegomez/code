var namespace = '/mylab';
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

function clean() {
    $("#panel").hide();
    // No more time
    $("#timer").text(TIME_IS_OVER);
    running = false;
    currentTime = 0;
    clearInterval(TIMER_INTERVAL);
}

function updateTime() {
    currentTime = currentTime - 1;
    if (currentTime > 0) {
        // Still time
        if (currentTime > 1)
            $("#timer").text(SECONDS_PLURAL.replace("NUM", currentTime));
        else
            $("#timer").text(SECONDS_SING);
    } else {
        clean();
    }
}

updateTime();

function turnOn(number) {
    turnLight(number, true);
    return false;
}

function turnOff(number) {
    turnLight(number, false);
    return false;
}

function turnLight(number, state) {
    socket.emit('lights', { number: number, state: state })
}

function sendProgram() {
    socket.emit('program')
}

socket.on('update-client', function (data) {
    parseStatus(data);
});

socket.on('on-task', function (data) {
    console.log(data);
});

function logout() {
    $.post(LOGOUT_URL, {
        csrf: CSRF
    }).done(function () {
        clean();
    });
}

var HIDE_MESSAGES_BOX = null;

function parseStatus(newStatus) {
    for (var i = 1; i < 3; i++) {
        if (newStatus["lights"]["light-" + i]) {
            $("#light_" + i + "_on").show();
            $("#light_" + i + "_off").hide();
        } else {
            $("#light_" + i + "_off").show();
            $("#light_" + i + "_on").hide();
        }
    }
    $("#microcontroller_status").text(newStatus["microcontroller"]);
}

var TIMER_INTERVAL = setInterval(updateTime, 1000);