function listenClickModel(idModal, idImg, idModalImg, src) {

    let modal = document.getElementById(idModal);
    let img = document.getElementById(idImg);
    let modalImg = document.getElementById(idModalImg);
    modal.style.display = "block";
    modalImg.src = src;
}

function closeModel(idModel) {
    let model = document.getElementById(idModel);
    model.style.display = "none";
}
$(document).ready(function() {
    var c = document.getElementsByClassName("dt_bill");
    if (c.length <= 1) {
        $("body").css({
            "width": "100%",
            "height": "100%",
            "background-attachment": "fixed"
        });
    } else {
        $("body").css({});
    }
});