function SignOnClick() {
    var text = document.getElementById("OriginalText").value;
    var event = new CustomEvent('SignRequest', { 'detail': text });
    document.dispatchEvent(event);
}

document.addEventListener('SignResponse',
function (e) {
    document.getElementById("Signature").value = e.detail;
}, false);
