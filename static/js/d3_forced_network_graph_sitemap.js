/*
d3_forced_network_graph.js

@author: ht-90
*/

$("document").ready(function () {
  $("#execute-crawl-sitemap").click(function (e) {
    e.preventDefault();

    // Clear existing svg
    clearGraph("svg");

    // Prepare tooltip container
    var tooltip = createTooltip(0);

    // Create containers
    createGraphContainer("div#viz-container");
    createLegendContainer("div#viz-container");

    // Create svg with width and height ratio
    var svg = d3
      .select("div#container")
      .append("svg")
      .attr("width", "100%")
      .attr("height", "600")
      .classed("svg-content", true)
      .call(
        d3.zoom().on("zoom", function (event, d) {
          svg.attr("transform", event.transform);
        })
      )
      .append("g");

    // Get container width and height values
    var svgContainer = document.getElementById("container");
    var width = svgContainer.clientWidth;
    var height = svgContainer.clientHeight;

    // Set a color scheme
    var color = d3.scaleOrdinal(d3.schemeCategory10);

    // Get input URL
    var url = document.getElementById("input-url-sitemap").value;
    console.log("INPUT URL:", url);

    // Set force for a graph
    var simulation = d3
      .forceSimulation()
      .force(
        "link",
        d3
          .forceLink()
          .id(function (d) {
            return d.id;
          })
          .distance(100)
      )
      .force("charge", d3.forceManyBody().strength(-1000))
      .force("center", d3.forceCenter(width / 2, height / 2))
      .force(
        "collide",
        d3.forceCollide().radius((d) => d.r * 10)
      );

    // Web Statistics
    var stats_container = d3.select("#stats-container");

    // Load data and create a graph
    d3.json("/sitemapper", {
      method: "POST",
      body: url,
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    }).then(function (data) {
      console.log("GRAPH DATA", data.graph);
      console.log("GROUP DATA", data.category);
      console.log("STATS DATA", data.stats);

      graph = data.graph;
      group = data.category;
      stats = data.stats;

      // Append links to svg
      var link = svg
        .append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(graph.links)
        .enter()
        .append("line")
        .attr("stroke-width", function (d) {
          return Math.sqrt(d.value);
        });

      // Append nodes to svg
      var node = svg
        .append("g")
        .attr("class", "nodes")
        .selectAll("g")
        .data(graph.nodes)
        .enter()
        .append("g");

      addLabel(node);

      // Add circles as nodes
      var circles = node.append("circle");
      sizeNode(circles, graph.nodes);
      colorNode(circles, color);

      // Add tooltip to circles
      addTooltip(circles, tooltip);

      // Create a node drag behaviour
      var dragHandler = d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);

      dragHandler(node);


      // Graph legend
      var legend = createLegend(width, group);
      addLegendSymbol(legend, group, color);
      addLegendText(legend, width, group, color);

      // Add Web Statistics
      addStatsContainer(stats_container, stats);

      // Create a table for top outgoing pages
      createTopFiveTable(
        stats_container,
        "stats-top-outgoing",
        "Top Outgoing Pages",
        ["Page", "No. of Outgoing Links"],
        stats.top_outgoing_pages,
      );
      createTopFiveTable(
        stats_container,
        "stats-top-incoming",
        "Top Incoming Pages",
        ["Page", "No. of Incoming Links"],
        stats.top_incoming_pages,
      );

      //
      simulation.nodes(graph.nodes).on("tick", ticked);

      //
      simulation.force("link").links(graph.links);

      //
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
      }
    });

    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }
  });
});
