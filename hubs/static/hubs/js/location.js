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

var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
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
            document.getElementById('locationDisplay').innerHTML = position.coords.latitude + "," + position.coords.longitude
            $.ajax({
                    type: "POST",
                    url: "locations",
                    data: position,
                    success: function(data) {
                        console.log("AJAX request sent successfully : " + data)
                        console.log("CSRF token : " + csrftoken)
                    }
            });
        });
    }
} else {
    console.log("Geo-location not supported by browser");
}