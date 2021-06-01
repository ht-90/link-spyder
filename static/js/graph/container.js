function createGraphContainer(dom) {

  // Select an element
  var container = d3.select(dom);

  // Add containers for viz
  container
    .append("div")
    .attr("class", "tile is-child notification is-light")
    .append("div")
    .attr("id", "container")
    .attr("class", "svg-container");

};


function createLegendContainer(dom) {

  // Select an element
  var container = d3.select(dom);

  // Add containers for viz legend
  container
    .append("div")
    .attr("class", "tile is-child notification is-light")
    .append("div")
    .attr("id", "legend")
    .attr("class", "legend-container");

};
