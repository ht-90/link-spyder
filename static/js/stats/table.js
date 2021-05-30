// Create a table
function createTable(table, headers, data) {
  var header = table.append("thead").append("tr");
  header
    .selectAll("th")
    .data(headers)
    .enter()
    .append("th")
    .text(function (d) {
      return d;
    });

  var tablebody = table.append("tbody");
  rows = tablebody.selectAll("tr").data(data).enter().append("tr");
  cells = rows
    .selectAll("td")
    .data(function (d) {
      return d;
    })
    .enter()
    .append("td")
    .text(function (d) {
      return d;
    });
}


function createTopFiveTable(container, id, title, headers, data) {
  var table = container
    .append("div")
    .attr("id", id)
    .attr("class", "tile is-child notification is-light")
    .append("p")
    .attr("class", "heading is-size-6 has-text-centered")
    .text(title)
    .append("table")
    .attr("class", "table");

  createTable(
    (table = table),
    (headers = headers),
    (data = data)
  );
};
