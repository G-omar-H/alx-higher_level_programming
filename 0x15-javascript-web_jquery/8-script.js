const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (data, textStatus) {
  $.each(data.results, function (i, obj) {
    $('UL#list_movies').append($('<li></li>').text(obj.title));
  });
});
