function clearGraph(dom) {
  if (d3.select(dom)) {
    d3.select(dom).selectAll("*").remove();
  };
};
