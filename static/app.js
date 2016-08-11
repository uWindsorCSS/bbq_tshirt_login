function autoComplete(query, cb) {
  $.get("/autocomplete/" + query, cb);
}

function loginResponseHandler(data) {
  var feedback = $("#feedback");
  feedback.removeClass("alert alert-success alert-danger");
  feedback.text(data.message);

  if (data.success) {
    feedback.addClass("alert alert-success");
  } else {
    feedback.addClass("alert alert-danger");
  }
}

$(document).ready(function() {
  $("#full-name").typeahead({
    source: autoComplete
  });

  $("#login").on("click", function() {
    $.get("/checkin/" + $("#full-name").val() + "/" + $("#shirt-size").val(),
        loginResponseHandler);
  });
});
