document.addEventListener("DOMContentLoaded", function () {
  const filterBtns = document.querySelectorAll(
    ".index-nav-category-detail-btn"
  );

  filterBtns.forEach(function (button) {
    button.addEventListener("click", function () {
      const filterValue = this.dataset.filter;
      filterProducts(filterValue);

      console.log("Button clicked! Filter value:", filterValue);
    });
  });

  function filterProducts(filterValue) {
    const productCards = document.querySelectorAll(".index-product");

    productCards.forEach(function (card) {
      const productOrigin = card.dataset.origin;
      const productRoast = card.dataset.roast;

      const originMatch =
        productOrigin === "All" || filterValue === productOrigin;
      const roastMatch = productRoast === "All" || filterValue === productRoast;

      if (originMatch) {
        card.style.display = "block";
      } else if (roastMatch) {
        card.style.display = "block";
      } else if (filterValue === "All") {
        card.style.display = "block";
      } else {
        card.style.display = "none";
      }
    });
  }
});
