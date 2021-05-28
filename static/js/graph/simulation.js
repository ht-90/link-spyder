function simulateGraph(width, height, dist, str, rad) {
  var w = width;
  var h = height;
  var simulation = d3
    .forceSimulation()
    .force(
      "link",
      d3
        .forceLink()
        .id(function (d) {
          return d.id;
        })
        .distance(dist)
    )
    .force("charge", d3.forceManyBody().strength(str))
    .force("center", d3.forceCenter(w / 2, h / 2))
    .force(
      "collide",
      d3.forceCollide().radius((d) => d.r * rad)
    );

  return simulation;
};


function rerunNodeSimulation(sim, node, node_data, link) {
  sim.nodes(node_data).on("tick", ticked);

  function ticked() {
    link
      .attr("x1", function (d) {
        return d.source.x;
      })
      .attr("y1", function (d) {
        return d.source.y;
      })
      .attr("x2", function (d) {
        return d.target.x;
      })
      .attr("y2", function (d) {
        return d.target.y;
      });
    node.attr("transform", function (d) {
      return "translate(" + d.x + "," + d.y + ")";
    });
  };
};


function rerunLinkSimulation(sim, link_data) {
  sim.force("link").links(link_data);
};
