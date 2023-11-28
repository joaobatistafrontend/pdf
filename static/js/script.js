const icon = document.querySelector(".icon");
const nav = document.querySelector(".nav-bar");
const navLinks = document.querySelectorAll(".nav-link")

icon.addEventListener("click", () => nav.classList.toggle("active"));

navLinks.forEach(function(navLink) {
    navLink.addEventListener("click", () => {
        if(nav.classList.contains("active")){
            nav.classList.remove("active");
        }
    });
});

function changeTo(sectionId) {
    let navbarHeight = document.querySelector('#inicio').offsetHeight;
    let section = document.getElementById(sectionId);

    if (section) {
        let sectionPosition = section.getBoundingClientRect().top;
        let space = navbarHeight; // 10 pixels de margem

        window.scrollBy({
            top: sectionPosition - space,
            left: 0,
            behavior: "smooth",
          });
    }
}

let buttons = document.querySelectorAll(".button-unidade");

buttons.forEach(function(button) {
  button.addEventListener("click", function() {
    let divPai = button.closest(".card-body");
    
    let rua = divPai.querySelector(".rua").textContent.trim();
    let estado = divPai.querySelector(".card-estado").textContent.trim();
    let numero = divPai.querySelector(".numero").textContent.trim();

    let endereco = estado + " - " + rua + " - " + numero;

    console.log(endereco)

    selectEnderecoValue(endereco);
    changeTo("section-agendamento");
  });
});

function selectEnderecoValue(value){
    var select = document.getElementById("id_locais");

    for (let i = 0; i < select.options.length; i++) {
        if (select.options[i].text  === value) {
            select.options[i].selected = true;
            break;
        }
    }
}