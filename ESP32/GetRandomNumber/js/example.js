function cal() {
    var a = 1 + Math.abs(Math.floor(Math.random() * 4));
    var b = 1 + Math.abs(Math.floor(Math.random() * 4));
    var opt = Math.random() > 0 ? '+' : '-';
    var c = opt == '+' ? (a + b) : (a - b);
    return [a, b, c];
}

function domath() {
    do {
        var [a, b, c] = cal();
    }
    while (c < 0 || c > 5);

    $("#a").text(a);
    $("#b").text(b);
    $("#c").text(c);


    return false;
};

$().ready(function() {
    // Process items to be repeated
    $('.item.repeat').each(function() {
        var $this = $(this);

        var text = $this.text();

        // Remove these comments if spaces are needed
        /*text += ' ';
        $this.html($this.text()+'&nbsp;');*/


        var numReps = 5;

        $this.html(text.repeat(numReps));
    });
});
