/*function Counter(inc) {
    var count = 0;
    var add = function() {
        count += inc;
        console.log("Current count: " + count);
    };
    return add;
}

var inc2 = Counter(2);
inc2();
inc2();*/

function Counter(inc) {
    var count = 0;
    var api = {};
    api.add = function() {
        count += inc;
        console.log('Current count: ' + count);
    };
    api.sub = function() {
        count -= inc;
        console.log('Current count: ' + count);
    };
    api.reset = function() {
        count = 0;
        console.log('Current count: ' + count)
    };
    return api;
}

cntr = Counter(3);
cntr.add();
cntr.add();
cntr.add();
cntr.sub();
cntr.reset();