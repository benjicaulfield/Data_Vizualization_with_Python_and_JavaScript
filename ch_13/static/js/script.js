var API_URL = 'http://localhost:5000/api';

var displayJSON = function(query) {

    d3.json(API_URL + query, function(error, data) {

        // log any error to the consale as a warning
        if(error) {
            console.warn(error);
        }

        d3.select('#query pre').html(query);
        d3.select('#data pre').html(JSON.stringify(data, null, 4));
        console.log(data);
    });
};

var query = '/winners?where=' + JSON.stringify({
        "name":"Albert Einstein"
    });

//var query = '/winners/' + albert_item._id;

displayJSON(query);