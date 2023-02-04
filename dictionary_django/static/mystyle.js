
document.getElementById("option_language").addEventListener("change", function() {
  const text = this.options[this.selectedIndex].text
  document.getElementById("search_text").placeholder = text;
                            
  var select = document.querySelector(".option_language");
  var selectOption = select.options[select.selectedIndex];
  var lastSelected = localStorage.getItem('select');
  lastSelected = select.options[select.selectedIndex].value;
  console.log(lastSelected);
  localStorage.setItem('select', lastSelected);
  })

