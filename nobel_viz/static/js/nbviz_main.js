/* global $, _, crossfilter, d3 */

(function(nbviz) {
    'use strict';

    var query_winners = 'winners?projection' +
            JSON.stringify( {"mini_bio":0, "bio_image":0} );

    queue()
        .defer(d3.json, "/static/data/world-110m.json")
        .defer(d3.csv, "/static/data/world-country-names-nobel.csv")
        .defer(d3.json, "/static/data/winning_country_data.json")
        .defer(nbviz.getDataFromAPI, query_winners)
        .await(ready);

    function ready(error, worldMap, countryNames, countryData, winnersDAta) {
        //LOG ANY ERROR TO CONSOLE
        if(error) {
            return console.warn(error);
        }
        //STORE OUR COUNTRY-DATA DATASET
        nbviz.data.countryData = countryData;
        // MAKE OUR FILTER AND ITS DIMENSIONS
        nbviz.makeFilterAndDimensions(winnersData);
        // INITIALIZE MENU AND MAP
        nbviz.initMenu();
        nbviz.initMap(worldMap, countryData);
        // TRIGGER UPDATE WITH FULL WINNERS' DATASET
        nbviz.onDataChange();
    }

}(window.nbviz = window.nbviz || {}));