const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(url, function (data, textStatus) {
  $('div#character').text(data.name);
});
