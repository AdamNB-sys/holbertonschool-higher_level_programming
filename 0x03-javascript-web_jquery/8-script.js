$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const films = data.results;
  for (const title in films) {
    $('UL#list_movies').append('<li>' + films[title].title + '</li>');
  }
});
