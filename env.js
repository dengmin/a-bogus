window = global;
delete global;
delete Buffer;

window.requestAnimationFrame= function () {}

XMLHttpRequest = function(){}
navigator = {}

screen = {
    availHeight: 1125,
    availWidth: 1759,
    availLeft: 41,
    availTop: 44,
    colorDepth: 30,
    height: 1169,
}

document = {}
