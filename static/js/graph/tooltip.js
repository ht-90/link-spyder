function createTooltip(opacity) {
  var tooltip = d3
    .select("body")
    .append("div")
    .attr("class", "tooltip")
    .style("opacity", opacity);

  return tooltip;
};

