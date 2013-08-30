// adds startswith
if (typeof String.prototype.startswith != 'function') {
  // see below for better implementation!
  String.prototype.startswith = function (str){
    return this.indexOf(str) == 0;
  };
}

function UrlSubmit(URL) {
    
    var input_id=window.name.replace(/____/g,'-').split("___").join(".");
    var link_id = 'link_' + input_id;
    input = opener.document.getElementById(input_id);
    link = opener.document.getElementById(link_id);
    // set new value for input field
    if (URL.startswith('http://'+current_site)) { // absolute URL are saved, but path-relatives are wished
      URL = URL.substring(('http://'+current_site).length);
    }
    input.value = URL;
    this.close();
}

$(function($) {
  $('.node').click(function(e) {
    e.preventDefault();
    e.stopPropagation();
    $this_ul = $(this).parent()
    children = $this_ul.find('.children');
    if (children.length > 0) {
      $(children[0]).slideToggle();
    };
    // ▶ = &#9658; and ▼ = &#9660;
    $icon = $(this).find('.icon');
    $icon.toggleClass('closed');
    if ($icon.hasClass('closed')) {
      $icon.html('&#9660;'); //toggle
    } else {
      $icon.html('&#9658;'); //toggle
    };
  })
});