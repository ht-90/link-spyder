function createLegend(width, group) {
  var w = width;
  var legend = d3
    .select("div#legend")
    .append("svg")
    .attr("width", w)
    .attr("height", group.length * 25);

  return legend;
};


function addLegendSymbol(legend, group, color) {
  legend
    .selectAll("circle")
    .data(group)
    .enter()
    .append("circle")
    .attr("cx", 50)
    .attr("cy", function (d, i) {
      return 15 + i * 25;
    })
    .attr("r", 7)
    .style("fill", function (d, i) {
      return color(d.category);
    });
};


function addLegendText(legend, width, group, color) {
  var w = width;
  // Create legend text
  legend
    .selectAll("labels")
    .data(group)
    .enter()
    .append("text")
    .attr("x", 70)
    .attr("y", function (d, i) {
      return 15 + i * 25;
    })
    .style("fill", function (d) {
      return color(d.category);
    })
    .text(function (d) {
      return d.category_url;
    })
    .attr("text-anchor", "left")
    .style("alignment-baseline", "middle");

  // Position legend text
  legend
    .append("text")
    .attr("x", w - 24)
    .attr("y", 9)
    .attr("dy", ".35em")
    .style("text-anchor", "end")
    .text(function (d) {
      return d;
    });
};
