const request = require('request');

// Function to fetch and print characters for a given movie ID
function getMovieCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, (error, response, body) => {
        if (!error && response.statusCode === 200) {
            const movieData = JSON.parse(body);
            const characters = movieData.characters;

            // Fetch and print character names
            characters.forEach((characterUrl) => {
                request(characterUrl, (charError, charResponse, charBody) => {
                    if (!charError && charResponse.statusCode === 200) {
                        const characterData = JSON.parse(charBody);
                        console.log(characterData.name);
                    } else {
                        console.error(`Failed to fetch character data for URL: ${characterUrl}`);
                    }
                });
            });
        } else {
            console.error(`Failed to fetch movie data for Movie ID: ${movieId}`);
        }
    });
}

// Check if a Movie ID is provided as a command-line argument
const args = process.argv.slice(2);
if (args.length === 1) {
    const movieId = args[0];
    getMovieCharacters(movieId);
} else {
    console.error('Usage: node 0-starwars_characters.js <Movie_ID>');
}
