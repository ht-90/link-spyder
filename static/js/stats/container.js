function addStatsContainer(obj, data) {
  obj
    .append("div")
    .attr("id", "stats-kpi")
    .attr("class", "tile is-child notification is-light")
    .html(
      '<nav class="level">' +
      '<div class="level-item has-text-centered">' +
      "<div>" +
      '<p class="heading is-size-6">' +
      "Pages Discovered" +
      "</p>" +
      '<p class="title">' +
      data.pages_found +
      "</p>" +
      "</div>" +
      "</div>" +
      '<div class="level-item has-text-centered">' +
      "<div>" +
      '<p class="heading is-size-6">' +
      "Internal Links Discovered" +
      "</p>" +
      '<p class="title">' +
      data.links_found +
      "</p>" +
      "</div>" +
      "</div>" +
      "</nav>"
    );
};
