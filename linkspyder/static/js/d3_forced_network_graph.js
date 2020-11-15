/*
d3_forced_network_graph.js

@author: ht-90
*/


$("document").ready(function(){

  $("#execute-crawl").click(function(e) {
    e.preventDefault();

    // Clear existing svg
    if (d3.select("svg")) {
      d3.select("svg")
        .selectAll("*")
        .remove();
    }

    // Create svg with width and height attributes
    var svg = d3.select("svg"),
        width = +svg.attr("width"),
        height = +svg.attr("height");
  
    // Set a color scheme
    var color = d3.scaleOrdinal(d3.schemeCategory10);  

    var url = document.getElementById("input-url").value;
    console.log("INPUT URL:", url);

    // Load data and create a graph
    d3.json("/data", {
      method:"POST",
      body: url,
      headers: {
        "Content-type": "application/json; charset=UTF-8"
      }
    }).then(function(data) {

      console.log("data", data)


      // Set force for a graph
      var simulation = d3.forceSimulation()
          .force("link", d3.forceLink().id(function(d) { return d.id; }).distance(100))
          .force("charge", d3.forceManyBody().strength(-1000))
          .force("center", d3.forceCenter(width / 2, height / 2))
          .force("collide", d3.forceCollide().radius(d => d.r * 10));

      // Append links to svg
      var link = svg.append("g")
            .attr("class", "links")
          .selectAll("line")
          .data(data.links)
          .enter()
          .append("line")
            .attr("stroke-width", function(d) { return Math.sqrt(d.value); });

      // Append nodes to svg
      var node = svg.append("g")
            .attr("class", "nodes")
          .selectAll("g")
          .data(data.nodes)
          .enter()
          .append("g")

      // Add behaviour to nodes ???
      var circles = node.append("circle")
            .attr("r", 5)
            .attr("fill", function(d) { return color(d.source_category); })
          .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended)
          );
      
      // Add node labels
      var labels = node.append("text")
          .text(function(d) { return d.id; })
            .attr("x", 6)
            .attr("y", 3);
      
      // Add title tag and text to nodes
      node.append("title")
        .text(function(d) { return d.id; });

      // 
      simulation
        .nodes(data.nodes)
        .on("tick", ticked);

      // 
      simulation.force("link")
        .links(data.links);

      // 
      function ticked () {
        link
          .attr("x1", function(d) { return d.source.x; })
          .attr("y1", function(d) { return d.source.y; })
          .attr("x2", function(d) { return d.target.x; })
          .attr("y2", function(d) { return d.target.y; });
        node
          .attr("transform", function(d) {
            return "translate(" + d.x + "," + d.y + ")";
          })
        }

      });

    function dragstarted(d) {
      if (!d3.event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(d) {
      d.fx = d3.event.x;
      d.fy = d3.event.y;
    }

    function dragended(d) {
      if (!d3.event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }

  });
});
