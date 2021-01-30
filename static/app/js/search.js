const input = document.getElementById("search-input");
const searchBtn = document.getElementById("search-btn");

const expand = () => {
    searchBtn.classList.toggle("close");
    input.classList.toggle("square");
};

searchBtn.addEventListener("click", expand);
// $(document).ready(function() {
//     $("#search-input").keyup(function() {
//         let key = $(this).val();
//         alert("{% url 'main:search' %}");
//         $.post("{% url 'main:search' %}", {
//             key: key
//         }, function(dataResponse) {
//             $("#list_bill").html(dataResponse);
//         });
//     });
// });