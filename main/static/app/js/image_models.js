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