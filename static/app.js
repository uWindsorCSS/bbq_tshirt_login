function autoComplete(query, cb) {
  $.get("/autocomplete/" + query, cb);
}

$(document).ready(function() {
  $("#full-name").typeahead({
    source: autoComplete
  });
});
