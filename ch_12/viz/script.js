/*d3.json('data/nobel_winners.json', function(error, data) {
    if (error) {
        console.error(error);
    }

    d3.select('h2#data-title').text('All the Nobel-winners');
    d3.select('div#data pre')
        .html(JSON.stringify(data, null, 4));
});*/

var loadCountryWinnersJSON = function(country) {
    d3.json('data/winners_by_country' + country + '.json',
        function(error, data) {
            if(error) {
                console.error(error);
            }

            d3.select('h2#data-title')
                .text('All the Nobel-winners from ' + country);
            d3.select('div#data pre')
                .html(JSON.stringify(data, null, 4));
        });
};

loadCountryWinnersJSON('Australia');