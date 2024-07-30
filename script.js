document.addEventListener('DOMContentLoaded', function () {
    var inputs = [
        { range: 'latitude_range', text: 'latitude_text' },
        { range: 'longitude_range', text: 'longitude_text' },
        { range: 'depth_range', text: 'depth_text' },
        { range: 'horizontalError_range', text: 'horizontalError_text' },
        { range: 'depthError_range', text: 'depthError_text' },
        { range: 'magError_range', text: 'magError_text' }
    ];

    inputs.forEach(function(input) {
        var rangeElement = document.getElementById(input.range);
        var textElement = document.getElementById(input.text);

        rangeElement.addEventListener('input', function () {
            textElement.value = rangeElement.value;
        });

        textElement.addEventListener('input', function () {
            rangeElement.value = textElement.value;
        });
    });
});
