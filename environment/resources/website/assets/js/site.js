// Set notification in local storage
function setNotificationMessage(category, text) {
    const notificationObject = { category, text };
    localStorage.setItem(
    "notificationMessage",
    JSON.stringify(notificationObject)
    );
}

document.addEventListener("DOMContentLoaded", function () {
    // Start: Toastr, Check if there is a notification message in local storage
    const storedNotification = JSON.parse(
    localStorage.getItem("notificationMessage")
    );

    if (storedNotification) {
    // Extract category and text from the stored object
    const { category, text } = storedNotification;

    // Display the notification message using Toastr based on the category
    if (category === "success") {
        toastr.success(text);
    } else if (category === "error") {
        toastr.error(text);
    } else if (category === "info") {
        toastr.info(text);
    }

    // Clear the notification message from local storage
    localStorage.removeItem("notificationMessage");
    }
    // End: Toastr, Check if there is a notification message in local storage

    // Start: Get URL parameters and populate the search box and category selected when the search results page loads
    const searchInput = document.getElementById("searchInput");
    const searchCategory = document.getElementById("searchCategory");
    const categoryRender = document.getElementById(
    "select2-searchCategory-container"
    );

    const searchCategoryFromUrl = getParameterByName("category");
    const searchInputFromUrl = getParameterByName("name");

    const decodedCategory = decodeURIComponent(searchCategoryFromUrl);
    const decodedSerchInput = decodeURIComponent(searchInputFromUrl);

    if (searchCategoryFromUrl) {
    searchCategory.value = decodedCategory;
    categoryRender.title = decodedCategory;
    categoryRender.textContent = decodedCategory;
    }
    if (searchInputFromUrl) {
    searchInput.value = decodedSerchInput;
    }
    // End: Get URL parameters and populate the search box and category selected when the search results page loads
});

// Add an event listener to trigger the search on pressing 'Enter'
document
    .getElementById("searchInput")
    .addEventListener("keyup", function (event) {
    if (event.key === "Enter") {
        performSearch();
    }
    });

// Perform search by using the search bar
function performSearch() {
    const searchCategory = document.getElementById("searchCategory").value;
    const searchTerm = document.getElementById("searchInput").value;
    if (searchTerm != "") {
    // const loadingDiv = document.getElementById('loadingDiv');
    loadingDiv.style.display = "";

    const searchUrl = `/foodshare/search?category=${encodeURIComponent(
        searchCategory
    )}&name=${encodeURIComponent(searchTerm)}`;
    window.location.href = searchUrl;
    }
}

// Perform search by clicking the category
function performSearchByCategory(category) {
    // const loadingDiv = document.getElementById('loadingDiv');
    loadingDiv.style.display = "";

    const searchUrl = `/foodshare/search?category=${encodeURIComponent(
    category
    )}`;
    window.location.href = searchUrl;
}

// Get URL Parameter
function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, "\\$&");
    const regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return "";
    return results[2].replace(/\+/g, " ");
}