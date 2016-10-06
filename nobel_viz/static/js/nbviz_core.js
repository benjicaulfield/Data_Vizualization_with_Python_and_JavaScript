/* global $, _, crossfilter, d3 */
(function(nbviz) {
    'use strict';

    nbviz.data = {}; // our main data object
    nbviz.valuePerCapita = 0; // metric flag
    nbviz.activeCountry = null;
    nbviz.ALL_CATS = 'All Categories';
    nbviz.TRANS_DURATION = 2000; // length in ms for our transitions
    nbviz.MAX_CENTROID_RADIUS = 30;
    nbviz.MIN_CENTROID_RADIUS = 2;
    nbviz.COLORS = { palegold: '#E6BE8A'}; // any named colors we use
    nbviz.CATEGORIES = [
        "Chemistry", "Economics", "Literature", "Peace",
        "Physics", "Physiology or Medicine"
    ];

    nbviz.categoryFill = function(category) {
        var i = nbviz.CATEGORIES.indexOf(category);
        return d3.hcl(i / nbviz.CATEGORIES.length * 360, 60, 70);
    };


    // $EVE_API (by default 'http://localhost:5000/api/' is set in
    // index.html (STATIC FILES) and templates/index.thml (MONGODB EVE API)
    nbviz.getDataFromAPI = function(resource, callback) {
        d3.json($EVE_API + resource, function(error, data) {
            if (error) {
                return callback(error);
            }
            if ('_items' in data) {
                callback(null, data._items);
            }
            else {
                callback(null, data);
            }
        });
    };

    var nestDataByYear = function(entries) {
        // ...
    };

    nbviz.makeFilterAndDimensions = function(winnersData) {
        // ...
    };

    nbviz.filterByCountries = function(countryNames) {
        // ...
    };

    nbviz.filterByCategories = function(cat) {
        // ...
    };

    nbviz.getCountryData = function() {
        // ...
    };

    nbviz.onDataChange = function() {
        var data = nbviz.getCountryData();
        nbviz.updateBarChart(data);
        nbviz.updateMap(data);
        nbviz.updateList(nbviz.countryDim.top(Infinity));
        data = nestDataByYear(nbviz.countryDim.top(Infinity));
        nbviz.updateTimeChart(data);
    };

}(window.nbviz = window.nbivz || {}));