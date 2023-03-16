var districtObject = {
    "Kasargode": ["Links", "Images", "Tables", "Lists"],
    "Kannur": ["Borders", "Margins", "Backgrounds", "Float"],
    "Wayanad": ["Variables", "Operators", "Functions", "Conditions"]
  },
  window.onload = function() {
  var districtSel = document.getElementById("district");
  var placeSel = document.getElementById("place");
  for (var x in districtObject) {
    districtSel.options[districtSel.options.length] = new Option(x, x);
  }
  districtSel.onchange = function() {
    //empty Chapters- and Topics- dropdowns
    placeSel.length = 1;
    //display correct values
    var y = districtObject[districtSel.value][this.value];
    for (var i = 0; i < y.length; i++) {
     placeSel.options[placeSel.options.length] = new Option(y[i], y[i]);
     }
  }
