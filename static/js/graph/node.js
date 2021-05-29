function sizeNode(circles, data) {
  // Prepare node size ratio
  var size_limit = 30;
  var max_size = 0;
  for (var i = 0; i < data.length; ++i) {
    if (max_size < data[i].size) {
      max_size = data[i].size;
    }
  }
  var size_ratio = size_limit / max_size;

  // Apply size
  circles
    .attr("r", function (d) {
      return d.size * size_ratio + 7;
    })
};


function colorNode(circles, color) {
  // Fill color
  circles
    .attr("fill", function (d) {
      return color(d.category);
    })
};


// Prepare short labels
function truncate(str, n) {
  if (str.length <= n) {
    return str;
  } else {
    return (
      str.substr(0, 8) + "..." + str.substr(str.length - 7, str.length)
    );
  };
};


function addLabel(obj) {
  obj
    .append("text")
    .text(function (d) {
      return truncate(d.page, 20);
    })
    .attr("x", 6)
    .attr("y", 3);
};
