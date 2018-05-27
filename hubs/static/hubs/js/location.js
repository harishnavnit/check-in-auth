function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != ' ') {
        var cookies = document.cookie.split(';')
        for (var index = 0; index < cookies.length; index++) {
            var cookie = jQuery.trim(cookies[index])
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

if (navigator.geolocation) {
    window.onload = function() {
        navigator.geolocation.getCurrentPosition(function(position) {
            positionStr = position.coords.latitude + "," + position.coords.longitude
            document.getElementById('locationDisplay').innerHTML = positionStr

            // Send a request with the current location to the server
            $.ajax({ type: "POST", url: "locations", data: position });
        });
    }
} else {
    console.log("Geo-location not supported by browser");
}
