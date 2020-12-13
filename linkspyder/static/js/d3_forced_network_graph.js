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

    // Prepare tooltip container
    var div = d3
      .select("body")
      .append("div")
      .attr("class", "tooltip")
      .style("opacity", 0);

    var viz_container = d3
      .select("div#viz-container");

    // Add containers for viz
    viz_container
      .append("div")
      .attr("class", "tile is-child notification is-light")
      .append("div")
      .attr("id", "container")
      .attr("class", "svg-container");

    // Add containers for viz legend
    viz_container
      .append("div")
      .attr("class", "tile is-child notification is-light")
      .append("div")
      .attr("id", "legend")
      .attr("class", "legend-container");

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
    var url = document.getElementById("input-url").value;
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
    var stats_container = d3
      .select("#stats-container")

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

      // Prepare node size ratio
      var size_limit = 30;
      var max_size = 0;
      for (var i = 0; i < graph.nodes.length; ++i) {
        if (max_size < graph.nodes[i].size) {
          max_size = graph.nodes[i].size;
        }
      }
      var size_ratio = size_limit / max_size;

      // Add circles as nodes
      var circles = node
        .append("circle")
        .attr("r", function (d) {
          return d.size * size_ratio + 7;
        })
        .attr("fill", function (d) {
          return color(d.category);
        })
        .on("mouseover", function (event, d) {
          div.transition().duration(200);
          div
            .html(
              "Page: " +
                d.page +
                "<br/>" +
                "Category: " +
                d.category +
                "<br/>" +
                "Full path: " +
                d.id
            )
            .style("left", event.pageX + "px")
            .style("top", event.pageY - 28 + "px")
            .style("opacity", 0.9);
        })
        .on("mouseout", function (d) {
          div.transition().duration(500).style("opacity", 0);
        });

      // Create a node drag behaviour
      var dragHandler = d3
        .drag()
        .on("start", dragstarted)
        .on("drag", dragged)
        .on("end", dragended);

      dragHandler(node);

      // Prepare short labels
      function truncate(str, n) {
        if (str.length <= n) {
          return str;
        } else {
          return (
            str.substr(0, 8) + "..." + str.substr(str.length - 7, str.length)
          );
        }
      }

      // Add node labels
      var labels = node
        .append("text")
        .text(function (d) {
          return truncate(d.page, 20);
        })
        .attr("x", 6)
        .attr("y", 3);

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

      // Add Web Statistics
      stats_container
        .append("div")
        .attr("id", "stats-kpi")
        .attr("class", "tile is-child notification is-light")
        .html(
          '<nav class="level">'
          + '<div class="level-item has-text-centered">'
            + '<div>'
              + '<p class="heading is-size-6">' + 'Pages Discovered' + '</p>'
              + '<p class="title">' + stats.pages_found + '</p>'
            + '</div>'
          + '</div>'
          + '<div class="level-item has-text-centered">'
            + '<div>'
              + '<p class="heading is-size-6">' + 'Internal Links Discovered' + '</p>'
              + '<p class="title">' + stats.links_found + '</p>'
            + '</div>'
          + '</div>'
          + '</nav>'
        )

      // Create a table for top outgoing pages
      var table = stats_container
        .append("div")
        .attr("id", "stats-top-outgoing")
        .attr("class", "tile is-child notification is-light")
        .append("p")
        .attr("class", "heading is-size-6 has-text-centered")
        .text("Top Outgoing Pages")
        .append("table")
        .attr("class", "table");
      createTable(
        table=table,
        headers=["Page", "No. of Outgoing Links"],
        data=stats.top_outgoing_pages
      );
      // Create a table for top incoming pages
      var table = stats_container
        .append("div")
        .attr("id", "stats-top-incoming")
        .attr("class", "tile is-child notification is-light")
        .append("p")
        .attr("class", "heading is-size-6 has-text-centered")
        .text("Top Incoming Pages")
        .append("table")
        .attr("class", "table");
      createTable(
        table=table,
        headers=["Page", "No. of Incoming Links"],
        data=stats.top_incoming_pages
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

    // Create a table
    function createTable(table, headers, data) {
      var header = table.append("thead").append("tr");
      header
        .selectAll("th")
        .data(headers)
        .enter()
        .append("th")
        .text(function(d) { return d; });

      var tablebody = table.append("tbody");
      rows = tablebody
        .selectAll("tr")
        .data(data)
        .enter()
        .append("tr");
      cells = rows
        .selectAll("td")
        .data(function (d) { return d; })
        .enter()
        .append("td")
        .text(function(d) { return d; });
    };

  });
});
