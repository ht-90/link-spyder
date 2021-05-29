function createDragHandler(obj, sim) {
  // Create drag behaviours
  var dragHandler = d3
    .drag()
    .on("start", dragstarted)
    .on("drag", dragged)
    .on("end", dragended);

  function dragstarted(event, d) {
    if (!event.active) sim.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
  };

  function dragged(event, d) {
    d.fx = event.x;
    d.fy = event.y;
  };

  function dragended(event, d) {
    if (!event.active) sim.alphaTarget(0);
    d.fx = null;
    d.fy = null;
  };

  // Add drag functionality to obj
  dragHandler(obj);
};
