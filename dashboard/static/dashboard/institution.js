document.addEventListener("DOMContentLoaded", function () {

    const sectorField = document.getElementById("id_sector");
    const institutionField = document.getElementById("id_institution");


    const publicInstitutions = [
        ["ministry", "Government Ministry"],
        ["department", "Government Department"],
        ["municipality", "Municipality / Town Council"],
        ["parastatal", "Parastatal"],
        ["police", "Police Service"],
        ["public_health", "Public Health Facility"],
        ["public_school", "Public School"],
        ["public_university", "Public University / College"],
        ["procurement", "Procurement Unit"],
        ["revenue", "Revenue Collection Agency"],
        ["other_public", "Other Public Institution"],
    ];


    const privateInstitutions = [
        ["insurance", "Insurance Company"],
        ["telecom", "Telecommunications"],
        ["transport", "Transport Company"],
        ["construction", "Construction Company"],
        ["textile", "Textile / Manufacturing"],
        ["retail", "Retail Business"],
        ["mining", "Mining Company"],
        ["agriculture", "Agriculture Business"],
        ["hotel", "Hotel / Tourism"],
        ["private_health", "Private Health Facility"],
        ["private_school", "Private School"],
        ["private_university", "Private University / College"],
        ["security", "Security Company"],
        ["other_private", "Other Private Institution"],
    ];


    function updateInstitutions() {

        institutionField.innerHTML = "";

        let selectedList = [];


        if (sectorField.value === "public") {

            selectedList = publicInstitutions;

        } else if (sectorField.value === "private") {

            selectedList = privateInstitutions;

        }


        selectedList.forEach(function(item){

            let option = document.createElement("option");

            option.value = item[0];
            option.text = item[1];

            institutionField.appendChild(option);

        });

    }


    sectorField.addEventListener(
        "change",
        updateInstitutions
    );


    updateInstitutions();

});