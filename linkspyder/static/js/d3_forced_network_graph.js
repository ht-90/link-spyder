/*
d3_forced_network_graph.js

@author: ht-90
*/

$("document").ready(function () {
  $("#execute-crawl").click(function (e) {
    e.preventDefault();

    // Clear existing svg
    if (d3.select("svg")) {
      d3.select("svg").selectAll("*").remove();
    }

    // Create svg with width and height ratio
    var svg = d3
      .select("div#container")
      .append("svg")
      .attr("preserveAspectRatio", "xMinYMin meet")
      .attr("viewBox", "0 0 960 600")
      .classed("svg-content", true);

    // Get container width and height values
    var svgContainer = document.getElementById("container");
    var width = svgContainer.clientWidth;
    var height = svgContainer.clientHeight;

    // Adjust the svg viewBox based on a container size
    d3.select("svg")
      .attr("width", width)
      .attr("height", height * 0.8);

    // Set a color scheme
    var color = d3.scaleOrdinal(d3.schemeCategory10);

    // Get input URL
    var url = document.getElementById("input-url").value;
    console.log("INPUT URL:", url);

    // Load data and create a graph
    d3.json("/data", {
      method: "POST",
      body: url,
      headers: {
        "Content-type": "application/json; charset=UTF-8",
      },
    }).then(function (data) {
      console.log("GRAPH DATA", data.graph);
      console.log("GROUP DATA", data.category);

      graph = data.graph;
      group = data.category;

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

      // Add behaviour to nodes ???
      var circles = node
        .append("circle")
        .attr("r", 10)
        .attr("fill", function (d) {
          return color(d.category);
        })
        .call(
          d3
            .drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended)
        );

      // Add node labels
      var labels = node
        .append("text")
        .text(function (d) {
          return d.page;
        })
        .attr("x", 6)
        .attr("y", 3);

      // Add title tag and text to nodes
      node.append("title").text(function (d) {
        return d.id;
      });

      // Graph legend
      var legend = d3
        .select("div#legend")
        .append("svg")
        .attr("width", width)
        .attr("height", group.length * 25);

      // Add legend symbols
      legend
        .selectAll("circle")
        .data(group)
        .enter()
        .append("circle")
        .attr("cx", 50)
        .attr("cy", function (d, i) {
          return 15 + i * 25;
        })
        .attr("r", 7)
        .style("fill", function (d, i) {
          return color(d.category);
        });

      // Add legend texts
      legend
        .selectAll("labels")
        .data(group)
        .enter()
        .append("text")
        .attr("x", 70)
        .attr("y", function (d, i) {
          return 15 + i * 25;
        })
        .style("fill", function (d) {
          return color(d.category);
        })
        .text(function (d) {
          return d.category_url;
        })
        .attr("text-anchor", "left")
        .style("alignment-baseline", "middle");

      legend
        .append("text")
        .attr("x", width - 24)
        .attr("y", 9)
        .attr("dy", ".35em")
        .style("text-anchor", "end")
        .text(function (d) {
          return d;
        });

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
});
