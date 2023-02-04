
document.getElementById("option_language").addEventListener("change", function () {
  const text = this.options[this.selectedIndex].text
  document.getElementById("search_text").placeholder = text;

  lastSelected = this.options[this.selectedIndex].value;
  localStorage.setItem('select', lastSelected);
  searchText = this.options[this.selectedIndex].text;
  localStorage.setItem('searchBox', searchText);

})
var select = document.getElementById("option_language");
var lastSelected = localStorage.getItem('select');
var box =document.getElementById("search_text");
var searchText = localStorage.getItem('searchBox');
if(lastSelected) {
  select.value = lastSelected;
  box.placeholder=searchText
 
}



  