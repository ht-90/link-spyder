function createTooltip(opacity) {
  var tooltip = d3
    .select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", opacity);

  return tooltip;
};


function addTooltip(obj, tooltip) {
  obj
    .on("mouseover", function (event, d) {
      tooltip.transition().duration(200);
      tooltip
        .html(
          "Page: " +
          d.page +
          "<br/>" +
          "Category: " +
          d.category +
          "<br/>" +
          "Full path: " +
          d.id
        )
        .style("left", event.pageX + "px")
        .style("top", event.pageY - 28 + "px")
        .style("opacity", 0.9);
    })
    .on("mouseout", function (d) {
      tooltip.transition().duration(500).style("opacity", 0);
    });
};
