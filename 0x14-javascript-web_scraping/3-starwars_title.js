#!/usr/bin/node
/**
 * script to print the title of a start war movie
 * where episode number match given integer as argument
 */

async function get () {
  const id = Number(process.argv[2]);
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  const req = new Request(url);
  const res = await fetch(req);
  const sw = await res.json();

  console.log(sw.title);
}
get();
